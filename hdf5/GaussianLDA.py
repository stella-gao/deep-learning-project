from __future__ import division
import gensim
import numpy as np
from numpy import log, pi, linalg, exp
from scipy.special import gamma, gammaln
import random
from collections import defaultdict



class Wishart(object):

    def __init__(self, word_vecs):
        self.nu = None
        self.kappa = None
        self.psi = None

        self.set_params(word_vecs)

    def set_params(self, word_vecs):
        #turn dict of word vecs into a matrix
        word_vecs = np.vstack(word_vecs.values())

        self.nu = word_vecs.shape[1] #len of columns
        self.kappa = 0.01
        self.psi = np.sum(word_vecs.T.dot(word_vecs), axis=0) # should this be np.sum(x.dot(x.T)))??? also changed this to x.T.dot(x)
        self.mu = np.mean(word_vecs, axis=0)
        print "psi shape", self.psi.shape



class Gauss_LDA(object):

    def __init__(self, num_topics, corpus, word_vector_filepath):
        self.doc_topic_CT = None
        self.word_topics = {}
        self.corpus = corpus
        self.vocab = None
        self.priors = None
        self.word_vecs = {}
        self.numtopics = num_topics
        self.vocab = set([])
        self.topic_params = defaultdict(dict)
        self.wordvecFP = word_vector_filepath
        self.word_index = {}
        self.word_vec_size = None
        self.alpha = 50./self.numtopics


    def process_corpus(self, documents):
        """
        Takes a list of documents, and processes them
        sets vocab
        returns: None
        """
        temp_corpus = {}
        for index, doc in enumerate(documents):
            words = doc.split()
            temp_corpus[index] = words
            for word in words:
                self.vocab.add(word)
        self.corpus = temp_corpus
        print "Done processing corpus with {} documents".format(len(documents))


    def process_wordvectors(self, filepath):
        print "Processing word-vectors, this takes a moment"

        vectors = gensim.models.Word2Vec.load_word2vec_format(fname=filepath, binary=False)
        useable_vocab = 0
        unusable_vocab = 0
        self.word_vec_size = vectors.vector_size

        for word in self.vocab:
            try:
                vectors[word]
                useable_vocab += 1
            except KeyError: unusable_vocab += 1

        print "There are {0} words that could be convereted to word vectors in your corpus \n" \
              "There are {1} words that could NOT be converted to word vectors".format(useable_vocab, unusable_vocab)

        # self.word_vecs = np.zeros((useable_vocab, vectors.vector_size))
        index = 0
        for word in self.vocab:
            try:
                self.word_vecs[word] = vectors[word]
                index += 1
            except KeyError: continue
        print "Word-vectors for the corpus are created"


    def fit(self, iterations=1, init=True): #set hyperparams here?
        if init == True:
            self.init()
            init = False

        print "Starting fit"
        for i in xrange(iterations):
            self.sample()
            print "{} iterations complete".format(i)

    def init(self):

        self.process_corpus(self.corpus)
        self.process_wordvectors(self.wordvecFP)
        #setting wishhart priors
        self.priors = Wishart(self.word_vecs)
        self.doc_topic_CT = np.zeros((len(self.corpus.keys()), self.numtopics))

        self.word_topics = {word: random.choice(range(self.numtopics)) for word in self.vocab}
        # get Doc-Topic Counts
        for docID, doc in self.corpus.iteritems():
            for word in doc:
                topicID = self.word_topics[word]
                self.doc_topic_CT[docID, topicID] += 1

        # Init parameters for topic distributions
        for k in range(self.numtopics):
            self.recalculate_topic_params(k)

        print "Intialization complete"
    def sample(self, init=True):

        print "sampling started"
        # Randomly assign word to topics
        if init == False:
            self.word_topics = {word: random.choice(range(self.numtopics)) for word in self.vocab}

        for docID, doc in self.corpus.iteritems():
            for word in doc:
                #subtracting info about current word-topic assignment from doc-topic count table
                topic_id = self.word_topics[word]
                self.doc_topic_CT[docID, topic_id] - doc.count(word)

                self.recalculate_topic_params(topic_id)
                posterior = []
                max = 0
                for k in range(self.numtopics): #start getting the pdf's for each word-topic assignment
                    log_prob = self.draw_new_wt_assgns(word, k)
                    # Count of topic in doc
                    Nkd = self.doc_topic_CT[docID, k]
                    log_posterior = log(Nkd + self.alpha) * log_prob
                    posterior.append(log_posterior)
                    #doing this for some normalization scheme
                    if log_posterior > max: max = log_posterior

                normalized_posterior = [exp(i-max) for i in posterior]
                print np.sum(posterior)
                print np.random.multinomial(1, pvals=posterior)
                ## need to copy the normalization scheme from Util.sample
        init = False
        return None

    def draw_new_wt_assgns(self, word, topic_id):

        # Getting params for calculating PDF of T-Dist for a word
        wordvec = self.word_vecs[word]
        inv_cov = self.topic_params[topic_id]["Inverse Covariance"]
        cov_det = self.topic_params[topic_id]["Covariance Determinant"]
        Nk = self.topic_params[topic_id]["Topic Count"]
        KappaK = self.topic_params[topic_id]["Topic Kappa"]
        centered = self.word_vecs[word] - self.priors.mu
        topic_cov = self.topic_params[topic_id]["Topic Covariance"]


        # Precalculating some terms (V_di - Mu)^T * Cov^-1 * (V_di - Mu)
        LLcomp = centered.T.dot(inv_cov).dot(centered)
        d = self.word_vec_size
        nu = self.priors.nu + Nk - d + 1

        log_prop = gammaln(nu + d / 2) - \
                   (gammaln(nu / 2) + d/2 * (log(nu) + log(pi)) +0.5 * log(cov_det) + (nu + d) / 2 * log(1 + LLcomp / nu))

        return log_prop
        # logprob = Gamma.logGamma((nu + Data.D)/2) - \
        #           (Gamma.logGamma(nu/2) + Data.D/2 * (Math.log(nu)+Math.log(Math.PI)) + 0.5 * Math.log(det) + (nu + Data.D)/2* Math.log(1+val/nu))

    def recalculate_topic_params(self, topic_id):

        topic_count = np.sum(self.doc_topic_CT[:, topic_id], axis=0) # N_k

        kappa_k = self.priors.kappa + topic_count # K_k
        nu_k = self.priors.nu + topic_count # V_k

        scaled_topic_mean_K, scaled_topic_cov_K  = self.get_scaled_topic_mean_cov(topic_id) # V-Bar_k and C_k

        vk_mu = scaled_topic_mean_K - self.priors.mu #V-bar_k - Mu
        print self.priors.psi
        psi_k = self.priors.psi + scaled_topic_cov_K + ((self.priors.kappa * topic_count) / kappa_k) * (vk_mu.T.dot(vk_mu)) # Psi_k

        topic_mean = (self.priors.kappa * self.priors.mu + topic_count * scaled_topic_mean_K) / kappa_k # Mu_k
        topic_cov = psi_k / (nu_k - self.word_vec_size + 1) # Sigma_k

        self.topic_params[topic_id]["Topic Count"] = topic_count
        self.topic_params[topic_id]["Topic Kappa"] = kappa_k
        self.topic_params[topic_id]["Topic Nu"] = nu_k
        self.topic_params[topic_id]["Topic Mean"], self.topic_params[topic_id]["Topic Covariance"] = topic_mean, topic_cov
        self.topic_params[topic_id]["Inverse Covariance"] = np.linalg.inv(topic_cov)
        self.topic_params[topic_id]["Covariance Determinant"] = np.linalg.det(topic_cov)
        self.topic_params[topic_id]["Liklihood Componant"] = None


        return topic_mean, topic_cov

    def get_scaled_topic_mean_cov(self, topic_id):
        'mean of word vecs in a topic'
        # get words assigned to topic_id
        word_vecs = []
        for word, topic in self.word_topics.iteritems():
            if topic == topic_id:
                word_vecs.append(self.word_vecs[word])
        print word_vecs
        word_vecs = np.vstack(word_vecs)
        print word_vecs.shape
        print np.sum(word_vecs, axis=0)
        print np.sum(self.doc_topic_CT[:, topic_id], axis=0)
        mean = np.sum(word_vecs, axis=0) / (np.sum(self.doc_topic_CT[:, topic_id], axis=0) + 2) #added a small number here to stop overflow

        # mean_centered = np.sum(word_vecs, axis=0) - mean
        mean_centered = word_vecs - mean
        print self.doc_topic_CT
        print mean
        print mean_centered

        cov = mean_centered.T.dot(mean_centered)
        return mean, cov

if __name__ == "__main__":
    corpus = ["apple orange mango melon", "dog cat bird rat"]
    wordvec_fileapth = "summary.txt"
    g = Gauss_LDA(2, corpus, wordvec_fileapth )
    g.fit(2)
    # print g.topic_params[1]["Topic Count"]
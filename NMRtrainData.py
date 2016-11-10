import numpy as np
import h5py
import scipy.io
np.random.seed(1337) # for reproducibility

from keras.preprocessing import sequence
from keras.optimizers import RMSprop, SGD
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from keras.regularizers import l2, activity_l1
from keras.constraints import maxnorm
from keras.layers.recurrent import LSTM, GRU
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.utils import np_utils

from keras.layers.embeddings import Embedding

from dna_io_new import *

file_name = 'humanNMR'
file_name_nm = 'NM1wtrain'
file_name_nr = 'NR1wtrain'
file_name_test = 'human_test'


seq_nm_len = longest_seq_len(file_name_nm+'.fa')
seq_nr_len = longest_seq_len(file_name_nr+'.fa')

print seq_nm_len
print seq_nr_len

max_len = max(seq_nm_len, seq_nr_len)
print max_len

seq_vecs_nm = hash_sequences_1hot(file_name_nm+'.fa', max_len)
seq_vecs_nr = hash_sequences_1hot(file_name_nr+'.fa', max_len)

seq_headers_nr = sorted(seq_vecs_nr.keys())
seq_headers_nm = sorted(seq_vecs_nm.keys())
# seq_headers_test = sorted(seq_vecs_test.keys())

# print len(seq_vecs_m)

##tmp = 0.25 * np.ones((4,26307-14080))
#tmp = 0.25 * np.ones((4, max(seq_lnc_len,seq_m_len) - min(seq_lnc_len, seq_m_len)))

train_seqs = []
train_scores = []

for header in seq_headers_nr:
    train_seqs.append(seq_vecs_nr[header])
    train_scores.append([1])

'''
for i in range(1000):
    train_seqs[i] = np.hstack((train_seqs[i],tmp))
'''
# print train_seqs.shape
print "--------"

for header in seq_headers_nm:
    train_seqs.append(seq_vecs_nm[header])
    train_scores.append([0])

train_seqs = np.array(train_seqs)
train_scores = np.array(train_scores)

# print train_seqs.shape

import h5py
h5f = h5py.File(file_name+'_train_1hot.hdf5', 'w')
h5f.create_dataset('x_train', data=train_seqs)
h5f.create_dataset('y_train', data=train_scores)
h5f.close()



#from __future__ import division

import os
os.environ['THEANO_FLAGS'] = "device=gpu"
import sys
sys.setrecursionlimit(15000)

import numpy
import h5py
import scipy.io
numpy.random.seed(1337) # for reproducibility



from keras.preprocessing import sequence
from keras.optimizers import RMSprop, SGD
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten, MaxoutDense
from keras.layers.convolutional import Convolution1D, MaxPooling1D, AveragePooling1D
from keras.layers.local import LocallyConnected1D
from keras.layers.pooling import AveragePooling1D

from keras.regularizers import l1, l2, activity_l1
from keras.constraints import maxnorm
from keras.layers.recurrent import LSTM, GRU
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers.wrappers import Bidirectional
from seya.layers.recurrent import Bidirectional
#from keras.utils.layer_utils import print_layer_shapes

from keras.layers.normalization import BatchNormalization
from residual_blocks import building_residual_block
from keras.utils import np_utils
from keras.layers.embeddings import Embedding
from sklearn.cross_validation import train_test_split

from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score

from hyperopt import Trials, STATUS_OK, tpe
from hyperas import optim
from hyperas.distributions import choice, uniform, conditional

file_name = sys.argv[1];
model_file_name = "./model/"+file_name+".all.bestmodel.hdf5";
result_file_name = "./result/"+file_name+'.all.res';

# arg 1: file_name

def data():
    file_name = sys.argv[1];
    trainmat = h5py.File('./' + file_name + '_train_1hot.hdf5', 'r')
    validmat = h5py.File('./' + file_name + '_valid_1hot.hdf5', 'r')
    testmat = h5py.File('./' + file_name + '_test_1hot.hdf5', 'r')

    X_train = numpy.transpose(numpy.array(trainmat['x_train']),axes=(0, 2, 1))
    y_train = numpy.array(trainmat['y_train'])

    X_test = numpy.transpose(numpy.array(testmat['x_test']),axes=(0, 2, 1))
    y_test = numpy.array(testmat['y_test'])

    X_valid = numpy.transpose(numpy.array(validmat['x_valid']),axes=(0, 2, 1))
    y_valid = numpy.array(validmat['y_valid'])

    return X_train, y_train, X_test, y_test, X_valid, y_valid


def model(X_train, Y_train, X_test, Y_test, X_valid, y_valid):
    '''
    Model providing function:

    Create Keras model with double curly brackets dropped-in as needed.
    Return value has to be a valid python dictionary with two customary keys:
        - loss: Specify a numeric evaluation metric to be minimized
        - status: Just use STATUS_OK and see hyperopt documentation if not feasible
    The last one is optional, though recommended, namely:
        - model: specify the model just created so that we can later use it again.
    '''

    NUM_FILTER1 = {{choice([64, 80, 100, 128, 200])}}
    INPUT_LENGTH = 10000
    FILTER_LENGTH1 = {{choice([64, 100, 128, 200])}}
    INIT_VALUE = {{choice(['uniform', 'lecun_uniform', 'normal', 'zero', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform'])}}

    print 'building model'
    model = Sequential()
    model.add(Convolution1D(input_dim=4, input_length=INPUT_LENGTH, nb_filter=NUM_FILTER1, filter_length=FILTER_LENGTH1, border_mode="valid", subsample_length=1, init=INIT_VALUE))

    model.add(MaxPooling1D(pool_length=45, stride=45))
    model.add(Dropout({{uniform(0, 1)}}))

    input_length, input_dim = model.output_shape[1:]
    nb_filter = {{choice([64, 100, 128, 200])}}
    filter_length = {{choice([4, 8, 10, 16])}}
    subsample = 1

    model.add(building_residual_block(r_input_length = input_length, r_input_dim = input_dim,
                                      r_nb_filter = nb_filter, r_filter_length = filter_length,
                                      is_subsample = True, n_skip =2, r_subsample = subsample))

    model.add(AveragePooling1D(pool_length=4, stride=4))
    model.add(Dropout({{uniform(0, 1)}}))

    input_length, input_dim = model.output_shape[1:]
    model.add(building_residual_block(r_input_length = input_length, r_input_dim = input_dim,
                                      r_nb_filter = nb_filter, r_filter_length = filter_length,
                                      is_subsample = True, n_skip =2, r_subsample = subsample))

    model.add(AveragePooling1D(pool_length=2, stride=2))
    model.add(Dropout({{uniform(0, 1)}}))

    model.add(Flatten())
    model.add(Dense(output_dim=150, init='glorot_uniform'))

    model.add(Activation({{choice(['relu', 'sigmoid', 'tanh', 'softmax'])}}))
    model.add(Dropout({{uniform(0, 1)}}))

    model.add(Dense(output_dim=1))
    model.add(Activation({{choice(['relu', 'sigmoid', 'tanh', 'softmax'])}}))

    print 'compiling model'
    sgd = SGD(lr={{choice([0.001, 0.003, 0.01, 0.03])}}, momentum=0.9, decay=1e-5, nesterov=True)
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])

    print model.summary()
    model.fit(X_train, y_train,
              batch_size=120,
              nb_epoch=80,
              shuffle=True,
              validation_data=(X_valid, y_valid))

    model.layers[1].get_weights()
    score, acc1 = model.evaluate(X_test, y_test, verbose=0)
    print 'predicting on test sequences'
    predret = model.predict(X_test, verbose=1)

    auc = roc_auc_score(y_test, predret)
    predret_class = model.predict_classes(X_test, verbose=1)
    mcc = matthews_corrcoef(y_test, predret_class)
    acc2 = accuracy_score(y_test, predret_class)

    print 'auc:', auc
    print 'mcc:', mcc
    print 'acc1:', acc1
    print 'acc2:', acc2

    return {'loss': -auc, 'status': STATUS_OK, 'model': model}


if __name__ == '__main__':
    best_run, best_model = optim.minimize(model=model,
                                          data=data,
                                          algo=tpe.suggest,
                                          max_evals=5,
                                          trials=Trials())
    X_train, y_train, X_test, y_test, X_valid, y_valid = data()
    print("Evalutation of best performing model:")
    print(best_run)
    fw = open(result_file_name, 'w')
    score, acc1 = best_model.evaluate(X_test, y_test, verbose=0)
    predret = best_model.predict(X_test, verbose=1)
    auc = roc_auc_score(y_test, predret)
    predret_class = best_model.predict_classes(X_test, verbose=1)
    mcc = matthews_corrcoef(y_test, predret_class)
    acc2 = accuracy_score(y_test, predret_class)

    fw.write('\t'.join(['acc1', 'auc', 'mcc', 'acc2']) +'\n')
    fw.write('\t'.join([str(acc1), str(auc), str(mcc), str(acc2)]) +'\n')
    fw.close();

    
    

################################################################################
# train_model  by Stella Gao
#
# Input
#  2 hdf5 files
#
# Output
#  model and error_rate
################################################################################

from __future__ import division
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

from sklearn.cross_validation import train_test_split


# loading train data

file_name = 'PLEK'

file = h5py.File(file_name+'_train_1hot.hdf5', 'r')
X_train = np.array(file['x_train']).astype('float32')
print X_train.shape
print X_train.dtype

Y_train = np.array(file['y_train']).astype('float32')
print Y_train.shape
print Y_train.dtype


file = h5py.File(file_name+'_test_1hot.hdf5', 'r')
X_test = np.array(file['x_test']).astype('float32')
print X_test.shape
print X_test.dtype

Y_test = np.array(file['y_test']).astype('float32')
print Y_test.shape
print Y_test.dtype


#x_train, x_valid, y_train, y_valid = train_test_split(X_train, Y_train, test_size=1/9, random_state=1)



print 'building model'
model = Sequential()
model.add(LSTM(128, input_shape=X_train.shape[1:])) #128
#model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1, activation = 'sigmoid'))
print(model.summary())

print 'compiling model'

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])


print 'fitting model'
model.fit(X_train, Y_train, batch_size=16, nb_epoch=50, validation_split = 0.111)


print 'evaluating model'

scores = model.evaluate(X_test, Y_test, verbose = 0)
#scores = model.evaluate(x_train, y_train, verbose = 0)

print("Accuracy: %.3f%%" % (scores[1]*100))


print 'making prediction'

# make predictions
trainPredict = model.predict(X_train)
print trainPredict.dtype
print trainPredict.shape
#print trainPredict
trainRounded = [round(x) for x in trainPredict]
#print(trainRounded)
count = 0
for i in xrange(1800):
    count += abs(trainRounded[i] - Y_train[i])

print("Train error rate is: %.3f%%" % ((count/1800)*100))

testPredict = model.predict(X_test)
print testPredict.dtype
print testPredict.shape
#print testPredict
testRounded = [round(x) for x in testPredict]
#print(testRounded)

cnt = 0
for i in xrange(200):
    cnt += abs(testRounded[i] - Y_test[i])


print("Test error rate is: %.3f%%" % ((cnt/200)*100))


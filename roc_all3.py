import numpy as np



from sklearn.metrics import roc_auc_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


import pandas
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sn_sp import * 
import plot
import matplotlib.pyplot as plt

             

false_positive_rate1 = [float(e) for e in open('cnn-fpr.txt', 'r').read().split()]
true_positive_rate1 = [float(e) for e in open('cnn-tpr.txt', 'r').read().split()]
    
false_positive_rate2 = [float(e) for e in open('rnn-fpr.txt', 'r').read().split()]
true_positive_rate2 = [float(e) for e in open('rnn-tpr.txt', 'r').read().split()]
    
false_positive_rate3 = [float(e) for e in open('crnn-fpr.txt', 'r').read().split()]
true_positive_rate3 = [float(e) for e in open('crnn-tpr.txt', 'r').read().split()]

fig = plt.figure()
#fig.savefig('temp.png', dpi=fig.dpi)
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate1, true_positive_rate1, 'b', label = 'CNN AUC = %0.3f' % 0.92742675)
plt.plot(false_positive_rate2, true_positive_rate2, 'g', label = 'RNN AUC = %0.3f' % 0.859113 )
plt.plot(false_positive_rate3, true_positive_rate3, 'm', label = 'CNN-RNN AUC = %0.3f' % 0.905026)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
#plt.show()
fig.savefig('roc.png', dpi=fig.dpi)

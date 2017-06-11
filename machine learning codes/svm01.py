from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

# create some V shaped data
np.random.seed(6)
X = np.random.randn(200, 2)
y = X[:, 1] > np.absolute(X[:, 0])
y = np.where(y, 1, -1)

# train a Support Vector Classifier using the rbf kernel
svm = SVC(kernel='rbf', random_state=0, gamma=0.5, C=10.0)
svm.fit(X, y)
plot_decision_regions(X, y, svm, markers=['o', 'x'], colors='blue,magenta')
plt.show()

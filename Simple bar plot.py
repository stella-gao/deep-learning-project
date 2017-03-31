# Simple bar plot

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 5
auc = [0.9257545, 0.926388, 0.926394, 0.9257545, 0.92748825]

mcc = [0.70817139822, 0.708514967537, 0.708514967537, 0.708514967537, 0.709363287028]

acc=[0.854, 0.85425, 0.8545, 0.854, 0.8545]

sn=[0.865, 0.8575, 0.849, 0.865, 0.8705]

sp=[0.843, 0.851, 0.86, 0.843, 0.8385]


## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.15                     # the width of the bars

## the bars
rects1 = ax.bar(ind, auc, width,
                color='red')

rects2 = ax.bar(ind+width, mcc, width,
                    color='orange')
rects3 = ax.bar(ind+2*width, acc, width,
                    color='blue')

rects4 = ax.bar(ind+3*width, sn, width,
                    color='green')
rects5 = ax.bar(ind+4*width, sp, width,
                    color='purple')
					

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,1)
ax.set_ylabel('Values')
ax.set_title('Times of test')
xTickMarks = ['Time'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('AUC', 'MCC', 'ACC', 'Sn', 'Sp') )

plt.savefig('times_value.png')


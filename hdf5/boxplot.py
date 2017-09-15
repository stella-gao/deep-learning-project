
## numpy is used for creating fake data
import numpy as np 
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 


fig = plt.figure()
ax = fig.add_subplot(111)

x54 = np.array([2,3,1,0])
x108 = np.array([2,3,1,0])
x162 = np.array([2,3,1,0])
x216 = np.array([2,3,1,0])

data_to_plot = [x54, x108, x162, x216]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

## Custom x-axis labels
ax.set_xticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])

## Remove top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()



# Create the boxplot
bp = ax.boxplot(data_to_plot)

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')

ax.boxplot([x1,x2,x3])
plt.show()
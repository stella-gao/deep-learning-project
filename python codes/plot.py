import matplotlib.pyplot as plt
import numpy as np

data = []
with open('python-fps-enroll.txt') as f:
    for line in f:
	      data.append(float(line))

#print(data)

plt.figure()
plt.hist(data, normed=True, bins=10)
plt.ylabel('Probability')
plt.savefig("py-enroll.png")

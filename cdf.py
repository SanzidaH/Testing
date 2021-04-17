import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import os

### Plot graph ###
numbers = [5,10,15,20,25]
#numbers = [5, 10]


for val in numbers:
 cnt = 0
 a = np.array([])
 fname = "app-delays-trace-cn" + str(val) + ".txt"
 path = os.path.join(os.path.expanduser('~'), 'ndnSIM', 'ns-3', fname)
 print(path)

 for line in open(path, 'r'):
  values = []
  values = [str(s) for s in line.split()]
  if cnt > 0:
   a = np.append (a, [round(float(values[5]),5)])
  cnt = cnt + 1

#1 
 x = np.sort(a)
 y = np.arange(len(x))/float(len(x))
#frequency
 unique_elements, counts_elements = np.unique(x, return_counts=True)
 print(len(x))
 print("Frequency of unique values of the said array:")
 print(np.asarray((unique_elements, counts_elements)))
 
 plt.xlabel('Delay')
 plt.ylabel('Probability (at or below delay)')
 plt.title('Empirical CDF of packet delay')
 
 #plt.plot(x, y, label = str(val))
 #plt.plot(np.sort(a), np.linspace(0, 100, len(a), endpoint=False), label = str(val))
#2
 X2 = np.sort(a)
 F2 = np.array(range(len(X2)))/float(len(X2))
 
 plt.plot(X2, F2, label = "Consumer: " + str(val))
 plt.legend(loc='best')

#3
#plt.plot(np.sort(a), np.linspace(0, 1, len(a), endpoint=False))

plt.savefig("new_cumulative_density_distribution_consumer.png", bbox_inches='tight')
fig = plt.gcf()
fig.set_size_inches((10, 3), forward=False)
#fig.savefig("new_cumulative_density_distribution_consumers"+str(val)+".png", bbox_inches='tight') #, dpi=500
plt.show()
plt.close()


     


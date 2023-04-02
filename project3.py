import matplotlib.pyplot as plt
import math
import numpy as np
import csv

days - [1,2,3,4,5]
sleeping - [7,8,6,11,7]
eating - [2,3,4,2,2]
working - [7,8,7,8,13]
playing - [8,5,7,8,13]
slices - [7,2,2,13]
activities - ['sleeping', 'eating', 'working', 'playing']
cols - ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()        
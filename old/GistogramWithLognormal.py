from scipy.stats import logistic, uniform, norm, pearsonr
from numpy import sqrt, pi, e
import numpy as np
import matplotlib.pyplot as plt
import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
import pylab
import random
import math
import numpy as np
from scipy.stats import shapiro
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
from collections import defaultdict


a = np.load('dspnorm.npy')
# a = a[:-27000]
# b = np.load('DPt.npy')
# #b = b[:-8500]
# c = np.concatenate((a, b), axis=0)
#
# print(len(a))
# print(len(b))
# print(len(c))
#
#
# np.save("DPall", c)

# x = random.uniform(1.0, 1.1)
# y = [i for i in a]
# yy = [i*x for i in y if i < 650/x]
# print(sum(yy)/len(yy))
# print(max(yy))
# print(min(yy))
#x = [i for i in range(0, len(c))]
#
#
#
# print(len(x))
# print(len(yy))
plt.hist(a, bins=80)
#plt.hist(yy, bins=100)
plt.minorticks_on()

plt.grid(which='minor',
         color = 'gray',
         linestyle = ':')
plt.ylabel('Пакеты', fontsize=8)
plt.xlabel('Размер пакетов, байт', fontsize=9)
# print('Sampling frequency is', frq)
plt.savefig('histogram.png', format='png')
plt.show()

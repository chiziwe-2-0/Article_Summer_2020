import matplotlib.pyplot as plt
import numpy as np
from numpy import mean

a, res, yn = [], [], []
summa = 0

diskret = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

a = np.load('array.npy')

n = 70
d = diskret(a, n) #разбиение массива a на n массивов

for i in d:
    for j in range(len(i)):
       res.append(np.var(i)) #дисперсия
       #res.append(mean(i)) #мо

for i in res:
    summa += i
    #считаем Y(n) по формуле Б.-Д.
    y = float((res.index(i)+1)/len(res)) * (1-((res.index(i)+1)/len(res)))*((1/(res.index(i)+1))*summa-(1/(len(res)-((res.index(i)+1))))*(sum(res)-summa))
    yn.append(y)




x = [i for i in range(0, len(yn))]

plt.plot(x, yn)
#plt.hist(res, bins=100)
plt.minorticks_on()

plt.grid(which='minor',
         color = 'gray',
         linestyle = ':')
plt.xlabel('Пакеты, n', fontsize=8)
#plt.ylabel('Размер пакетов, байт', fontsize=9)
# print('Sampling frequency is', frq)
plt.savefig('histogram.png', format='png')
plt.show()

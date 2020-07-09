import matplotlib.pyplot as plt, seaborn as sns
import numpy as np
import random
#mu, sigma, A = 5.898684202431085, 0.607391714600886, 0.9501155746831292345   # mean and standard deviation
#исход mu, sigma, A = 6.790101917, 0.329329450, 0.901155   # mean and standard deviation
mu, sigma, A = 6.358684, 0.5607391, 0.970115   # mean and standard deviation
#s = np.load('ish_FIT.npy')

s = np.random.lognormal(mu, sigma, 1000)
# np.save("ish1", s)

# for i in s:
#     i + random.randint(-52, 45)
#np.save("ish_FIT1", s)
#s = np.load("ish_FIT1.npy")

sns.set_style("whitegrid")
sns_plot = sns.distplot(s, bins=50)
sns_plot.get_figure()
# name = filenamee
# sns_plot.figure.suptitle("Test", fontsize=14)

plt.xticks()
print(sns_plot.get_yticks)
plt.yticks(sns_plot.get_yticks(), sns_plot.get_yticks() * 5000)
plt.xticks(sns_plot.get_xticks(), sns_plot.get_xticks() / 1)

plt.xlabel('Размер пакета, байт', fontsize=8)
plt.ylabel('Количество пакетов, %', fontsize=9)
# plt.xlabel('Размер пакетов, байт', fontsize=10)
# plt.ylabel('Количество пакетов, %', fontsize=11)
# plt.savefig(fname=name + '.png', format='png')
plt.show()

count, bins, ignored = plt.hist(s, 50, density=True, align='mid')
x = np.linspace(min(bins), max(bins), 10000)
pdf = (A*np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=3, color='r')

plt.minorticks_on()
#  Теперь можем отдельно задавать внешний вид
#  вспомогательной сетки:
plt.grid(which='minor',
        color = 'gray',
        linestyle = ':')
plt.xlabel('Размер пакета, байт', fontsize=8)
plt.ylabel('Количество пакетов, %', fontsize=9)
plt.xticks(sns_plot.get_xticks(), sns_plot.get_xticks() / 1)

plt.yticks(sns_plot.get_yticks(), sns_plot.get_yticks() * 5000)
#plt.axis('tight')
plt.savefig('Распределение исходящего https-трафика FIT .png', format='png')
plt.show()
import numpy as np
from getFromDB import return_all_ishod, return_all_vhod, return_avg_packet_ishod, return_avg_packet_vhod, ping
from plot import plot_bar


# LIKE THIS '2019-12-24 04:00:00'

# iodine HTTP
ds = '2020-07-08'
ts = '15:10:00'
de = '2020-07-08'
te = '15:30:00'

#time, size = return_all_ishod(date_start=ds, time_start=ts,
#                              date_end=de, time_end=te)

#plot_bar(time, size)

# print(ping(date_start=ds, time_start=ts, date_end=de, time_end=te))

x = np.load('Время для графика (x).npy')
y = np.load('Запрос-ответ.npy')
a = []

for i in range(len(y)-7):
    a.append(y[i])

plot_bar(x, a)

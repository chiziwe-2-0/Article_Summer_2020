import numpy as np
from modData import window_aggregation
from getFromDB import return_all_ishod, return_all_vhod, return_avg_packet_ishod, return_avg_packet_vhod, ping
import plot
import modData

# INPUT LIKE THIS '2019-12-24 04:00:00'

ds = '2020-07-16'
ts = '16:36:00'
de = '2020-07-16'
te = '16:48:00'

x, y = [], []
array = np.load('np_arrs/FTP/pure/ishod_ftp.txt.npy')
print(array)

for line in array:
 #    if line[1] < 1500:
        x.append(line[0])
        y.append(line[1])

avg = str((sum(y) / len(y)))

plot.plot_bar(x, y, name="Средний размер пакета = " + avg, filename="FTP_исходящий_no_tun", x_label="Время", y_label="Размер пакета, байт")

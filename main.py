import numpy as np
from modData import window_aggregation
from getFromDB import return_all_ishod, return_all_vhod, return_avg_packet_ishod, return_avg_packet_vhod, ping
import plot
import modData

# INPUT LIKE THIS '2019-12-24 04:00:00'

ds = '2020-07-17'
ts = '12:20:00'
de = '2020-07-17'
te = '12:32:00'

x, y = [], []
y = np.load('np_arrs/RDP/pure/response_time_rdp.txt.npy')

# for line in array:
#     #    if line[1] < 1500:
#     x.append(line[0])
#     y.append(line[1])

avg = str((sum(y) / len(y)))
print(y)

plot.plot_hist(y, name="Средний размер пакета = " + avg, filename="RDP_время_no_tun",
               x_label="Время, с",
               y_label="Количество")

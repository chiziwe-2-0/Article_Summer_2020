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
array = np.load('np_arrs/RDP/iodine/RDP_входящий(time+size)_iodine.npy')

for line in array:
    x.append(line[0])
    y.append(line[1])

avg = str((sum(y) / len(y)))

plot.plot_hist(y, name="Средний размер пакета = " + avg, filename="RDP_входящий_iodine_гистограмма",
               y_label="Количество",
               x_label="Размер пакета, байт")

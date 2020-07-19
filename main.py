import numpy as np
from modData import window_aggregation
from getFromDB import return_all_ishod, return_all_vhod, return_avg_packet_ishod, return_avg_packet_vhod, ping
import plot
import modData

# INPUT LIKE THIS '2019-12-24 04:00:00'

# iodine HTTP
# ds = '2020-07-16'
# ts = '16:36:00'
# de = '2020-07-16'
# te = '16:48:00'

ds = '2020-07-16'
ts = '16:36:00'
de = '2020-07-16'
te = '16:48:00'


# x = np.load('np_arrs/Время для графика (x).npy')
# y = np.load('np_arrs/Запрос-ответ.npy')
#

print(ping(date_start=ds, time_start=ts,
           date_end=de, time_end=te))

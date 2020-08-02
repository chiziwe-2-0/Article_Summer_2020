import numpy as np
from modData import window_aggregation
from getFromDB import return_all_ishod, return_all_vhod, return_avg_packet_ishod, return_avg_packet_vhod, ping
import plot
import modData

# INPUT LIKE THIS '2019-12-24 04:00:00'

ds = '2020-08-01'
ts = '00:45:00'
de = '2020-08-01'
te = '01:15:00'

# vhod, ishod, time = modData.vhod_ishod_ping_from_file("https.txt")

# array, qty = return_all_ishod(ds, ts, de, te)

# np.save("np_arrs/first/DNS/DNS_исходящий", array)

x, y = [], []
# array = np.load("np_arrs/first/DNS/DNS_запрос-ответ.npy")
array = ping(ds, ts, de, te)

for line in array:
    if line < 0.5:
        x.append(line)
#     y.append(line[1])

avg = str((sum(x) / len(x)))

plot.plot_hist(x, name="Среднее время = " + avg, filename="time_HTTPS_in_DNS",
               y_label="Количество",
               x_label="Время, с")

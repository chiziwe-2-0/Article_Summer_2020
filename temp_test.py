import numpy as np
# import datetime as DT
# ds = '2020-07-08'
# ts = '15:25:00'
# de = '2020-07-08'
# te = '15:55:00'
#
# dt_start = DT.datetime.fromisoformat(ds + ' ' + ts)
# dt_end = DT.datetime.fromisoformat(de + ' ' + te)
#
# dt_start_unix_MSK = dt_start.timestamp() + 10800
#
# print(dt_start_unix_MSK)


a = [x for x in range(10)]
np.save('np_arrs/ttt', a)
print(a)
import numpy as np
from getFromDB import return_all_vhod, return_all_ishod


# функция массив размеров пакетов с учетом окна агрегации
def window_aggregation(arr, window):
    size = []
    temp_size = 0
    i = 0
    end = float(arr[0][0]) + window

    while i < len(arr) - 1:
        if float(arr[i][0]) <= end:
            temp_size += int(arr[i][1])
            i += 1
        else:
            if temp_size != 0:
                size.append(temp_size)
            temp_size = 0
            end += window
    np.save("np_arrs/windows_aggr", size)
    return size

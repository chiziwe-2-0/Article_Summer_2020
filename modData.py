import numpy as np
from getFromDB import return_all_vhod, return_all_ishod


# на вход подается массив time + size (Finger Printing)
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


# на вход подается массив БД (time + srcip + srcport + dstip + dstport + size)
def vhod_ishod_ping_from_file(filename):
    vhod, ishod, temp_vhod, temp_ishod = [], [], [], []
    with open('arrs/' + filename) as f:
        myList = [line.replace('\n', '').split(",") for line in f]

    for i in range(len(myList)):
        # входящий
        if int(myList[i][2][1:-1]) == 22:
            if myList[i][3][1:-1] == "10.227.11.45":
                fp_vhod = [float(myList[i][0][1: -1]), float(myList[i][5][1: -1])]
                temp_vhod_once = [float(myList[i][0][1: -1]), myList[i][1][1: -1], myList[i][2][1: -1], myList[i][3][1: -1], myList[i][4][1: -1]]
                temp_vhod.append(temp_vhod_once)
                vhod.append(fp_vhod)

        # исходящий
        if int(myList[i][4][1:-1]) == 22:
            if myList[i][1][1:-1] == '10.227.11.45':
                fp_ishod = [float(myList[i][0][1: -1]), float(myList[i][5][1: -1])]
                temp_ishod_once = [float(myList[i][0][1: -1]), myList[i][1][1: -1], myList[i][2][1: -1], myList[i][3][1: -1], myList[i][4][1: -1]]
                temp_ishod.append(temp_ishod_once)
                ishod.append(fp_ishod)

    # запрос-ответ
    delta = 3
    answer, response_time_arr = [], []

    for i in range(len(temp_ishod)):
        out_time = float(temp_ishod[i][0])
        sip = str(temp_ishod[i][1])
        sport = str(temp_ishod[i][2])

        in_time = out_time + delta

        for j in range(len(temp_vhod)):
            if sip == temp_vhod[j][3]:
                if sport == temp_vhod[j][4]:
                    if out_time < temp_vhod[j][0] < in_time:
                        answer.append(temp_vhod[j][0])

        try:
            response_time = float(answer[0]) - out_time
        except IndexError:
            pass

        response_time_arr.append(response_time)

        answer.clear()

    np.save("np_arrs/vhod_" + filename, vhod)
    np.save("np_arrs/ishod_" + filename, ishod)
    np.save("np_arrs/response_time_" + filename, response_time_arr)

    return vhod, ishod, response_time_arr

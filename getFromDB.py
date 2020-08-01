import datetime as DT
from db import Db
import numpy as np
import progressbar
import time

h = "192.168.132.250"
u = "vsu"
p = "2020"
db = "traffcoll"
# db = "traffcoll_upto20200720"

BD = Db(host=h, user=u, password=p, db=db)


# функция возвращает весь исходящий трафик
def return_all_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 0
    dt_end_unix_MSK = dt_end.timestamp() + 0

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53');")

    quantity = BD.query(sql="SELECT count(*) FROM netsessions " +
                            "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                            str(
                                dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53');")

    # np.save("np_arrs/RDP_исходящий(time+size)_iodine", packs)

    return packs, quantity


# функция возвращает весь входящий трафик
def return_all_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 0
    dt_end_unix_MSK = dt_end.timestamp() + 0

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND dstip like '10.227.11.%' AND srcport='53');")

    quantity = BD.query(sql="SELECT count(*) FROM netsessions " +
                            "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                            str(dt_end_unix_MSK) + " AND dstip like '10.227.11.%' AND srcport='53');")

    # np.save("np_arrs/RDP_входящий(time+size)_iodine", packs)

    return packs, quantity


# функция возвращает средний размер пакета исходящего трафика
def return_avg_packet_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 0
    dt_end_unix_MSK = dt_end.timestamp() + 0

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53');")
    return packs


# функция возвращает средний размер пакета входящего трафика
def return_avg_packet_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 0
    dt_end_unix_MSK = dt_end.timestamp() + 0

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND dstip like '10.227.11.%' AND srcport='53');")
    return packs


# функция возвращает время "запрос-ответ" всего трафика
def ping(date_start, time_start, date_end, time_end):
    count = 0

    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 0
    dt_end_unix_MSK = dt_end.timestamp() + 0

    # исходящий
    packs = BD.query(sql="SELECT * FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")

    print(len(packs))
    np.save("np_arrs/Исходящий_ping", packs)
    arr_packs = np.load("np_arrs/Исходящий_ping.npy")

    delta = 3
    response_time_arr, time_x_arr = [], []

    for i in range(len(arr_packs) - 1):
        out_time = float(arr_packs[i][1])
        sip = str(arr_packs[i][2])
        sport = str(arr_packs[i][3])

        in_time = out_time + delta

        answer = BD.query(sql="SELECT * FROM netsessions " +
                              "WHERE (frametime >= " + str(out_time) + " AND frametime <= " +
                              str(in_time) + " AND dstip = '" + str(sip.replace(' ', '')) + "' AND dstport= '" +
                              str(sport.replace(' ', '')) + "') ORDER BY frametime;")

        try:
            response_time = float(answer[0][1]) - out_time

            if i % 1000 == 0:
                print(count, response_time)
                count += 1

        except IndexError:
            pass
        except TypeError:
            pass

        try:
            time_x_arr.append(float(answer[0][1]))
        except IndexError:
            pass

        response_time_arr.append(response_time)

    np.save("np_arrs/first/DNS/DNS_запрос-ответ", response_time_arr)
    np.save("np_arrs/first/DNS/DNS_абсциссы_для_запрос_ответ", time_x_arr)

    return response_time_arr

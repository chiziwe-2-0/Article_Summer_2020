import datetime as DT
from db import Db
import numpy as np

h = "192.168.132.250"
u = "vsu"
p = "2020"
db = "traffcoll"

BD = Db(host=h, user=u, password=p, db=db)


# функция возвращает весь исходящий трафик
def return_all_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 10800
    dt_end_unix_MSK = dt_end.timestamp() + 10800

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53');")

    quantity = BD.query(sql="SELECT count(*) FROM netsessions " +
                            "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                            str(
                                dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53');")

    np.save("np_arrs/Исходящий", packs)

    return packs, quantity


# функция возвращает весь входящий трафик
def return_all_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 10800
    dt_end_unix_MSK = dt_end.timestamp() + 10800

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND dstip like '10.227.11.%' AND srcport='53');")

    quantity = BD.query(sql="SELECT count(*) FROM netsessions " +
                            "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                            str(dt_end_unix_MSK) + " AND dstip like '10.227.11.%' AND srcport='53');")

    np.save("np_arrs/Входящий", packs)

    return packs, quantity


# функция возвращает средний размер пакета исходящего трафика
def return_avg_packet_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 10800
    dt_end_unix_MSK = dt_end.timestamp() + 10800

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53');")
    return packs


# функция возвращает средний размер пакета входящего трафика
def return_avg_packet_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 10800
    dt_end_unix_MSK = dt_end.timestamp() + 10800

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND dstip like '10.227.11.%' AND srcport='53');")
    return packs


# функция возвращает время "запрос-ответ" всего трафика
def ping(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    dt_start_unix_MSK = dt_start.timestamp() + 10800
    dt_end_unix_MSK = dt_end.timestamp() + 10800

    packs = BD.query(sql="SELECT * FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start_unix_MSK) + " AND frametime <= " +
                         str(dt_end_unix_MSK) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")

    np.save("np_arrs/Входящий_ping", packs)
    # np.save("np_arrs/Входящий (%s %s - %s %s)" % (date_start, time_start, date_end, time_end), packs)

    arr_packs = np.load("np_arrs/Входящий_ping.npy")

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
        except IndexError:
            pass

        try:
            time_x_arr.append(float(answer[0][1]))
        except IndexError:
            pass

        response_time_arr.append(response_time)

    np.save("np_arrs/Запрос-ответ", response_time_arr)
    np.save("np_arrs/Время для графика (x)", time_x_arr)

    return response_time_arr

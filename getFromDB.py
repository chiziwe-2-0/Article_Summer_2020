import datetime as DT
from db import Db
import numpy as np

h = "192.168.132.250"
u = "vsu"
p = "2020"
db = "traffcoll"

BD = Db(host=h, user=u, password=p, db=db)


def return_all_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                         str(
                             dt_end.timestamp() + 10800) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")

    quantity = BD.query(sql="SELECT count(*) FROM netsessions " +
                            "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                            str(
                                dt_end.timestamp() + 10800) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")

    np.save('Исходящий (' + date_start + ' ' + time_start + '; ' + date_end + ' ' + time_end + ')', packs)


def return_all_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                         str(
                             dt_end.timestamp() + 10800) + " AND dstip like '10.227.11.%' AND srcport='53') ORDER BY frametime;")

    quantity = BD.query(sql="SELECT count(*) FROM netsessions " +
                            "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                            str(
                                dt_end.timestamp() + 10800) + " AND dstip like '10.227.11.%' AND srcport='53') ORDER BY frametime;")

    # time, size = [], []
    # for i in range(len(packs)):
    #     time.append(packs[i][0])
    #     size.append(packs[i][1])
    #
    # return time, size

    np.save('Входящий (' + date_start + ' ' + time_start + '; ' + date_end + ' ' + time_end + ')', packs)


def return_avg_packet_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                         str(dt_end.timestamp() + 10800) + " AND srcip like '10.227.11.%' AND dstport='53');")
    return packs


def return_avg_packet_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                         str(dt_end.timestamp() + 10800) + " AND dstip like '10.227.11.%' AND srcport='53');")
    return packs


def ping(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT * FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp() + 10800) + " AND frametime <= " +
                         str(
                             dt_end.timestamp() + 10800) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")

    # np.save('Исходящий (для поиска времени "запрос-ответ")', packs)

    delta = 3
    response_time_arr = []

    for i in range(len(packs)):
        out_time = float(packs[i][1])
        sip = str(packs[i][2])
        sport = str(packs[i][3])

        in_time = out_time + delta

        answer = BD.query(sql="SELECT * FROM netsessions " +
                              "WHERE (frametime >= " + str(out_time) + " AND frametime <= " +
                              str(
                                  in_time) + " AND dstip = '" + str(sip.replace(' ', '')) + "' AND dstport= '" + str(
            sport.replace(' ', '')) + "') ORDER BY frametime;")

        response_time = float(answer[0][1]) - out_time
        response_time_arr.append(response_time)

    return response_time_arr

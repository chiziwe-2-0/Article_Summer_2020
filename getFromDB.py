import datetime as DT
from db import Db

h = "192.168.132.250"
u = "vsu"
p = "2020"
db = "traffcoll"

BD = Db(host=h, user=u, password=p, db=db)


# LIKE THIS '2019-12-24 04:00:00'
def return_all_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(
                             dt_end.timestamp()) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")
    time, size = [], []
    for i in range(len(packs)):
        time.append(packs[i][0])
        size.append(packs[i][1])

    return time, size


def return_all_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT frametime, size FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(
                             dt_end.timestamp()) + " AND dstip like '10.227.11.%' AND srcport='53') ORDER BY frametime;")

    time, size = [], []
    for i in range(len(packs)):
        time.append(packs[i][0])
        size.append(packs[i][1])

    return time, size


def return_avg_packet_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         " WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(dt_end.timestamp()) + " AND srcip like '10.227.11.%' AND dstport='53');")
    return packs


def return_avg_packet_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         " WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(dt_end.timestamp()) + " AND dstip like '10.227.11.%' AND srcport='53');")
    return packs

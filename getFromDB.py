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
                         "WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(dt_end.timestamp()) + " AND srcip like '10.227.11.%' AND dstport='53');")
    return packs


def return_avg_packet_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT avg(size) AS avgfs FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(dt_end.timestamp()) + " AND dstip like '10.227.11.%' AND srcport='53');")
    return packs


def ping(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = BD.query(sql="SELECT frametime, size, dstip, dstport, srcip, srcport FROM netsessions " +
                         "WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= " +
                         str(dt_end.timestamp()) + " AND (srcip LIKE '10.227.11.%' OR dstip LIKE '10.227.11.%') " +
                         "AND (dstport='53' OR srcport='53')) ORDER BY frametime;")

    time, size, dstip, dstport, srcip, srcport = [], [], [], [], [], []
    for i in range(len(packs)):
        dip = packs[i][2]
        dport = packs[i][3]
        while



        time.append(packs[i][0])
        size.append(packs[i][1])
        dstip.append(packs[i][2])
        dstport.append(packs[i][3])
        srcip.append(packs[i][4])
        srcport.append(packs[i][5])

        all = np.concatenate([time, size, dstip, dstport, srcip, srcport])

#    for i in range(len(time)):

    return all #, size, dstip, dstport, srcip, srcport

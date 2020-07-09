import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
import numpy as np
import decimal
import datetime as DT
from db import Db

h = "192.168.132.250"
u = "vsu"
p = "2020"
db = "traffcoll"

bd = Db(host=h, user=u, password=p, db=db)


# LIKE THIS '2019-12-24 04:00:00'
def return_all_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = bd.query(sql="SELECT frametime, size FROM netsessions"
                              + " WHERE (frametime >= " + str(dt_start.timestamp()) + " AND frametime <= "
                              + str(dt_end.timestamp()) + " AND srcip like '10.227.11.%' AND dstport='53') ORDER BY frametime;")
    return packs


def return_all_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = get_info(db, u, p, h, port,
                     sql_entry="SELECT frametime, size FROM netsessions" +
                               "WHERE (frametime >= " + dt_start.timestamp() + " AND frametime <= " + dt_end.timestamp() +
                               "AND dstip like '10.227.11.%' AND srcport='53') ORDER BY frametime;").split()
    return packs


def return_avg_packet_ishod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = get_info(db, u, p, h, port,
                     sql_entry="SELECT avg(size) AS avgfs FROM netsessions" +
                               "WHERE (frametime >= " + dt_start.timestamp() + " AND frametime <= " + dt_end.timestamp() +
                               "AND srcip like '10.227.11.%' AND dstport='53');").split()
    return packs


def return_avg_packet_vhod(date_start, time_start, date_end, time_end):
    dt_start = DT.datetime.fromisoformat(date_start + ' ' + time_start)
    dt_end = DT.datetime.fromisoformat(date_end + ' ' + time_end)

    packs = get_info(db, u, p, h, port,
                     sql_entry="SELECT avg(size) AS avgfs FROM netsessions" +
                               "WHERE (frametime >= " + dt_start.timestamp() + " AND frametime <= " + dt_end.timestamp() +
                               "AND dstip like '10.227.11.%' AND srcport='53');").split()
    return packs


ds = '2020-07-08'
ts = '15:25:00'

de = '2020-07-08'
te = '15:55:00'

a = return_all_ishod(date_start=ds, time_start=ts,
                     date_end=de, time_end=te)

print(a)

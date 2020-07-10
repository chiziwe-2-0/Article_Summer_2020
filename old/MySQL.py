import numpy as np


def mysql(direction):
    import pymysql
    import pandas as pd
    from sshtunnel import SSHTunnelForwarder
    from os.path import expanduser

    sql_hostname = 'localhost'
    sql_username = 'root'
    sql_password = ''
    sql_main_database = 'perl'
    sql_port = 3306
    ssh_host = '10.36.65.1'
    ssh_user = 'DPOLL_NOlimpiev'
    ssh_password = 'K@f92AsR'
    ssh_port = 22
    sql_ip = '127.0.0.1'

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                               passwd=sql_password, db=sql_main_database,
                               port=tunnel.local_bind_port)
        query = '''SELECT VERSION();'''
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM traffic WHERE " + direction + "_port = '443';")
        arr = np.array(cursor.fetchall())
        cursor.close()
        data = pd.read_sql_query(query, conn)
        conn.close()
    return arr


def mezhpacket_int(arr):
    plotarr = []
    for i in range(arr.shape[0] - 1):
        if float(arr[i + 1][0]) - float(arr[i][0]) < 1:
            if arr[i][2] == arr[i + 1][4]:
                plotarr.append(float(arr[i + 1][0]) - float(arr[i][0]))
            elif arr[i][4] == arr[i + 1][2]:
                plotarr.append(float(arr[i + 1][0]) - float(arr[i][0]))
    np.save("SP_notunMySQL", plotarr)
    return plotarr


def packs_agrwindow(arr, window):
    size = []
    temp_size = 0
    i = 0
    end = float(arr[0][0]) + window

    while i < arr.shape[0] - 1:
        if float(arr[i][0]) <= end:
            temp_size += int(arr[i][1])
            i += 1
        else:
            if temp_size != 0:
                size.append(temp_size)
            temp_size = 0
            end += window
    np.save("DP_1", size)
    return size


def hrm_realtime(array):
    import matplotlib.pyplot as plt
    frq = 100
    plt.hist(array, bins=frq)
    print('Sampling frequency is', frq)
    plt.savefig('histogram.png', format='png')
    plt.show()


# np.save('SRC', mysql('src'))
# np.save('DST', mysql('dst'))

# print(np.load("SP_notunMySQL.npy"))

np.save('DST_1', packs_agrwindow(np.load("dst.npy"), 1))
# arr = np.load('dst.npy')

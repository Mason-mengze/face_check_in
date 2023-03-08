import sqlite3
from time import localtime,strftime
import zlib
# import os
# from skimage import io as iio
import io
import numpy as np  # 数据处理的库numpy


def getDateAndTime():
    dateandtime = strftime("%Y-%m-%d %H:%M:%S",localtime())
    return "["+dateandtime+"]"


#数据库部分
#初始化数据库
def initDatabase():
    conn = sqlite3.connect("inspurer.db")  #建立数据库连接
    cur = conn.cursor()             #得到游标对象
    cur.execute('''create table if not exists worker_info
    (name text not null,
    id int not null primary key,
    face_feature array not null)''')
    cur.execute('''create table if not exists logcat
     (datetime text not null,
     id int not null,
     name text not null,
     late text not null)''')
    cur.close()
    conn.commit()
    conn.close()


def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    dataa = out.read()
    # 压缩数据流
    return sqlite3.Binary(zlib.compress(dataa, zlib.Z_BEST_COMPRESSION))


def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    dataa = out.read()
    # 解压缩数据流
    out = io.BytesIO(zlib.decompress(dataa))
    return np.load(out)


def insertARow(Row,type):
    conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
    cur = conn.cursor()  # 得到游标对象
    if type == 1:
        cur.execute("insert into worker_info (id,name,face_feature) values(?,?,?)",
                (Row[0],Row[1],adapt_array(Row[2])))
        print("写人脸数据成功")
    if type == 2:
        cur.execute("insert into logcat (id,name,datetime,late) values(?,?,?,?)",
                    (Row[0],Row[1],Row[2],Row[3]))
        print("写日志成功")
        pass
    cur.close()
    conn.commit()
    conn.close()
    pass


def loadDataBase(type):
    # type 1 注册 2打卡
    conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
    cur = conn.cursor()  # 得到游标对象
    if type == 1:
        knew_id = []
        knew_name = []
        knew_face_feature = []
        cur.execute('select id,name,face_feature from worker_info')
        origin = cur.fetchall()
        for row in origin:
            # print(row[0])
            knew_id.append(row[0])
            # print(row[1])
            knew_name.append(row[1])
            # print(convert_array(row[2]))
            knew_face_feature.append(convert_array(row[2]))
        return [knew_id, knew_name, knew_face_feature]
    if type == 2:
        logcat_id = []
        logcat_name = []
        logcat_datetime = []
        logcat_late = []
        cur.execute('select id,name,datetime,late from logcat')
        origin = cur.fetchall()
        for row in origin:
            # print(row[0])
            logcat_id.append(row[0])
            # print(row[1])
            logcat_name.append(row[1])
            # print(row[2])
            logcat_datetime.append(row[2])
            # print(row[3])
            logcat_late.append(row[3])
        return [logcat_id, logcat_name, logcat_datetime, logcat_late, origin]
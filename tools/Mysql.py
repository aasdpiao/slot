import marshal
import MySQLdb as mdb

conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456')
conn.autocommit(0)

cursor = conn.cursor()

def ConnectDB():
    try:
        DB_NAME = 'SlotGame'
        cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
        conn.select_db(DB_NAME)

        TABLE_NAME = 'SlotRun'
        cursor.execute('CREATE TABLE IF NOT EXISTS %s(checkerboard blob not null,boardlines blob not null,linestr text,id INT(20) not null AUTO_INCREMENT,primary key (id))'%TABLE_NAME)
    except:
        import traceback
        traceback.print_exc()
        conn.rollback()

def SaveRecord(checkerboard,lines,linestr):
    try:
        sql = 'INSERT INTO SlotRun(checkerboard,boardlines,linestr) values("%s","%s","%s")' %(marshal.dumps(checkerboard),marshal.dumps(lines),linestr)
        cursor.execute(sql)
    except:
        import traceback
        traceback.print_exc()
        conn.rollback()

def DisconnectDB():
    conn.commit()
    cursor.close()
    conn.close()
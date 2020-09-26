import MySQLdb

def conn_f():
    con = MySQLdb.connect(
        user = 'root',
        passwd = 'siragami',
        host = 'localhost',
        db = "todo_app",
        charset = 'utf8'
    )
    return con

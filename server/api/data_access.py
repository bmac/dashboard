import pickle
import sqlite3

from config import DB_PATH

print DB_PATH

def execute(query):
        dbPath = DB_PATH
        connection = sqlite3.connect(dbPath)
        cursorobj = connection.cursor()
        try:
                cursorobj.execute(query)
                result = cursorobj.fetchall()
                connection.commit()
        except Exception:
                raise
        connection.close()
        return result


def query(table, query=None, columns="*"):
        q = "select %s from %s" % (columns, table)
        if query:
                q += " where %s" % query
        q += ";"
        return execute(q)


def set_up():
        execute("create table users(id integer primary key not null, " + \
                        "name varchar(20) unique not null, " + \
                        "api_key varchar unique);")
        execute("create table graphs(id int primary key, " + \
                        "created datetime default current_timestamp," + \
                        "name varchar(20), " + \
                        "user_id references users(id) not null, " + \
                        "color blob, " + \
                        "lambda blob);")
        execute("create table events(id int primary key, " + \
                        "graph_id references graphs(id) not null, " + \
                        "date datetime not null, " + \
                        "data blob);")
        init_data()


def init_data():
        execute("insert into users('name') values('ingrid');")
        execute("insert into users('name') values('bmac');")
        execute("insert into graphs('name', 'user_id') values ('foo', 1);")
        execute("insert into graphs('name', 'user_id') values ('exercise', 2);")
        execute("insert into events('graph_id', 'date') values (1, '2007-01-01 10:00:00');")
        execute("insert into events('graph_id', 'date') values (2, '2007-01-01 10:00:00');")


def tear_down():
        try:
                execute("drop table users;")
        except:
                pass
        try:
                execute("drop table graphs;")
        except:
                pass
        try:
                execute("drop table events;")
        except:
                pass

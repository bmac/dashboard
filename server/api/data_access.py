import pickle
import sqlite3

from config import DB_PATH


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


def format_list(list, keys):
    cleaned = []
    for i in range(len(list)):
        d = {}
        for k in keys:
            d[k] = list[i]
        list.append(d)


def format(list, keys=None):
    pass

def graph(id=None, user_id=None, name=None):
    if id:
        q = 'id=' + str(id)
    elif user_id and name:
        q = 'user_id=' + str(user_id) + "and name='" + name
    else:
        # Raise error.
        pass
    results = query('graphs', query=q)
    graph = format_list(results, ['id', 'created', 'name', 'user_id', 'color'])


def query(table, query=None, columns="*"):
    q = "select %s from %s" % (columns, table)
    if query:
        q += " where %s" % query
    q += ";"
    return execute(q)


def set_up():
        execute("create table users(id integer primary key not null, " + \
                        "name varchar(20) unique not null, " + \
                        "grapha references graphs(id), " + \
                        "api_key varchar unique);")
        execute("create table graphs(id integer primary key not null, " + \
                        "created datetime default current_timestamp," + \
                        "name varchar(20), " + \
                        "user_id references users(id) not null, " + \
                        "color blob, " + \
                        "lambda blob);")
        execute("create table events(id integer primary key not null, " + \
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
        execute("insert into events('graph_id', 'date', 'data') values (2, '2013-06-01 10:00:00', 5);")
        execute("insert into events('graph_id', 'date', 'data') values (2, '2013-06-02 10:00:00', 5);")
        execute("update users set grapha='exercise' where id=2;")


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

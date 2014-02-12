from data_access import execute


def create(name, user_id):
    user = execute("insert into graphs('name', 'user_id') values('%s', '%s');" \
                       % name, user_id)[0][0]
    return user


def read(user, name):
    try:
        user_id = execute("select id from users where name='" + user + "';")[0][0]
    except:
        # User doesn't exist.
        pass
    try:
        graph = execute("select * from graphs where user_id=" + str(user_id) + \
                      " and name='" + name + "';")[0]
    except:
        # User has no graph of that name
        pass

    graph_id = graph[3]

    try:
        events = execute("select * from events where graph_id=" + str(graph_id) + ";")
    except:
        pass
    dict = {}
    dict['start_date'] = events[0][1]
    dict['events'] = events

    return events

def save(graph):
    pass

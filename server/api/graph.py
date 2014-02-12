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

    graph_id = graph[0]

    try:
        events = execute("select * from events where graph_id=" + str(graph_id) + ";")
    except:
        pass

    # Format events
    cleaned_events = {}
    for e in events:
        cleaned_events[e[2]] = e[3]


    dict = {}
    dict['id'] = graph_id
    dict['name'] = name
    dict['data'] = cleaned_events

    return dict

def save(graph):
    pass

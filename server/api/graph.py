from data_access import execute


def create(name):
    # Check name availibility.
    user = execute("select id from users where name=%s" % name)
    if user:
        # Raise error, name not available.
        pass
    else:
        user = execute("insert into users('name') values('%s');" \
                           % name)[0][0]
        return user;


def save(graph):
    pass

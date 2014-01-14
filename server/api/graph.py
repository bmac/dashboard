from data_access import execute


def create(name, user_id):
    user = execute("insert into graphs('name', 'user_id') values('%s', '%s');" \
                       % name, user_id)[0][0]
        return user;


def save(graph):
    pass

from data_access import execute

"""
def create(name, user_id):
    user = execute("insert into graphs('name', 'user_id') values('%s', '%s');" \
                       % name, user_id)[0][0]
    return user
"""

def read(user):
    try:
        user = execute("select * from users where name='" + user + "';")[0]
    except:
        # User doesn't exist.
        pass
    dict = {}
    dict['id'] = user[0]
    dict['name'] = user[1]
    dict['graphs'] = [user[2], user[3]]

    return dict

def save(graph):
    pass

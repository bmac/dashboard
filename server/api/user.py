import base64
import hashlib
import random

from data_access import execute


def generate_api_key(user_id):
    # Check if user already has an api_key.
    api_key = execute("select api_key from users where id=%i" \
                % user_id)[0][0]

    if api_key:
        # return existing api_key.
        return api_key
    # User does not already ahve an api key.
    api_key = base64.b64encode(hashlib.sha256( str(random.getrandbits(256)) ).digest(), random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])).rstrip('==')
    q = "update users set api_key='%s' where id=%i;" \
                % (api_key, user_id)
    print q
    execute(q);

    return api_key


def validate_api_key(key):
    user = execute("select id from users where api_key='%s';" \
                       % key)
    if user:
        return user
    else:
        # Probs raise an error here.
        return None


def user(user_id=None, name=None):
    if user_id:
        pass
    elif name:
        pass
    else:
        # Raise error
        pass

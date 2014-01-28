import tornado
import tornado.web
import json

from api.user import validate_api_key
from api import graph


class DBHandler(tornado.web.RequestHandler):
    def prepare(self):
        #action = self.request.path.split('/')[-1]
        api_key = self.get_argument('user', '')
        if not api_key:
            # Throw error.
            pass
        user = validate_api_key(api_key)
        if not user:
            # Throw error.
            pass


class ProfileHandler(DBHandler):
    def get(self, user):
        self.write(json.dumps("USER ACTION"))


class UserHandler(DBHandler):
    def get(self, user, action):
        self.write(json.dumps(graph.read(user, action)))

class GraphHandler(DBHandler):
    def get(self, user):
        print user
        self.write(json.dumps("Graph"))
    def post(self):
        pass

class GitHubHandler(DBHandler):
    def get(self):
        self.write(json.dumps("Github"))


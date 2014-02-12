import tornado
import tornado.web
from tornado import template
import json

from api.user import validate_api_key
from api import graph, profile

loader = template.Loader("./templates/")

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

class DataHandler(DBHandler):
    def get(self, user):
        self.write(json.dumps(profile.read(user)))


class DashHandler(DBHandler):
    def get(self, user):
        self.render('templates/profile.html', user=user)


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


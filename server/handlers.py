import tornado
import tornado.web
from tornado import template
import json
from requests import get

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
    def get(self, user):
        response = get("https://github.com/users/" + user + "/contributions_calendar_data")
        # if reponse.status_code == 200:
        data = {}
        def scrub(x):
            date = x[0]
            date = date.replace('/', '-')
            data[date] = x[1]
        map(scrub, response.json())
        d = {
            "id" : "gh",
            "name" : "github",
            "data" : data
        }
        self.write(json.dumps(d))

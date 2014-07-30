import jinja2
import logging
import webapp2
import os

from google.appengine.api import memcache
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname('templates/')))

class Home(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('home.html')
    self.response.out.write(template.render())

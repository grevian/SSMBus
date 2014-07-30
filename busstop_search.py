import json
import logging
import webapp2
import os

from google.appengine.api import memcache
from google.appengine.api import users

class ById(webapp2.RequestHandler):
  def get(self, id):
    logging.debug("Finding stop by id %r" % id)
    results = find_by_id(id)
    self.response.out.write(json.dumps(results))

class Nearest(webapp2.RequestHandler):
  def get(self):
    try:
      logging.debug("Attempting to look up nearest stop...")
      logging.debug("Position is [%r]" % self.request.get('position'))
      position = json.loads(self.request.get('position'))
      logging.debug("Finding stop by position %r" % position)
    except:
       self.abort(400)
    
    results = get_nearest_to_position(position)
    self.response.out.write(json.dumps(results))

def find_by_id(id):
  pass

def get_nearest_to_position(position):
  # Do spacial query to get id    
  logging.debug("spacial query for position %r" % position)
  id = query_position_for_id(position.get('longitude'), position.get('latitude'))
  return find_by_id(id)

def query_position_for_id(longitude, latitude):
  pass

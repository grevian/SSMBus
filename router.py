import webapp2

from index import Home
import busstop_search as search

APP = webapp2.WSGIApplication([
  (r'/', Home),
  (r'/find/nearest', search.Nearest),
  (r'/find/(\d+)', search.ById)
], debug=True)
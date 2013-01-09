from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import urllib2

# Retrieve the targetURL and return OK if targetString is found.
targetUrl = "https://developer.apple.com/wwdc/"
targetString = "Apple Worldwide Developers Conference 2011"

class MainPage(webapp.RequestHandler):
   def get(self):
      status = "OK"
      time = 0

      try:
         fp = urllib2.urlopen(targetUrl)
         data = fp.read()
         fp.close()
         if not (targetString in data):
            status = "BAD"
      except:
         pass
         
      self.response.headers['Content-Type'] = 'text/xml'
      msg = "<pingdom_http_custom_check><status>%s</status><response_time>%0.3f</response_time></pingdom_http_custom_check>" % (status, time)
      self.response.out.write(msg)

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
   main()
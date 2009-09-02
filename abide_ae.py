#import random

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#from haiku import HAIKUS, FIVES, SEVENS
#from quotes import QUOTES



class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('The Dude Abides')

class Haiku(webapp.RequestHandler):
    def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      try:
        self.response.out.write( HAIKUS[random.randint(0,len(HAIKUS))])
      except IndexError:
        self.response.out.write("[THIS AGGRESSION WILL NOT STAND]")

class Quote(webapp.RequestHandler):
    def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      try:
        self.response.out.write( QUOTES[random.randint(0,len(QUOTES))])
      except IndexError:
        self.response.out.write("[I AM THE WALRUS?]")


application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     #('/haiku', Haiku),
                                     #('/quote', Quote)],
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()

import random
from itty import *
from haiku import HAIKUS, FIVES, SEVENS
from quotes import QUOTES

@get('/')
def index(request):
    return 'The Dude Abides'


@get('/haiku')
def haiku(request):
    try:
        return HAIKUS[random.randint(0,len(HAIKUS))]
    except IndexError:
        return "[THIS AGGRESSION WILL NOT STAND]"
    

@get('/quote')
def quote(request):
    try:
        return QUOTES[random.randint(0,len(QUOTES))]
    except:
        return "[I AM THE WALRUS?]"

run_itty()

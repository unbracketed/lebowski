import random
from itty import *
from haiku import HAIKUS, FIVES, SEVENS


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
    return 'Hello World!'

run_itty()

"""Collections of 5 and 7 syllable phrases from "The Big Lebowski"

"""

FIVES = [s.strip() for s in open('phrases_5.txt').readlines()]
SEVENS = [s.strip() for s in open('phrases_7.txt').readlines()]


def parsem():
    out = ''
    for line in open('haikus.txt').readlines():
        if len(line.strip()):
            out += "<p>%s</p>" % (line.strip())
        else:
            yield out
            out = ''
    

HAIKUS = [haiku for haiku in parsem()]
'HTML snippets of selected quotes from "The Big Lebowski"'

QUOTES = []
f = open('quotes.txt')
for line in f.readlines():
    if not line.startswith('['):
        QUOTES.append(line.strip())




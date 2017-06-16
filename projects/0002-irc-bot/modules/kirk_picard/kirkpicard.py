import sopel.module
import random
import os

@sopel.module.commands('kirk','picard')
def helloworld(bot, trigger):
    jokes = []
    with open ('/home/dotpy/.sopel/modules/kirkpicard.txt') as file:
        for line in file:
            jokes.append(line)
    bot.say('.beefact ' + jokes[random.randint(0,len(jokes)-1)])

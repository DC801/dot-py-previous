import sopel.module
from sopel.module import commands, rule
import random
import os

@commands('joke')
def joke(bot, trigger):
        bot.say('KNOCK KNOCK.')
        @rule('foobar')
        def respond(bot, trigger):
            bot.say('baz')

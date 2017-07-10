import sopel.module
import random
import os
import re
import random

@sopel.module.rule(r'\bh[ea]lp\b')
def halp(bot, trigger):
    bot.say('marvthegreat! marvthegreat! {} needs an adult!'.format(trigger.nick))

@sopel.module.commands('roll')
def observer(bot, trigger):
    # 1d4
    # 1d20
    # 1d100
    # 2d4
    # 2d20
    # 2d100
    # 10d4
    # 10d20
    # 10d100
    # 100d4
    # 100d20
    # 100d100
    # the first number could theoretically go to infinity, but the second number would probably better be limited in tabletop rpg context. the limit could be higher than 100 though, according to DM design.
    # IT SEEMS that trigger.group(2) and trigger.group(3) contain equivalent values. Why? And why go with trigger.group(3) for the below operations?
    foo = trigger.group(3)
    bar = re.match('^([1-9]+[\d]{0,}|[1-9]+[\d]{0,}d[1-9]+[\d]{0,})$', foo)

    if (not bar):
        coinflip = random.randint(0,1)
        if (coinflip == 0):
            bot.say('**CRITICAL FAILURE**')
    else:
        baz = bar.group(1)
        biz = baz.split('d')

        if (len(biz) == 1):
            ceil = int(biz[0])
            roll = random.randint(1,ceil)
            bot.say('You rolled ' + str(roll))
        else:
            upper = int(biz[0]) + 1
            total = 0
            for i in range(1,upper):
                ceil = int(biz[1])
                roll = random.randint(1,ceil)
                total = total + roll
                bot.say('Roll {}: '.format(i) + str(roll))
            bot.say('Total: {}'.format(total))

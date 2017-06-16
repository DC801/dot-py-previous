import sopel.module

@sopel.module.commands('dogfacts')
def helloworld(bot, trigger):
    bot.say('Small quantities of grapes and raisins can cause renal failure in dogs. Chocolate, macadamia nuts, cooked onions, or anything with caffeine can also be harmful.')


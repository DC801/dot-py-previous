import sopel.module

@sopel.module.commands('enc')
def caesar(bot, trigger):
    set = {
            'a': 'b',
            'e': 'f',
            'i': 'j',
            'o': 'p',
            'u': 'q'
        }
    text = trigger.group(2)
    for key, value in set.items():
        text = text.replace(key, value)
    # print('result: {}'.format(text))
    bot.say(text)

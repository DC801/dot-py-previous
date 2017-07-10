import sopel.module
import requests
from lxml import html

@sopel.module.rule(r'\bhttp(|s)://.*\b')
def title(bot, trigger):
    url = trigger
    page = requests.get(url)
    tree = html.fromstring(page.content)
    title = tree.xpath('/html/head/title/text()')
    bot.say('{}'.format(title))

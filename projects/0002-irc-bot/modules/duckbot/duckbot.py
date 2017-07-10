import sopel.module
from sopel.db import SopelDB
from operator import itemgetter
import csv
import json
import io
import re

from collections import defaultdict
nested_dict = lambda: defaultdict(nested_dict)
list_count = nested_dict()

with open('/home/pips/.sopel/modules/duck_count.json', 'r') as infile:
    list_count = json.loads(infile.read())

leaderboard = []
for key,value in list_count.items():
  leaderboard.append({'name':str(key), 'count': value['count']})  
leaderboard = sorted(leaderboard, key=itemgetter('count'), reverse=True)

    
#list_count = json.loads

count = 0
help_message = """
BOT PURPOSE: Count ducks and inform users of their ducks.
BOT AUTHOR: @pips801
BOT VERSION: 0.4
LAST-UPDATE: July 5th, 2017
NOTE: This bot will not count duck commands or itself saying duck in the duck counter.
=======================================================================================
COMMAND: .duck help
DESC: Messages you the ducking help message.
=======================================================================================
COMMAND: .duck me
DESC: Tells you how many ducking ducks you give and your ducking place.
=======================================================================================
COMMAND: .duck {nick}
DESC: TElls you what ducking place the ducking user is in and how many ducks they give.
=======================================================================================
COMMAND: .duck leaderboard
DESC: Tells you the top 10 duckers in the ducking list.
=======================================================================================
COMMAND: .duck compare {nick1} {nick2}
DESC: Compares two ducking users and tells you which ducker is better.
=======================================================================================
COMMAND: .duck total
DESC: Tells you the ducking total for all ducks said.
=======================================================================================
COMMAND: .duck you
DESC: ducks you.
=======================================================================================
COMMAND: .duck update {nick} {number}
DESC: [ADMIN ONLY] Updates the user specified to a new ducking duck count.
=======================================================================================
COMMAND: .duck reset {nick}
DESC: [ADMIN ONLY] Resets the ducking user's duck count to 0.
=======================================================================================
"""

# handler for users saying duck
@sopel.module.rule('.*duck')
def duck_counter(bot, trigger):
  # do not process the duck if it is a command or said by the bot or im PM
  if ( not (trigger.nick == bot.nick) and not ('.duck' in trigger.group(0)) and not (trigger.is_privmsg)):
  
    global count
    global list_count
    global leaderboard
    if trigger.nick.lower() in list_count:
      list_count[trigger.nick.lower()]['count'] =+ list_count[trigger.nick.lower()]['count'] + 1
      
    else:
      #list_count[trigger.nick] = {}
      list_count[trigger.nick.lower()] = {'count': 1}
      #list_count[trigger.nick]
    
    with open('/home/pips/.sopel/modules/duck_count.json', 'w') as outfile:
      json.dump(list_count, outfile)
    
    leaderboard = []
    for key,value in list_count.items():
      leaderboard.append({'name':str(key), 'count': value['count']})  
    leaderboard = sorted(leaderboard, key=itemgetter('count'), reverse=True)
  
@sopel.module.commands('duck')
def duck_bot_handler(bot, trigger):

  global list_count
  global count
  global leaderboard
  
  if trigger.group(3) is None: 
    bot.say ('I count every time someone says duck. For commands, type .duck help .')
  
  elif trigger.group(3) == 'me':
    if trigger.nick.lower() in list_count:

      bot.say(trigger.nick + ' has said duck ' + str(list_count[trigger.nick.lower()]['count']) + ' times. Your position on the leaderboard is ' + str(1 + leaderboard.index({'count': list_count[trigger.nick.lower()]['count'], 'name': trigger.nick})))
    else:
      bot.say(trigger.nick + ' gives no ducks.')
  
    
  elif trigger.group(3) == 'leaderboard':
    bot.say('ducklist leaderboard is too big for a chanel, PrivMsging ' + trigger.nick + ' with the top 10.')
    
    bot.say('===== Top 10 ducking duckers =====', trigger.nick)
    
    a = 0
    while (a < 10) and (a < len(leaderboard)):
      if (leaderboard[a] is not None):
        bot.say(str(a+1) + ') ' + leaderboard[a]['name'] + ' with ' + str(leaderboard[a]['count']) + ' ducks given.', trigger.nick)
        a = a + 1
    bot.say('==================================', trigger.nick)
      
  elif trigger.group(3) == 'help':
    bot.say ('Messaging ' + trigger.nick + ' with all of the ducking commands.')
    global help_message
    for line in help_message.split('\n'):
      bot.say(line, trigger.nick)
      
  elif trigger.group(3) == 'total':
    total = 0
    for key, value in list_count.items():
      #total  = total + value['count']   
      total = total + value['count']
    bot.say('The duck grand total is ' + str(total) + '.')

  elif trigger.group(3) == 'compare':
    if (trigger.group(4) is not None and trigger.group(5) is not None):
      
      if (trigger.group(4).lower() in list_count and trigger.group(5).lower() in list_count):
        if (trigger.group(4) != trigger.group(5)):
          user1_name = trigger.group(4)
          user2_name = trigger.group(5)
        
          user1_count = list_count[user1_name.lower()]['count']
          user2_count = list_count[user2_name.lower()]['count']
        
          if(user1_count > user2_count):
            bot.say(user1_name + ' has said duck ' + str(user1_count - user2_count) + ' more times than ' + user2_name + '.')
          elif(user2_count > user1_count):
            bot.say(user2_name + ' has said duck ' + str(user2_count - user1_count) + ' more times than ' + user1_name+ '.')
          else:
            bot.say ('Both ' + user1_name + ' and ' + user2_name + ' have a duck count of ' + str(user1_count) + '.')
        else:
          bot.say('I can\'t compare the same user, you ducking idiot.')
      else:
        bot.say('Both specified users have to be in the duck list with a duck count.')
      
    else:
      bot.say('You have to specify two users, duckface.')

  elif trigger.group(3) == 'you':
    bot.say ('No, duck you ' + trigger.nick + '!')
    
  elif trigger.group(3) == 'update':
    if (trigger.user == '~Pips' and trigger.host == 'pips.rocks'):
      if (trigger.group(4) is not None):
        if (trigger.group(5) is not None):
          if (re.match("\d{1,6}", trigger.group(5)) is not None):
            if (trigger.group(4).lower() in list_count):
              bot.say ('Changing ' + trigger.group(4) + '\'s count from ' + str(list_count[trigger.group(4).lower()]['count']) + ' to ' + trigger.group(5))
              
              list_count[trigger.group(4).lower()]['count'] = int(trigger.group(5))
              
              with open('/home/pips/.sopel/modules/duck_count.json') as outfile:
                json.dump(list_count, outfile)
                
              leaderboard = []
              for key,value in list_count.items():
                leaderboard.append({'name':str(key), 'count': value['count']})  
                leaderboard = sorted(leaderboard, key=itemgetter('count'), reverse=True)
            
              
            else:
              bot.say ('This person doesn\'t exist in my database, I can\'t update them.')
          else:
            bot.say ('That\'s not a valid ducking number.')
        else:
          bot.say ('You have to give me a number, duckface.')
      else:
        bot.say ('You have to give me a user to update, duckface.')
    else:
      bot.say ('You are not the ducking admin of this bot, duck off.')
      
  elif trigger.group(3) == 'reset':
    if ((trigger.user == '~Pips') and (trigger.host == 'pips.rocks')):
      if (trigger.group(4) is not None):
        if (trigger.group(4).lower() in list_count):
          bot.say ('Resetting ' + trigger.group(4) + ' from ' + str(list_count[trigger.group(4).lower()]['count']) + ' to 0.' )
          list_count[trigger.group(4).lower()] = {'count': 0}
          
          with open('/home/pips/.sopel/modules/duck_count.json') as outfile:
            json.dump(list_count, outfile)
          
          leaderboard = []
          for key,value in list_count.items():
            leaderboard.append({'name':str(key), 'count': value['count']})  
            leaderboard = sorted(leaderboard, key=itemgetter('count'), reverse=True)
        
        elif (trigger.group(4) == 'all'):
          bot.say ('Resetting all ' + str(len(list_count)) + ' tracked user\'s duck count.')
          list_count = {}
          
        else:
          bot.say ('Can\'t find any duck couter to reset in my Database for ' + trigger.group(4) + '.')
        
        with open('./duck_count.json', 'w') as outfile:
          json.dump(list_count, outfile)
      else:
        bot.say ('You have to give me a user to reset, duckface.')
    else:
      bot.say ('You are not the ducking admin of this bot, duck off.')
    
  elif trigger.group(3) == bot.nick:
    bot.say ('This bot doesn\'t record it\'s own duck count, you ducking idiot.')
      
  elif trigger.group(3).lower() in list_count:
  
    leaderboard = []
    for key,value in list_count.items():
      leaderboard.append({'name':str(key), 'count': value['count']})  
      leaderboard = sorted(leaderboard, key=itemgetter('count'), reverse=True)
    bot.say(trigger.group(3) + ' has said duck ' + str(list_count[trigger.group(3).lower()]['count']) + ' times. Their position on the leaderboard is ' + str(1 + leaderboard.index({'count': list_count[trigger.group(3).lower()]['count'], 'name': trigger.group(3).lower()})))
    
  else:
    bot.say('Can\'t find any duck counter for ' + trigger.group(3) + ' in my database.')

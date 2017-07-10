import sopel.modules
import MySQLdb

db = MySQLdb.connect(host = 'localhost',
                     user = 'john',
                     passwd = 'megajohny',
                     db = 'johnydb')
@sopel.module.rule('.*duck')

@sopel.module.commands('duck')
def duck_handler(bot, trigger):
    

def duck_help():
    # Messages you the ducking help message.
def duck_me():
    # Tells you how many ducking ducks you give and your ducking place.
def duck_nick():
    # Tells you what ducking place the ducking user is in and how many ducks they give.
def duck_leaderboard():
    # Tells you the top 10 duckers in the ducking list.
def duck_compare():
    # Compares two ducking users and tells you which ducker is better.
def duck_total():
    # Tells you the ducking total for all ducks said.
def duck_you():
    # ducks you.
def duck_update():
    # [ADMIN ONLY]
    # Updates the user specified to a new ducking duck count.
def duck_reset():
    # [ADMIN ONLY]
    # Resets the ducking user's duck count to 0.

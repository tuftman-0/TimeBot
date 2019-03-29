import discord
import time
import json

def str2time(s):
    a,b = map(int,s.split(':'))
    return a,b

def time2str(t):
    return '%0.2d:%0.2d' % t

def timediff(t, t0):
    h, m   = t
    h0, m0 = t0
    return (h-h0)%12, (m-m0)%60

# this could be way more efficient but whatever
def phonetic(t):
    digits  = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    hours   = ['twelve'] + digits[1:] + ['ten', 'eleven']
    small   = [''] + ['oh-' + x for x in digits[1:]] + ['eleven', 'twelve'] + [x + 'teen' for x in ['thir','four','fif','six','seven','eigh','nine']]
    large   = [x + ('-' if y != '' else '') + y for x in ['twenty','thirty','forty','fifty','sixty'] for y in digits]
    minutes = small + large
    h, m    = t
    words   = hours[h] + ('-' if m > 0 else '') + minutes[m]
    return words


    

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="with time"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!time":
        current = time.strftime("%I:%M")
        two_to  = phonetic(timediff(str2time(current), (0,-2)))
        await message.channel.send("My clock says two to {0}; does your clock say two to {0} too".format(two_to))


# get token from file so you don't accidentally reveal it in your github repository
with open('config.json','r') as f:
    data = json.load(f)
    token = data['token']
    client.run(token)

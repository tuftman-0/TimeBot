import discord
import time, datetime
import json
import asyncio

def str2time(s):
    a,b = map(int,s.split(':'))
    return a,b

def time2str(t):
    return '%0.2d:%0.2d' % t

def timediff(t, t0):
    h, m   = t
    h0, m0 = t0
    return (h-h0)%12, (m-m0)%6

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!time":
        current = time.strftime('%I:%M')
        two_to  = time2str(timediff(str2time(current),(0,-2)))
        await message.channel.send("my clock says two to {0} does your clock say two to {0} too".format(two_to))


# @client.event
# async def time_check():
#     await client.wait_until_ready()
#     counter = 0
#     channel = discord.Object(id='542493356266356736')
#     trigger = '2:00'
#     while not client.is_closed:
#         current = time.strftime('%I:%M')
#         hour, minute = map(int,current.split(':'))
#         if 60 - minute <= 3:
#             if current == trig
#                 message.channel.send("my clock says two to {0} does your clock say two to {0} too".format(trigger)
#         else:
#             asyncio.sleep(60)
    

# get token from file so you don't accidentally reveal it in your github repository
with open('token.txt','r') as f:
    token = str(f.read())
    print(token)
    client.run(token)

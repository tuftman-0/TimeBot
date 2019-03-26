import discord
import time, datetime
import json

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        # await client.send_message(message.channel, "World")
        await message.channel.send("World")


@client.event
async def time_check():
    await client.wait_until_ready()
    counter = 0
    channel = 542493356266356736
    

# get token from file so you don't accidentally reveal it in your github repository
with open('token.txt','r') as f:
    token = f.read()

client.run(token)

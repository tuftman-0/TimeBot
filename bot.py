import discord
import time, datetime

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
    channel = 




client.run("NTU0NDcyNzUzNjM4NjcwMzM2.D3h_XA.vevLJJZ6E9i6l3G-Hl7GCvdZNJ0")
542493356266356736

"""
This will be a bot for my discord channel because I want to keep adding stuff that i canot afford in my wishlist channel ahaha
"""
#import shit here import os
import os
import discord

TOKEN = os.environ['DISCORD_TOKEN'] 
GUILD = '708547549824548945'
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(msg):
    channelName = str(msg.channel)

    cmd = msg.content.lower()

    print(cmd)

    if cmd == "!testlol":
        await msg.channel.send("This slaps fool")

# @client.event
# async def on_member_join(member):
    # channelName = 
client.run(TOKEN)
#write some class here 

#run it down here 

"""
This will be a bot for my discord channel because I want to keep adding stuff that i canot afford in my wishlist channel ahaha
"""
#import shit here import os
import os
import discord
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN'] 
GUILD = '708547549824548945'
client = discord.Client()

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
   channel = client.get_channel(708547549824548948) 
   await channel.send(f"Welcome to the Trap, be real {member}")



@bot.command('testlol')
async def on_message(msg):
    print(msg)
    if msg.author == client.user:
        return
    await msg.channel.send("This slaps bruh")


# @bot.command('boop') asynce testlol(ctx, target) ctx.send(f'{ctx.author.name} boops {target}') print('user: {ctx.author.name} used boop on {target} in {ctx.channel.name}')

# @client.event
# async def on_member_join(member):
    # channelName = 
client.run(TOKEN)
bot.run(TOKEN)
# write some class here 

#run it down here 

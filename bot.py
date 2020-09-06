"""
This will be a bot for my discord channel because I want to keep adding stuff that i canot afford in my wishlist channel ahaha
"""
#import shit here import os
import os
import discord
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN'] 
GUILD = '708547549824548945'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(708547549824548948) 
    await channel.send(f"Welcome to the Trap, be real {member}")

@bot.command('wishlist')
async def on_message(msg):
    channel = client .get_channel(752187131522187325)
    


@bot.command('testlol')
async def on_message(msg):
    if msg.author == client.user:
        return
    await msg.channel.send("This slaps bruh")

@bot.command('boop')
async def boop(ctx, target):
    await ctx.channel.send(f'{ctx.author.mention} boops {target}')


bot.run(TOKEN)


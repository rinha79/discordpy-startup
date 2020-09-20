import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='r!!')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    channel = bot.get_channel(696922604660850740)
    await channel.send("何故でしょう")
        
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
 
@bot.event
async def on_message(message):
    if message.channel.id == 696922604660850740:
        is_bot = " [BOT]"if message.author.bot else ""
        print("{0.author}{1}\n{0.content}".format(message,is_bot))

bot.run(token)

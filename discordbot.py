
import discord
from discord.ext import commands
import os
import traceback
import datetime

bot = commands.Bot(command_prefix='r!!')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    channel = bot.get_channel(696922604660850740)
    await channel.send("あいうえお")   
        
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@bot.event
async def on_message(message):
    if message.channel.id == 696922604660850740:
        is_bot = " [BOT]"if message.author.bot else ""
        date = datetime.datetime.now()
        hour = date.hour
        mnin = date.minute
        print("{0.author}{1} ({0.author.id}) str(hour)時str(mnin)分\n{0.content}".format(message,is_bot))
    await bot.process_commands(message)

bot.run(token)

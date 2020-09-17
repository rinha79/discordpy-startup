from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='r!!')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    channel = client.get_channel(696922604660850740)
    await channel.send("へっよ")
        
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))
 
@bot.command()
async def is_owner(ctx):
    return ctx.author.id == 5

@bot.command(name='eval')
@commands.check(is_owner)
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))
    
@bot.event
async def on_message(message):
    if message.channel.id == 696922604660850740:
        is_bot = " [BOT]"if message.author.bot else ""
        print("{0.author}{1}\n{0.content}".format(message,is_bot))

client.run(token)

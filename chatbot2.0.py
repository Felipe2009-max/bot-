import discord
from discord.ext import commands
from botlogic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generador(ctx, longitud:int):
    await ctx.send(f"esta es tu contrasena {gen_pass(longitud)}")
bot.run("EL TOKEN SECRETO VA AQUÍ")
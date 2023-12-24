import discord
from discord.ext import commands
from discord import Interaction
from get_data import send_link

intents = discord.Intents.default()
intents.messages = True 
intents.guilds = True 
intents.message_content = True 
client = commands.Bot(command_prefix = '!', intents=intents)
with open('./token.txt', 'r') as file:
    token = file.read()

@client.event
async def on_ready():
    print(f'{client.user.name} is ready ')

@client.command()
async def play(ctx):
    await ctx.send(f"{send_link()}")

client.run(token=token)
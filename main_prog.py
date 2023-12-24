import discord
from discord.ext import commands
import asyncio
from get_data import send_link

intents = discord.Intents.default()
intents.messages = True 
intents.guilds = True 
intents.message_content = True 
client = commands.Bot(command_prefix='!', intents=intents)

with open('../Api keys/token.txt', 'r') as file:
    token = file.read()

# Dictionary to store user inputs
user_inputs = {}

@client.event
async def on_ready():
    print(f'{client.user.name} is ready ')

@client.command()
async def play(ctx):
    # Send link
    link_message = await ctx.send(f"{send_link()} \n Your 10 seconds start now")

    # Wait for 30 seconds
    await asyncio.sleep(10)

    # Collect user input
    await ctx.send("Enter your text within the next 10 seconds:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        response = await client.wait_for('message', timeout=10.0, check=check)
        user_inputs[ctx.author.name] = response.content
        await response.delete()  # Remove the user's input message from the channel
        await ctx.author.send(f"Your input: {response.content}")
    except asyncio.TimeoutError:
        await ctx.send("Time's up! No input received.")

    # Send summary DM to everyone
    summary = "\n".join(f"{user}: {text}" for user, text in user_inputs.items())
    for user in user_inputs:
        member = ctx.guild.get_member_named(user)
        if member:
            await member.send(f"Summary:\n{summary}")

    # Clear user inputs for the next round
    user_inputs.clear()

client.run(token=token)

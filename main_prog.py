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

user_inputs = {}
user_votes = {}

@client.event
async def on_ready():
    print(f'{client.user.name} is ready ')

@client.command()
async def play(ctx):
    link_message = await ctx.send(f"{send_link()} \n Your 10 seconds start now")
    await asyncio.sleep(10)
    await ctx.send("Enter your text within the next 10 seconds:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        response = await client.wait_for('message', timeout=10.0, check=check)
        user_inputs[ctx.author.name] = response.content
        await response.delete()
        await ctx.author.send(f"Your input: {response.content}")
    except asyncio.TimeoutError:
        await ctx.send("Time's up! No input received.")

    
    summary = "\n".join(f"{user}: {text}" for user, text in user_inputs.items())
    summary_message = await ctx.send(f"Here are everyone's inputs:\n{summary}")

    await asyncio.sleep(10)
    await ctx.send("Type the username of the person with the best message:")

    def vote_check(message):
        return message.channel == ctx.channel

    try:
        vote_message = await client.wait_for('message', timeout=20.0, check=vote_check)
        best_user = vote_message.content
        if best_user in user_votes:
            user_votes[best_user] += 1
        else:
            user_votes[best_user] = 1
    except asyncio.TimeoutError:
        pass

    await ctx.send("Tally of votes:")
    for user, votes in user_votes.items():
        await ctx.send(f"{user}: {votes} vote(s)")

    user_inputs.clear()
    user_votes.clear()

client.run(token=token)

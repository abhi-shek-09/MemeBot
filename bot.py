import discord
import responses
from dotenv import load_dotenv
import os
load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = os.getenv('TOKEN')
    print(TOKEN)
    TOKEN = TOKEN
    intents = discord.Intents.default()
    intents.messages = True 

    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running...')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(username, user_message, channel)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message=message, user_message=user_message, is_private=True)
        else:
            await send_message(message=message, user_message=user_message, is_private=True)
    
    client.run(token=TOKEN)
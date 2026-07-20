import discord
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# add an intents object (what the bot is getting from discord API)
# default enables everything except presence, message content and members
intents = discord.Intents.default()

# additionally flag message_content as true bc we need that
intents.message_content = True

# create the actual bot object here and send it the intents
m3mmo = discord.Client(intents=intents)

# async event decorator that is called when client is done preparing data recieved from discord
# usually after login is complete (when is a bot logged in?)
@m3mmo.event
async def on_ready():
    print('Ready!')


@m3mmo.event
async def on_message(message):
    print(message.content)
    print(f"Message author: {1}", message.author)
    print(f"m3mmo user: {1}", m3mmo.user)
    if(message.author != m3mmo.user):
        await message.channel.send(message.content)
    else:
        pass

if __name__ == "__main__":
    # call bot.run in the actual main function here
    m3mmo.run(token)
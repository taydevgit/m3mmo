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
    channel = message.channel.name
    print(f"Message channel: {message.channel.name}")
    print(f"Message author: {message.author}")
    print(f"m3mmo user: {m3mmo.user}")

    
    
    if(message.author != m3mmo.user):
        await message.channel.send(message.content)
        match channel:
            case "sandbox":
                await message.channel.send(f"We are in the {channel} channel.")
            case "appointments":
                await message.channel.send(f"We are in the {channel} channel.")
            case "groceries":
                await message.channel.send(f"We are in the {channel} channel.")
            case "reminders":
                await message.channel.send(f"We are in the {channel} channel.")
            case "recipes":
                await message.channel.send(f"We are in the {channel} channel.")
            case "misc":
                await message.channel.send(f"We are in the {channel} channel.")
            case _:
                await message.channel.send("No valid channel found.")

        
        
    else:
        pass


if __name__ == "__main__":
    # call bot.run in the actual main function here
    m3mmo.run(token)
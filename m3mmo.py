import discord
import asyncio
from dotenv import load_dotenv
import os
from database.m3mmory import init_db


# declaring variables so they exist to initialize db in on_ready function for bot
global conn, cur

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
    conn, cur = init_db()
    print('Database initialized, bot online.')


@m3mmo.event
async def on_message(message):
    channel = message.channel.name
    print(f"Message channel: {message.channel.name}")
    print(f"Message author: {message.author}")
    print(f"m3mmo user: {m3mmo.user}")

    
    
    if(message.author != m3mmo.user):
        # await message.channel.send(message.content)
        match channel:
            case "shopping-list":
                await message.channel.send(f"Shopping list channel.")
            case "wishlist":
                await message.channel.send(f"Wishlist channel.")
            case "links":
                await message.channel.send(f"Links channel.")
            case "recipes":
                await message.channel.send(f"Recipes channel.")
            case "maintenance":
                await message.channel.send(f"Maintenance channel.")
            case "appointments":
                await message.channel.send(f"Appointments channel.")
            case "announcements":
                await message.channel.send(f"Announcements channel.")
            case "to-do":
                await message.channel.send(f"To-do channel.")
            case "monthly-bills":
                await message.channel.send(f"Monthly bills channel.")
            case "subscriptions":
                await message.channel.send(f"Subscriptions channel.")
            case "workout-plans":
                await message.channel.send(f"Workout plans channel.")
            case "progress-journal":
                await message.channel.send(f"Progress journal channel.")
            case "movies-and-shows":
                await message.channel.send(f"Movies and shows channel.")
            case "games":
                await message.channel.send(f"Games channel.")
            case "food-reviews":
                await message.channel.send(f"Food reviews channel.")
            case "sandbox":
                await message.channel.send(f"Sandbox channel.")
            case _:
                pass
    
    else:
        pass


if __name__ == "__main__":
    # call bot.run in the actual main function here
    

    m3mmo.run(token)
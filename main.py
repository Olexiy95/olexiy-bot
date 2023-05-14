import discord
from dotenv import load_dotenv
import os
import requests

# Specify which events your bot intends to listen to
intents = discord.Intents.default()

# Enable the privileged intents for members and presences (requires enabling in the Discord developer portal)
intents.members = True
intents.presences = True
intents.message_content = True


load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")  # Get bot token from environment variable
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello, world!")

    if message.content.startswith("$ping"):
        await message.channel.send("Pong!")

    if message.content.startswith("$dice"):
        import random

        result = random.randint(1, 6)
        await message.channel.send(f"The result is {result}!")

    if message.content.startswith("$flip"):
        import random

        result = random.choice(["heads", "tails"])
        await message.channel.send(f"The result is {result}!")

    if message.content.startswith("$quote"):
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        await message.channel.send(f'{data["content"]} - {data["author"]}')

    if message.content.startswith("$chuck"):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        await message.channel.send(f'{data["value"]}')


client.run(TOKEN)

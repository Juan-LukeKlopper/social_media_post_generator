import discord
import asyncio
import os

async def post_to_discord(message):
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(int(os.getenv('DISCORD_CHANNEL_ID')))  # Get channel ID from environment variable

        if channel is not None:
            await channel.send(message)
            await client.close()

    await client.start(os.getenv('DISCORD_TOKEN'))  # Get bot token from environment variable
    await asyncio.sleep(5)  # Wait for the message to be sent
    await client.close()

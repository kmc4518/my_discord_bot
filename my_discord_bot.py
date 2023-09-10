"""
KMC4518 Discord Bot 2023
"""

import discord
import spotipy
import os
from discord.ext import commands
from spotipy.oauth2 import SpotifyOAuth

# Secrets
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
MASTER_PLAYLIST_TOKEN = os.environ['MASTER_PLAYLIST_TOKEN']
YEARTWO_PLAYLIST_TOKEN = os.environ['YEAR_PLAYLIST_TOKEN']

# Define scope & command prexix

intents = discord.Intents.default()
intents.message_content = True

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
client = commands.Bot(command_prefix="+", intents=intents)

# Remove default help command
client.remove_command('help')


@client.command()
async def ping(ctx):
    """Define command to reply with the ms latency"""
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')


@client.command()
async def add(ctx, *args):
    """Define command to adds a song to Spotify playlist"""
    tracks = [*args]
    print(tracks)
    sp.playlist_add_items(MASTER_PLAYLIST_TOKEN, tracks)
    sp.playlist_add_items(YEARTWO_PLAYLIST_TOKEN, tracks)
    await ctx.send("Song added!")

print(DISCORD_TOKEN)
print(MASTER_PLAYLIST_TOKEN)
print(YEARTWO_PLAYLIST_TOKEN)

@client.event
async def on_ready():
    """Print client detials on startup"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(DISCORD_TOKEN)
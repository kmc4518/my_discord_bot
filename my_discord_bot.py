"""
V1.0 KMC4518 Discord Bot 2022
V1.1 JS 2022 #move secrets from files to ENV Vars
"""

import time
import discord
import spotipy
from discord.ext import commands
from spotipy.oauth2 import SpotifyOAuth

# Secrets
DISCORD_TOKEN = os.environ['ENV_DISCORD_TOKEN']
MASTER_PLAYLIST_TOKEN = os.environ['ENV_MASTER_PLAYLIST_TOKEN']
YEAR_PLAYLIST_TOKEN = os.environ['ENV_YEAR_PLAYLIST_TOKEN']

# Define scope & command prexix
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
client = commands.Bot(command_prefix="+")

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
    sp.playlist_add_items(YEAR_PLAYLIST_TOKEN, tracks)
    await ctx.send("Song added!")


@client.event
async def on_ready():
    """Print client detials on startup"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(DISCORD_TOKEN)


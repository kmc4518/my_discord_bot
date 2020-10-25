import discord
import spotipy
from discord.ext import commands
from spotipy.oauth2 import SpotifyOAuth

# Secrets
DISCORD_TOKEN = open("discord_token.txt", "r").readline()
SPOTIFY_PLAYLIST_TOKEN = open("sp_playlist_token.txt", "r").readline()

# Define scope & command prexix
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
client = commands.Bot(command_prefix="+")

# Remove default help command
client.remove_command('help')

# Define command to reply with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

# Define command to adds a song to Spotify playlist
@client.command()
async def add(ctx, *args):
    tracks = [*args]
    print(tracks)
    sp.playlist_add_items(SPOTIFY_PLAYLIST_TOKEN, tracks)
    await ctx.send("Done")

# Print client detials on startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(DISCORD_TOKEN)

import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 's.', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(status=discord.Status.idle, type=discord.ActivityType.playing, name=f"my carrot flute"))


client.run("NjkxMTI3MTY3ODE1NTE2MjYw.XnbcVQ.0HwwFdI21HhNZlhKdzcEmyypQyo")
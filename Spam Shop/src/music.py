import discord
from discord.ext import commands
import pafy
import youtube_dl
from youtube_search import YoutubeSearch
import os
from discord.utils import get

client = commands.Bot(command_prefix="s-")
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity=discord.Activity(status=discord.Status.idle, type=discord.ActivityType.listening, name=f"Music | s-help"))

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Music Commands", description="Here are the music commands. (Please report to an Employee if anyone are misusing/trolling with these commands)", color=discord.Color.teal())
    embed.add_field(name="!join", value="To add the bot to join the music voice channel", inline=False)
    embed.add_field(name="!leave", value="To remove the bot from the music voice channel (Employees Only)", inline=False)
    embed.add_field(name="!play <song>", value="To start playing music", inline=False)
    embed.add_field(name="!pause", value="To pause the music", inline=False)
    embed.add_field(name="!resume", value="To resume the music", inline=False)
    embed.add_field(name="!stop", value="To stop the music", inline=False)
    embed.add_field(name="!add", value="To add music to the queue", inline=False)
    embed.add_field(name="!queue", value="To see the queue", inline=False)
    embed.add_field(name="!skip", value="To skip the song", inline=False)
    embed.add_field(name="!clearQueue", value="To clear the queue (Employees Only)", inline=False)
    await ctx.send(embed=embed)

musicList = []

@client.command()
async def queue(ctx):
    async with ctx.typing():
       pass
    if len(musicList) == 0:
        await ctx.send('There are no songs in the queue.')
    else:
        q = ''
        num = 1
        for song in range(len(musicList)):
            q += f'`{num}` [{musicList[num-1]["name"]}]({musicList[num-1]["url"]}) | {musicList[num-1]["duration"]}\n'
            num += 1
        embed = discord.Embed(title="Queue", description=q, color=discord.Color.teal())
        await ctx.send(embed=embed)

@client.command()
@commands.has_role("Employee")
async def clearQueue(ctx):
    musicList.clear()
    await ctx.send("The queue has been cleared")

@client.command()
async def add(ctx, *, search: str):
    async with ctx.typing():
       pass
    results = YoutubeSearch(search, max_results=1).to_dict()
    x = results[0]
    url = 'https://www.youtube.com' + x['url_suffix']
    title = x['title']
    video = pafy.new(url)
    duration = x['duration']
    if video.length > 600:
        await ctx.send('This file too large! Please go under `10 minutes`.')
    else:
        music = {}
        music["name"] = title
        music["url"] = url
        music["duration"] = duration
        musicList.append(music)
        embed = discord.Embed(title="Song Added", description=f"[{title}]({url})", color=discord.Color.teal())
        embed.set_footer(text=f"Added by{ctx.author.name}")
        await ctx.send(embed=embed)


@client.command()
async def join(ctx):
    try:
        channel = get(ctx.message.guild.voice_channels, name="Music")
        await channel.connect()
    except commands.CommandInvokeError:
        await ctx.send('Bot is already connected to a voice channel!')

@client.command()
@commands.has_role("Employee")
async def leave(ctx):
    try:
        server = ctx.message.guild.voice_client
        await server.disconnect()
    except commands.CommandInvokeError:
        await ctx.send('Bot is not connected to a voice channel!')

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.message.add_reaction("⏸️")
    else:
        await ctx.send("Currently no audio is playing.")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.message.add_reaction("▶️")
    else:
        await ctx.send("The audio is not paused.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    try:
        os.remove('song.mp3')
    except FileNotFoundError:
        pass
    await ctx.message.add_reaction("⏹️")

@client.command()
async def skip(ctx):
    try:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        url = musicList[0]["url"]

        embed = discord.Embed(title="Now Playing", description=f'[{musicList[0]["name"]}]({url}) | {musicList[0]["duration"]}', color=discord.Color.teal())
        embed.set_footer(text="It might take a couple seconds to load")
        await ctx.send(embed=embed)

        os.remove("song.mp3")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        
        while len(musicList) != 0:
            url = musicList[0]["url"]
            print(url)
            video = pafy.new(url)

            try:
                os.remove("song.mp3")
            except FileNotFoundError:
                pass
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

            embed = discord.Embed(title="Now Playing", description=f'[{musicList[0]["name"]}]({url}) | {musicList[0]["duration"]}', color=discord.Color.teal())
            embed.set_footer(text="It might take a couple seconds to load")
            await ctx.send(embed=embed)

            musicList.pop(0)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            await asyncio.sleep(video.length)


    except IndexError:
        await ctx.send("There are no tracks on the queue!")
        

@client.command(pass_context=True)
async def play(ctx, *, search=None):
    if search is None:
         while len(musicList) != 0:

            url = musicList[0]["url"]
            print(url)
            video = pafy.new(url)

            try:
                os.remove("song.mp3")
            except FileNotFoundError:
                pass
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

            embed = discord.Embed(title="Now Playing", description=f'[{musicList[0]["name"]}]({url}) | {musicList[0]["duration"]}', color=discord.Color.teal())
            embed.set_footer(text="It might take a couple seconds to load")
            await ctx.send(embed=embed)

            musicList.pop(0)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            await asyncio.sleep(video.length)


    else:
        try:
            results = YoutubeSearch(search, max_results=1).to_dict()
            x = results[0]
            url = 'https://www.youtube.com' + x['url_suffix']
            video = pafy.new(url)
            if video.length > 600:
                await ctx.send('This file too large! Please go under `10 minutes`.')
            else:
                try:
                    os.remove("song.mp3")
                except FileNotFoundError:
                    pass
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

                embed = discord.Embed(title="Now Playing", description=f'[{x["title"]}]({url}) | {x["duration"]}', color=discord.Color.teal())
                embed.set_footer(text="It might take a couple seconds to load")
                await ctx.send(embed=embed)

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                voice.play(discord.FFmpegPCMAudio("song.mp3"))
                await asyncio.sleep(video.length)
                while len(musicList) != 0:

                    url = musicList[0]["url"]

                    os.remove("song.mp3")
                    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

                    embed = discord.Embed(title="Now Playing", description=f'[{musicList[0]["name"]}]({url}) | {musicList[0]["duration"]}', color=discord.Color.teal())
                    embed.set_footer(text="It might take a couple seconds to load")
                    await ctx.send(embed=embed)

                    musicList.pop(0)

                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, "song.mp3")
                    voice.play(discord.FFmpegPCMAudio("song.mp3"))
                    await asyncio.sleep(video.length)

        except IndexError:
            embed = discord.Embed(title='🚫 No results found for', description=f'"{search}"', color=15158332)
            await ctx.send(embed=embed)


client.run("")

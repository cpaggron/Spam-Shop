import discord
from discord.ext import commands
import json
import os
import asyncio
import random

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 's!', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready')
    n = 1
    while n == 1:
        await client.change_presence(activity=discord.Activity(status=discord.Status.idle, type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))

if os.path.exists('badge.json'):
   with open('badge.json', 'r') as file:
       badge = json.load(file)
else:
   badge = {}

if os.path.exists('bal.json'):
    with open('bal.json', 'r') as file:
        bal = json.load(file)
else:
    bal = {}

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Here are the list of commands. Command prefix: `s!`", inline=False)
    embed.add_field(name="Giveaway", value=)
    await ctx.send(embed=embed)

@client.command()
async def give(ctx, amount: int, time: int):
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if ctx.author.id == 468476776104853505:
        embed = discord.Embed(title="Spambux Giveaway", description=f"React to <:SpamShop:768583474206081054> for a chance to win {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
        embed.add_field(name="Event ends in", value=f"{time} minutes", inline=False)
        embed.set_footer(text=f"Organized by {ctx.author.name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:SpamShop:768583474206081054>')
        while time > 0:
            await asyncio.sleep(60)
            time -= 1
            embed1 = discord.Embed(title="Spambux Giveaway", description=f"React to <:SpamShop:768583474206081054> for a chance to win {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
            embed1.add_field(name="Event ends in", value=f"{time} minutes", inline=False)
            embed1.set_footer(text=f"Organized by {ctx.author.name}")
            await msg.edit(embed=embed1)
        gaw = await ctx.fetch_message(msg.id)
        users = await gaw.reactions[0].users().flatten()
        if len(users) > 3:
            N = 1
            while N == 1:
                winner = random.choice(users)
                if winner == client.user or winner == ctx.author:
                    users.remove(winner)
                else:
                    break
            win = winner.mention
            mark = '!'
            await ctx.send(f":tada: {win} has won the giveaway for {amount} <:Spambux:812017408260702248>! https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
        else:
            win = "`No One`"
            mark = '.'
            await ctx.send(f":tada: {win} has won the giveaway for {amount} <:Spambux:812017408260702248>{mark} https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
        if str(winner.id) in bal:
            bal[str(winner.id)] += amount
        else:
            bal[str(winner.id)] = amount
        with open('bal.json', 'w+') as I:
            json.dump(bal, I)

@client.command(aliases=['g'])
@commands.cooldown(1, 3600, commands.BucketType.user)
async def giveaway(ctx, amount: int, time: int):
    if os.path.exists('badge.json'):
        with open('badge.json', 'r') as file:
            badge = json.load(file)
    else:
        badge = {}
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(ctx.author.id)
    if ctx.author.id != 468476776104853505 and ctx.guild.id == 733392111130640446 and "<:Employee:785190629075976202>" in badge[user] and amount <= 1000:
        embed = discord.Embed(title="Spambux Giveaway", description=f"React to <:SpamShop:768583474206081054> for a chance to win {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
        embed.add_field(name="Event ends in", value=f"{time} minutes", inline=False)
        embed.set_footer(text=f"Organized by {ctx.author.name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:SpamShop:768583474206081054>')
        while time > 0:
            await asyncio.sleep(60)
            time -= 1
            embed1 = discord.Embed(title="Spambux Giveaway", description=f"React to <:SpamShop:768583474206081054> for a chance to win {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
            embed1.add_field(name="Event ends in", value=f"{time} minutes", inline=False)
            embed1.set_footer(text=f"Organized by {ctx.author.name}")
            await msg.edit(embed=embed1)
        gaw = await ctx.fetch_message(msg.id)
        users = await gaw.reactions[0].users().flatten()
        if len(users) > 3:
            N = 1
            while N == 1:
                winner = random.choice(users)
                if winner == client.user or winner == ctx.author:
                    users.remove(winner)
                else:
                    break
            win = winner.mention
            mark = '!'
            await ctx.send(f":tada: {win} has won the giveaway for {amount} <:Spambux:812017408260702248>! https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
        else:
            win = "`No One`"
            mark = '.'
            await ctx.send(f":tada: {win} has won the giveaway for {amount} <:Spambux:812017408260702248>! https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
        if str(winner.id) in bal:
            bal[str(winner.id)] += amount
        else:
            bal[str(winner.id)] = amount
        with open('bal.json', 'w+') as I:
            json.dump(bal, I)
    elif ctx.author.id == 468476776104853505:
        embed = discord.Embed(title="Spambux Giveaway", description=f"React to <:SpamShop:768583474206081054> for a chance to win {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
        embed.add_field(name="Event ends in", value=f"{time} minutes", inline=False)
        embed.set_footer(text=f"Organized by {ctx.author.name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:SpamShop:768583474206081054>')
        while time > 0:
            await asyncio.sleep(60)
            time -= 1
            embed1 = discord.Embed(title="Spambux Giveaway", description=f"React to <:SpamShop:768583474206081054> for a chance to win {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
            embed1.add_field(name="Event ends in", value=f"{time} minutes", inline=False)
            embed1.set_footer(text=f"Organized by {ctx.author.name}")
            await msg.edit(embed=embed1)
        gaw = await ctx.fetch_message(msg.id)
        users = await gaw.reactions[0].users().flatten()
        if len(users) > 3:
            N = 1
            while N == 1:
                winner = random.choice(users)
                if winner == client.user or winner == ctx.author:
                    users.remove(winner)
                else:
                    break
            win = winner.mention
            mark = '!'
            await ctx.send(f":tada: {win} has won the giveaway for {amount} <:Spambux:812017408260702248>! https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
        else:
            win = "`No One`"
            mark = '.'
            await ctx.send(f":tada: {win} has won the giveaway for {amount} <:Spambux:812017408260702248>{mark} https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
        if str(winner.id) in bal:
            bal[str(winner.id)] += amount
        else:
            bal[str(winner.id)] = amount
        with open('bal.json', 'w+') as I:
            json.dump(bal, I)

@client.command(aliases=['bal'])
async def balance(ctx, member : discord.Member=None):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if member == None:
        user = str(ctx.author.id)
        if user in bal:
            await ctx.send(f'{ctx.author.mention} You have {bal[user]} <:Spambux:812017408260702248>!')
        else:
            await ctx.send(f'{ctx.author.mention} You have 0 <:Spambux:812017408260702248>.')
    else:
        user = str(member.id)
        if user in bal:
            await ctx.send(f'{member.mention} has {bal[user]} <:Spambux:812017408260702248>!')
        else:
            await ctx.send(f'{member.mention} You have 0 <:Spambux:812017408260702248>.')

@client.command()
async def gift(ctx, member : discord.Member, amount : int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    receiver = str(member.id)
    donor = str(ctx.author.id)
    if amount > 0:
        if donor in bal and bal[donor] >= amount:
            if receiver in bal:
                bal[receiver] += amount
                bal[donor] -= amount
                await ctx.send(f'{ctx.author.mention} has gifted {member.mention} {amount} <:Spambux:812017408260702248>!')
                with open('bal.json', 'w+') as i:
                    json.dump(bal, i)
            else:
                bal[receiver] = 0
                bal[receiver] += amount
                bal[donor] -= amount
                await ctx.send(f'{ctx.author.mention} has gifted {member.mention} {amount} <:Spambux:812017408260702248>!')
                with open('bal.json', 'w+') as i:
                    json.dump(bal, i)
        else:
            await ctx.send('You don\'t have enough <:Spambux:812017408260702248>!')
    else:
        await ctx.send('Please put a valid number')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please put the required amount of arguments.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} You are not allowed to used that!')
    elif isinstance(error, commands.CommandOnCooldown):
        msg = "Try again in {:.2f} seconds. ".format(error.retry_after)
        embed = discord.Embed(title="You are on cooldown for this command!", description=msg, color=15158332)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found")
    elif isinstance(error, commands.BadArgument):
        pass
    else:
        raise error

client.run("")

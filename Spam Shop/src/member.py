import discord
from discord.ext import commands
from discord.utils import get
import os
import json
import asyncio

client = commands.Bot(command_prefix='!')
client.remove_command('help')

if os.path.exists('bal.json'):
   with open('bal.json', 'r') as file:
       bal = json.load(file)
else:
   bal = {}

if os.path.exists('badge.json'):
   with open('badge.json', 'r') as file:
       badge = json.load(file)
else:
   badge = {}

if os.path.exists('hasMember.json'):
   with open('hasMember.json', 'r') as file:
       hasMember = json.load(file)
else:
   hasMember = {}

@client.event
async def on_ready():
    print("Bot is ready")
    channel = client.get_channel(770331467468767253)
    await asyncio.sleep(2592000)
    for i in hasMember: 
        badge[i].remove("<:Member:785316690204164106>") 
        hasMember[i].pop
        user = await client.fetch_user(int(i))
        role = get(channel.guild.roles, name="Member")
        await user.remove_roles(role)
        await user.send('Your membership has ended.')
    with open('badge.json', 'w+') as i:
        json.dump(badge, i)
    with open('hasMember.json', 'w+') as a:
        json.dump(hasMember, a)
    print('worked')



@client.command()
async def buy(ctx, m, hi: discord.Member=None):
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if os.path.exists('badge.json'):
        with open('badge.json', 'r') as file:
            badge = json.load(file)
    else:
        badge = {}
    user = str(ctx.author.id)
    if m == 'membership':
        print(bal[user])
        if user in bal and bal[user] >= 15000:
            if user in badge and "<:Member:785316690204164106>" in badge[user]:
                await ctx.send('You already have a membership!')
            else:
                bal[user] -= 15000
                with open('bal.json', 'w+') as a:
                    json.dump(bal, a)
                userr = ctx.author
                role = get(userr.guild.roles, name="Member")
                await userr.add_roles(role)
                hasMember.append(user)
                await ctx.send(f'{ctx.author.mention} Your membership ends in 30 days')
                if user in badge:
                    badge[user].append("<:Member:785316690204164106>")
                else:
                    badge[user] = ["<:Member:785316690204164106>"]
                with open('badge.json', 'w+') as i:
                    json.dump(badge, i)
                with open('hasMember.json', 'w+') as A:
                    json.dump(hasMember, A)
                await asyncio.sleep(2592000)
                await userr.remove_roles(role)
                await ctx.author.send('Your membership has ended')
                badge[user].remove("<:Member:785316690204164106>")
                hasMember.remove(user)
                with open('hasMember.json', 'w+') as B:
                    json.dump(hasMember, B)
                with open('badge.json', 'w+') as z:
                    json.dump(badge, z)
        else:
            await ctx.send("You can't afford that!")
    
    elif m == "gift" and ctx.author.id == 468476776104853505:
        userr = hi
        role = get(userr.guild.roles, name="Member")
        await userr.add_roles(role)
        hasMember.append(userr)
        with open('hasMember.json', 'w+') as I:
            json.dump(hasMember, I)
        await ctx.send(f'{userr.mention} Your membership ends in 30 days')
        if userr in badge:
            badge[userr].append("<:Member:785316690204164106>")
        else:
            badge[userr] = ["<:Member:785316690204164106>"]
        with open('badge.json', 'w+') as i:
            json.dump(badge, i)
        await asyncio.sleep(2592000)
        await userr.remove_roles(role)
        await userr.send('Your membership has ended')
        badge[userr].remove("<:Member:785316690204164106>")
        hasMember.remove(userr)
        with open('hasMember.json', 'w+') as Z:
            json.dump(hasMember, Z)
        with open('badge.json', 'w+') as a:
            json.dump(badge, a)
    
    elif m == "gift" and ctx.author.id != 468476776104853505:
        if user in bal and bal[user] >= 15000:
            userr = hi
            role = get(userr.guild.roles, name="Member")
            await userr.add_roles(role)
            hasMember.append(userr)
            with open('hasMember.json', 'w+') as H:
                json.dump(hasMember, H)
            await ctx.send(f'{userr.mention} Your membership ends in 30 days')
            if userr in badge:
                badge[userr].append("<:Member:785316690204164106>")
            else:
                badge[userr] = ["<:Member:785316690204164106>"]
            with open('badge.json', 'w+') as i:
                json.dump(badge, i)
            await asyncio.sleep(2592000)
            await userr.remove_roles(role)
            await userr.send('Your membership has ended')
            badge[userr].remove("<:Member:785316690204164106>")
            hasMember.remove(userr)
            with open('hasMember.json', 'w+') as Q:
                json.dump(hasMember, Q)
            with open('badge.json', 'w+') as a:
                json.dump(badge, a)
        else:
            await ctx.send('You can\'t afford that!')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} You are not allowed to used that!')
    elif isinstance(error, commands.CommandOnCooldown):
        msg = "Try again in {:.2f} seconds. ".format(error.retry_after)
        embed = discord.Embed(title="You are on cooldown for this command!", description=msg, color=15158332)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.BadArgument):
        pass
    else:
        raise error


client.run('')

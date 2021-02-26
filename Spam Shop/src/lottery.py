import discord
from discord.ext import commands
import asyncio
import random
import json
from discord.utils import get
import os

client = commands.Bot(command_prefix='!')
client.remove_command('help')

if os.path.exists('tickets.json'):
   with open('tickets.json', 'r') as zozo:
       ticket = json.load(zozo)
else:
   ticket = {}

if os.path.exists('cticket.json'):
   with open('cticket.json', 'r') as zozi:
       cticket = json.load(zozi)
else:
   cticket = []

if os.path.exists('lticket.json'):
   with open('lticket.json', 'r') as zoza:
       lticket = json.load(zoza)
else:
   lticket = []

if os.path.exists('rticket.json'):
   with open('rticket.json', 'r') as zoze:
       rticket = json.load(zoze)
else:
   rticket = []

if os.path.exists('dticket.json'):
   with open('dticket.json', 'r') as zozn:
       dticket = json.load(zozn)
else:
   dticket = []

if os.path.exists('tticket.json'):
   with open('tticket.json', 'r') as zozl:
       tticket = json.load(zozl)
else:
   tticket = []

if os.path.exists('bal.json'):
   with open('bal.json', 'r') as zozl:
       bal = json.load(zozl)
else:
   bal = {}

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def autoLottery(ctx):
    if ctx.author.id == 468476776104853505:
        if os.path.exists('bal.json'):
            with open('bal.json', 'r') as zozl:
                bal = json.load(zozl)
        else:
            bal = {}
        await ctx.channel.purge(limit=1)
        n = 2
        while n == 2:
            if os.path.exists('bal.json'):
                with open('bal.json', 'r') as file:
                    bal = json.load(file)
            else:
                bal = {}
            customer = get(ctx.guild.roles, name='Customers')
            try:
                c = random.randint(0, 19)
                cticketw = await client.fetch_user(cticket[c])
                one = str(cticketw.mention)
                bal[str(cticket[c])] += 100
            except IndexError:
                one = '`No One`'
            try:
                lticketw = await client.fetch_user(lticket[random.randint(0, 24)])
                two = str(lticketw.mention)
                bal[str(lticket[c])] += 500
            except IndexError:
                two = '`No One`'
            try:
                rticketw = await client.fetch_user(rticket[random.randint(0, 49)])
                three = str(rticketw.mention)
                bal[str(rticket[c])] += 750
            except IndexError:
                three = '`No One`'
            try:
                dticketw = await client.fetch_user(dticket[random.randint(0, 199)])
                four = str(dticketw.mention)
                bal[str(dticket[c])] += 1500
            except IndexError:
                four = '`No One`'
            try:
                tticketw = await client.fetch_user(tticket[random.randint(0, 999)])
                five = str(tticketw.mention)
                bal[str(tticket[c])] += 100000
            except IndexError:
                five = '`No One`'
            await ctx.send(f'{customer.mention}\n**This week\'s lotter winners are...**\n\n`1` {one}\n`2` {two}\n`3` {three}\n`4` {four}\n`5` {five}\nThe coins will be automatically added to your accounts. Thank you for ~~wasting~~ investing your money in the lottery! The drawing is next Sunday.\n\n*To see the lottery tickets do `!lottery` It will give you instructions on how to buy one.*\n\n-Christopher\n\n*To get pinged for these notifications, use the command `!sub`. You can undo it anytime with `!unsub`.*')
            ticket["cticket"] = 20
            ticket["lticket"] = 25
            ticket["rticket"] = 50
            ticket["dticket"] = 200
            ticket["tticket"] = 1000
            cticket.clear()
            lticket.clear()
            rticket.clear()
            dticket.clear()
            tticket.clear()
            with open('cticket.json', 'w') as a:
                json.dump(cticket, a)
            with open('lticket.json', 'w') as b:
                json.dump(lticket, b)
            with open('rticket.json', 'w') as c:
                json.dump(rticket, c)
            with open('dticket.json', 'w') as d:
                json.dump(dticket, d)
            with open('tticket.json', 'w') as e:
                json.dump(tticket, e)
            with open('tickets.json', 'w+') as i:
                json.dump(ticket, i)
            await asyncio.sleep(604800)
    else:
        pass


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

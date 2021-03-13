import os
import random
import discord
import time
import asyncio
from discord.ext import commands
import json
from discord.utils import get
from discord.ext import menus


TOKEN = 'NzIwODU2NjUwNTgzMzc1ODcz.XxfEFw.lIlq2EQW3JBtjfn0Uy8i9_V9u4I'

# Some things we ought to know

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!', intents=intents)
client.remove_command('help')

# Bot Status
@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(status=discord.Status.idle, type=discord.ActivityType.watching, name=f"for orders | v3.0.1"))

if os.path.exists('pop.json'):
    with open('pop.json', 'r') as file:
        population = json.load(file)
else:
    population = {}

@client.event
async def on_member_join(member):
    embed = discord.Embed(title=f"Welcome to Spam Shop {member.name}!", description="Spam Shop is a virtual restaurant where you get Spambux and food", color=discord.Color.blue())
    embed.add_field(name="Check these places out!", value="[Rules](https://discord.com/channels/733392111130640446/767103070835310612/768959613022109718)\n[What to do in this server](https://discord.com/channels/733392111130640446/733721320315027466/770352535357489155)\n[Yelpp](https://discord.com/channels/733392111130640446/770686661868650546/770705321956999218)", inline=False)
    embed.add_field(name="Other Tips", value="`!help` For a list of commands\n`!profile` To see your Spam Shop stats!\n`!collect` To get <:Spambux:812017408260702248> every minute\n`!order [food]` To order food. Do it only in the #order channel\n`!rate [stars] [review]` To rate Spam Shop on #yelpp. (e.g. !rate 5 Good Food)\n`!menu` Check out our menu!\n`!lottery` To view our lottery tickets\n`!sub` To subscribe to announcement pings\n\nIf you have any other questions, you can DM or ping an Employee or CEO (We are friendly). We hope you enjoy your time here!", inline=False)
    embed.add_field(name="Extra", value="[Server Invite Link](https://discord.gg/AkYyFy5)\n[Giveaway Bot Invite](https://discord.com/api/oauth2/authorize?client_id=786019288326209536&permissions=347200&scope=bot)")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/808811371268931605/811739649999241256/spamshop.png")
    await member.send(embed=embed)

@client.event
async def on_member_remove(member):
    pass


if os.path.exists('badge.json'):
    with open('badge.json', 'r') as file:
        badge = json.load(file)
else:
    badge = {}


if os.path.exists('spent.json'):
    with open('spent.json', 'r') as file:
        spent = json.load(file)
else:
    spent = {}

if os.path.exists('won.json'):
   with open('won.json', 'r') as file:
       won = json.load(file)
else:
   won = {}

if os.path.exists('lost.json'):
   with open('lost.json', 'r') as file:
       lost = json.load(file)
else:
   lost = {}

class welp(menus.Menu):

    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed(title="Help", description=":coin: `Currency`\n:shallow_pan_of_food: `Food`\n🏓 `Role`\n<:SpamShop:768583474206081054> `Others`", color=3447003)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        return await channel.send(embed=embed)

    @menus.button('🏛️')
    async def on_home(self, payload):
        embed = discord.Embed(title="Help", description=":coin: Currency\n:shallow_pan_of_food: Food\n🏓 Role\n<:SpamShop:768583474206081054> Others", color=3447003)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        return await self.message.edit(embed=embed)
    
    @menus.button('🪙')
    async def on_one(self, payload):
        embed = discord.Embed(title="Currency Commands", description="Here are the currency commands", color=discord.Color.blue())
        embed.add_field(name="!dice [@user] [amount]", value="To play Dice of Doom | Contributed by IKnowWhoGokulIs#6874", inline=False)
        embed.add_field(name="!sec [@user] [amount]", value="Get closest to 5 seconds! Gamble against your friends!", inline=False)
        embed.add_field(name="!collect", value="To get money", inline=False)
        embed.add_field(name="!balance", value="To see how much money you have", inline=False)
        embed.add_field(name="!coinflip [heads/tails] [amount]", value="To gamble by flipping a coin", inline=False)
        embed.add_field(name="!gift [@user] [amount]", value="To gift someone some money", inline=False)
        embed.add_field(name="!daily", value="To get some money everyday", inline=False)
        embed.add_field(name="!extra", value="An extra daily command for members only", inline=False)
        embed.add_field(name="!tictactoe [user] [amount]", value="To play tic tac toe against another user", inline=False)
        embed.add_field(name="!num [number]", value="To guess a number from 1 - 1000. Costs 5 <:Spambux:812017408260702248>. Can win 10000 <:Spambux:812017408260702248>.", inline=False)
        embed.add_field(name="!lottery", value="To see the lottery tickets and avliability", inline=False)
        embed.add_field(name="!buy [Number]", value="To buy a lottery ticket", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)
        
    @menus.button('🥘')
    async def on_two(self, payload):
        embed = discord.Embed(title="Food Commands", description="Here are the food commands.", color=discord.Color.blue())
        embed.add_field(name="!menu", value="To see the menu", inline=False)
        embed.add_field(name="!order [food]", value="To order something on the menu", inline=False)
        embed.add_field(name="!speed", value="To see how fast the service is (Ping)", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)
        
    @menus.button('🏓')
    async def on_three(self, payload):
        embed = discord.Embed(title="Role Commands", description="Here are the role commands.", color=discord.Color.blue())
        embed.add_field(name="!event", value="To subscribe to event pings", inline=False)
        embed.add_field(name="!unevent", value="To unsubscribe to event pings", inline=False)
        embed.add_field(name="!sub", value="To subscribe to announcement pings", inline=False)
        embed.add_field(name="!unsub", value="To unsubscribe to announcement pings", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)
        
    @menus.button('<:SpamShop:768583474206081054>')
    async def on_four(self, payload):
        embed = discord.Embed(title="Other Commands", description="Here are the other commands", color=discord.Color.blue())
        embed = discord.Embed(title="Commands", description="Here are the commands", color=3447003)
        embed.add_field(name="!suggest [suggestion]", value="To suggest something for the menu. PLEASE BE LOGICAL", inline=False)
        embed.add_field(name="!leaderboard", value="To view the leaderboard", inline=False)
        embed.add_field(name="!rate [stars] [review]", value="To review Spam Shop on Yelpp", inline=False)
        embed.add_field(name="!rank", value="To check your level.", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)

    @menus.button('⏹️')
    async def on_stop(self, payload):
        self.stop()

@client.command()
async def help(ctx):
    async with ctx.typing():
       pass
    await welp().start(ctx)
    
            

@client.command()
async def mute(ctx, member: discord.Member, reason, *, date):
    if ctx.author.id == 468476776104853505:
        await ctx.channel.purge(limit=1)
        role = get(ctx.guild.roles, name='Quarantined')
        await member.add_roles(role)
        await ctx.send(f'{member.mention} has been muted.')
        channel = client.get_channel(767129162439196733)
        await channel.send(f'{member.mention} has been quarantined for {reason} until {date}.')
    else:
        pass

@client.command()
async def unmute(ctx, member: discord.Member):
    if ctx.author.id == 468476776104853505:
        await ctx.channel.purge(limit=1)
        role = get(ctx.guild.roles, name='Quarantined')
        await member.remove_roles(role)
        await ctx.send(f'{member.mention} has been unmuted.')
    else:
        pass


@client.command()
async def sub(ctx):
    async with ctx.typing():
       pass
    user = ctx.author
    role = get(user.guild.roles, name="Customers")
    await user.add_roles(role)
    await ctx.send(f'{ctx.author.mention} You have subscribed for announcement pings.')

@client.command()
async def unsub(ctx):
    async with ctx.typing():
       pass
    user = ctx.author
    role = get(user.guild.roles, name="Customers")
    await user.remove_roles(role)
    await ctx.send(f'{ctx.author.mention} You have unsubscribed for announcement pings.')
    
@client.command()
async def event(ctx):
    async with ctx.typing():
       pass
    user = ctx.author
    role = get(user.guild.roles, name="Events")
    await user.add_roles(role)
    await ctx.send(f'{ctx.author.mention} You have subscribed for giveaway pings.')

@client.command()
async def unevent(ctx):
    async with ctx.typing():
       pass
    user = ctx.author
    role = get(user.guild.roles, name="Events")
    await user.remove_roles(role)
    await ctx.send(f'{ctx.author.mention} You have unsubscribed for giveaway pings.')


if os.path.exists('bal.json'):
   with open('bal.json', 'r') as file:
       bal = json.load(file)
else:
   bal = {}

@client.command()
async def unreward(ctx, member: discord.Member, amount: int):
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(member.id)
    if ctx.author.id == 468476776104853505:
        if user in bal and bal[user] >= amount:
            bal[user] -= amount
        else:
            bal[user] = 0
        with open('bal.json', 'w+') as i:
            json.dump(bal, i)
    else:
        pass

@client.command()
async def num(ctx, amount: int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(ctx.author.id)
    if user in bal and bal[user] >= 5:
        bal[user] -= 5
        l = random.randint(1, 100000)
        if amount == l:
            await ctx.send(f'{ctx.author.mention} HOLY!!!!!!!!!!!!!!!!! You guessed it!!!!!!!!! You got 100,000 <:Spambux:812017408260702248>!!!!!')
            bal[user] += 100000
            if user in won:
                won[user] += 100000
            else:
                won[user] = 100000
        else:
            await ctx.send(f'You lost. The number was {l}.')
            if user in lost:
                lost[user] += 5
            else:
                lost[user] = 5
        with open('bal.json', 'w+') as i:
            json.dump(bal, i)
        with open('won.json', 'w+') as w:
            json.dump(won, w)
        with open('lost.json', 'w+') as l:
            json.dump(lost, l)
    else:
        await ctx.send(f'{ctx.author.mention} You can\'t afford that!')


# Contributed by ggpigeotto -----------------------------------------------------------------------------------------
@client.command()
async def dice(ctx, member : discord.Member, amount : int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user1 = str(ctx.author.id)
    user2 = str(member.id)
    player1 = ctx.author
    player2 = member
    if member.id == 814907331124265010:
        await ctx.send('You cheater, you lose all your money to the bot.')
        bal[user2] += bal[user1]
    else:
        if user1 in bal and user2 in bal and bal[user1] >= amount and bal[user2] >= amount and amount > 0:
            msg = await ctx.send(f'{member.mention} {ctx.author.name} has challenged you to Dice of Doom!')
            await msg.add_reaction('👍')
            def check(reaction, user):
                return user == member and str(reaction.emoji) == '👍'
            try:
                await client.wait_for('reaction_add', timeout=60, check=check)
            except asyncio.TimeoutError:
                await msg.edit(content='This request has timed out!')
            else:
              msg1 = await ctx.send(f'{player1.mention} Click this to Roll!')
              await msg1.add_reaction('🎲')
              def check2(reaction, user):
                  return user == player1 and str(reaction.emoji) == '🎲'
              try:
                  await client.wait_for('reaction_add', timeout=60, check=check2)
              except asyncio.TimeoutError:
                  await msg1.edit(content='Opponent Wins')
                  bal[user1] -= amount 
                  bal[user2] += amount
                  with open("bal.json", "w+") as i:
                    json.dump(bal, i)
              else:
                roll1 = random.randint(1, 10)
                await ctx.send(f"{player1.mention} You got a {roll1}!")
                
                # Below is start of user 2 turn

                msg2 = await ctx.send(f'{player2.mention} Click this to Roll!')
                await msg2.add_reaction('🎲')
                def check1(reaction, user):
                    return user == player2 and str(reaction.emoji) == '🎲'
                try:
                    await client.wait_for('reaction_add', timeout=60, check=check1)
                except asyncio.TimeoutError:
                    await msg2.edit(content='Opponent Wins')
                    bal[user2] -= amount 
                    bal[user1] += amount
                    with open("bal.json", "w+") as i:
                      json.dump(bal, i)
                else:
                  roll2 = random.randint(1, 10)
                  await ctx.send(f"{player2.mention} You got a {roll2}!")

                  # below, check who is the winner

                  if roll1>roll2:
                    await ctx.send(f"{player1.mention} You win {amount} <:Spambux:812017408260702248>")
                    bal[user2] -= amount 
                    bal[user1] += amount
                  elif roll2>roll1:
                   await ctx.send(f"{player2.mention} You win {amount} <:Spambux:812017408260702248>")
                   bal[user1] -= amount 
                   bal[user2] += amount
                  elif roll1 == roll2:
                    await ctx.send(f"Time for a Tie-Breaker,{player2.mention} we will re-roll your roll") 
                    tie=True
                    while tie:
                        roll2 = random.randint(1, 10)
                        if roll2 == roll1:
                          pass
                        else:
                          break
                    await ctx.send(f"You rolled a {roll2}")
                    if roll2 > roll1:
                      await ctx.send(f"{player2.mention} You win {amount} <:Spambux:812017408260702248>")
                      bal[user2] -= amount 
                      bal[user1] += amount
                    else:
                      bal[user2] += amount 
                      bal[user1] -= amount
                  with open ("bal.json", "w+") as z:
                    json.dump(bal, z)
        else:
          await ctx.send("One of you can't afford the gamble!")
# --------------------------------------------------------------------------------------------------------------

winner = 1
@client.command()
async def tictactoe(ctx, member: discord.Member, amount: int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if str(member.id) in bal and str(ctx.author.id) in bal and bal[str(ctx.author.id)] >= amount and bal[str(member.id)] >= amount:
        tick = await ctx.send('**Tic Tac Toe** To join, click the 🚪')
        await tick.add_reaction('🚪')
        client.get_user(720856650583375873)
        def check(reaction, user):
            return user == member and str(reaction.emoji) == '🚪' 
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
        except asyncio.TimeoutError:
            await tick.edit(content='The game request has timed out!')
            await tick.clear_reaction('🚪')
        else:
            game = 9
            player_1 = ctx.author
            player_2 = user
            at = ':regional_indicator_a:'
            bt = ':regional_indicator_b:'
            ct = ':regional_indicator_c:'
            dt = ':regional_indicator_d:'
            et = ':regional_indicator_e:'
            ft = ':regional_indicator_f:'
            gt = ':regional_indicator_g:'
            ht = ':regional_indicator_h:'
            it = ':regional_indicator_i:'
            ttt_board = await ctx.send(f'**Tic Tac Toe**\n\nTurn: {player_1.mention}\n\n{at}{bt}{ct}\n{dt}{et}{ft}\n{gt}{ht}{it}\n\n{player_1.mention} vs. {player_2.mention}')
            reactions = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮']
            for z in range(len(reactions)):
                await ttt_board.add_reaction(reactions[z])
            while game != 0:
                def chec(reaction, user):
                    return str(reaction.emoji) in reactions and user == player_1
                try:
                    reaction, user = await client.wait_for("reaction_add", timeout=None, check=chec)
                    if str(reaction.emoji) == '🇦' and '🇦' in reactions:
                        at = ':o:'
                        reactions.remove('🇦')
                        await ttt_board.clear_reaction('🇦')
                    elif str(reaction.emoji) == '🇧' and '🇧' in reactions:
                        bt = ':o:'
                        reactions.remove('🇧')
                        await ttt_board.clear_reaction('🇧')
                    elif str(reaction.emoji) == '🇨' and '🇨' in reactions:
                        ct = ':o:'
                        reactions.remove('🇨')
                        await ttt_board.clear_reaction('🇨')
                    elif str(reaction.emoji) == '🇮' and '🇮' in reactions:
                        it = ':o:'
                        reactions.remove('🇮')
                        await ttt_board.clear_reaction('🇮')
                    elif str(reaction.emoji) == '🇩' and '🇩' in reactions:
                        dt = ':o:'
                        reactions.remove('🇩')
                        await ttt_board.clear_reaction('🇩')
                    elif str(reaction.emoji) == '🇪' and '🇪' in reactions:
                        et = ':o:'
                        reactions.remove('🇪')
                        await ttt_board.clear_reaction('🇪')
                    elif str(reaction.emoji) == '🇫' and '🇫' in reactions:
                        ft = ':o:'
                        reactions.remove('🇫')
                        await ttt_board.clear_reaction('🇫')
                    elif str(reaction.emoji) == '🇬' and '🇬' in reactions:
                        gt = ':o:'
                        reactions.remove('🇬')
                        await ttt_board.clear_reaction('🇬')
                    elif str(reaction.emoji) == '🇭' and '🇭' in reactions:
                        ht = ':o:'
                        reactions.remove('🇭')
                        await ttt_board.clear_reaction('🇭')
                    await ttt_board.edit(content=f'**Tic Tac Toe**\n\nTurn: {player_2.mention}\n\n{at}{bt}{ct}\n{dt}{et}{ft}\n{gt}{ht}{it}\n\n{player_1.mention} vs. {player_2.mention}')
                    if at == ':o:' and bt == ':o:' and ct == ':o:':
                        winner = player_1
                        game = 0
                        break
                    elif dt == ':o:' and et == ':o:' and ft == ':o:':
                        winner = player_1
                        game = 0 
                        break
                    elif gt == ':o:' and ht == ':o:' and it == ':o:':
                        winner = player_1
                        game = 0
                        break
                    elif at == ':o:' and dt == ':o:' and gt == ':o:':
                        winner = player_1
                        game = 0
                        break
                    elif bt == ':o:' and et == ':o:' and ht == ':o:':
                        winner = player_1
                        game = 0
                        break
                    elif ct == ':o:' and ft == ':o:' and it == ':o:':
                        winner = player_1
                        game = 0
                        break
                    elif at == ':o:' and et == ':o:' and it == ':o:':
                        winner = player_1
                        game = 0
                        break
                    elif ct == ':o:' and et == ':o:' and gt == ':o:':
                        winner = player_1
                        game = 0
                        break
                    else:
                        game -= 1
                        if game == 0:
                            winner = 'Tie'
                            break
                except asyncio.TimeoutError:
                    await ctx.send('Type this command: ```v.bug ttt timeout error```')

                if game == 0:
                    winner = 'Tie'
                    break

                # Player 2's turn
                def chek(reaction, user):
                    return str(reaction.emoji) in reactions and user == player_2
                try:
                    reaction, user = await client.wait_for("reaction_add", timeout=None, check=chek)
                    if str(reaction.emoji) == '🇦' and '🇦' in reactions:
                        at = ':x:'
                        reactions.remove('🇦')
                        await ttt_board.clear_reaction('🇦')
                    elif str(reaction.emoji) == '🇧' and '🇧' in reactions:
                        bt = ':x:'
                        reactions.remove('🇧')
                        await ttt_board.clear_reaction('🇧')
                    elif str(reaction.emoji) == '🇨' and '🇨' in reactions:
                        ct = ':x:'
                        reactions.remove('🇨')
                        await ttt_board.clear_reaction('🇨')
                    elif str(reaction.emoji) == '🇮' and '🇮' in reactions:
                        it = ':x:'
                        reactions.remove('🇮')
                        await ttt_board.clear_reaction('🇮')
                    elif str(reaction.emoji) == '🇩' and '🇩' in reactions:
                        dt = ':x:'
                        reactions.remove('🇩')
                        await ttt_board.clear_reaction('🇩')
                    elif str(reaction.emoji) == '🇪' and '🇪' in reactions:
                        et = ':x:'
                        reactions.remove('🇪')
                        await ttt_board.clear_reaction('🇪')
                    elif str(reaction.emoji) == '🇫' and '🇫' in reactions:
                        ft = ':x:'
                        reactions.remove('🇫')
                        await ttt_board.clear_reaction('🇫')
                    elif str(reaction.emoji) == '🇬' and '🇬' in reactions:
                        gt = ':x:'
                        reactions.remove('🇬')
                        await ttt_board.clear_reaction('🇬')
                    elif str(reaction.emoji) == '🇭' and '🇭' in reactions:
                        ht = ':x:'
                        reactions.remove('🇭')
                        await ttt_board.clear_reaction('🇭')
                    await ttt_board.edit(content=f'**Tic Tac Toe**\n\nTurn: {player_1.mention}\n\n{at}{bt}{ct}\n{dt}{et}{ft}\n{gt}{ht}{it}\n\n{player_1.mention} vs. {player_2.mention}')
                    if at == ':x:' and bt == ':x:' and ct == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif dt == ':x:' and et == ':x:' and ft == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif gt == ':x:' and ht == ':x:' and it == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif at == ':x:' and dt == ':x:' and gt == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif bt == ':x:' and et == ':x:' and ht == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif ct == ':x:' and ft == ':x:' and it == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif at == ':x:' and et == ':x:' and it == ':x:':
                        winner = player_2
                        game = 0
                        break
                    elif ct == ':x:' and et == ':x:' and gt == ':x:':
                        winner = player_2
                        game = 0
                        break
                    else:
                        game -= 1
                        if game == 0:
                            winner = 'Tie'
                            break
                except asyncio.TimeoutError:
                    await ctx.send('Type this command: ```!bug ttt timeout error```')
            
            await ttt_board.edit(content=f'**Tic Tac Toe**\n\nWinner: **{winner}**\n\n{at}{bt}{ct}\n{dt}{et}{ft}\n{gt}{ht}{it}\n\n{player_1.mention} vs. {player_2.mention}')
            for t in range(len(reactions)):
                await ttt_board.clear_reaction(reactions[t])
                if winner == player_1:
                    bal[str(ctx.author.id)] += amount
                    bal[str(user.id)] -= amount
                    with open('bal.json', 'w+') as I:
                        json.dump(bal, I)
                elif winner == player_2:
                    bal[str(ctx.author.id)] -= amount
                    bal[str(user.id)] += amount
                    with open('bal.json', 'w+') as I:
                        json.dump(bal, I)
                else:
                    pass

    else:
        await ctx.send("One of you can't afford the gamble!")


@client.command()
async def sec(ctx, member : discord.Member, amount : int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user1 = str(ctx.author.id)
    user2 = str(member.id)
    if member.id == 720856650583375873:
        await ctx.send('You cheater, you lose all your money to the bot.')
        bal[user2] += bal[user1]
    else:
        if user1 in bal and user2 in bal and bal[user1] >= amount and bal[user2] >= amount and amount > 0:
            msg = await ctx.send(f'{member.mention} {ctx.author.name} has challenged you to the 5 seconds game!')
            await msg.add_reaction('🚪')
            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🚪'
            try:
                await client.wait_for('reaction_add', timeout=60, check=check)
            except asyncio.TimeoutError:
                await msg.edit(content='This request has timed out!')
            else:
                a = 3
                embed = discord.Embed(title=a, description=f'{ctx.author.mention} Type any message at 5 seconds', color=discord.Color.blue())
                l = await ctx.send(embed=embed)
                a -= 1
                await asyncio.sleep(1)
                embed = discord.Embed(title=a, description=f'{ctx.author.mention} Type any message at 5 seconds', color=discord.Color.blue())
                await l.edit(embed=embed)
                a -= 1
                await asyncio.sleep(1)
                embed = discord.Embed(title=a, description=f'{ctx.author.mention} Type any message at 5 seconds', color=discord.Color.blue())
                await l.edit(embed=embed)
                await asyncio.sleep(1)
                await ctx.send('Go!')
                begin = time.time()
                await client.wait_for('message', check=lambda message: message.author == ctx.author)
                end = time.time()
                u1 = end - begin
                await ctx.send(f'{ctx.author.mention} You got {u1} seconds')
                a = 3
                embed = discord.Embed(title=a, description=f'{member.mention} Type any message at 5 seconds', color=discord.Color.blue())
                m = await ctx.send(embed=embed)
                a -= 1
                await asyncio.sleep(1)
                embed = discord.Embed(title=a, description=f'{member.mention} Type any message at 5 seconds', color=discord.Color.blue())
                await m.edit(embed=embed)
                a -= 1
                await asyncio.sleep(1)
                embed = discord.Embed(title=a, description=f'{member.mention} Type any message at 5 seconds', color=discord.Color.blue())
                await m.edit(embed=embed)
                await asyncio.sleep(1)
                await ctx.send('Go!')
                begin = time.time()
                await client.wait_for('message', check=lambda message: message.author == member)
                end = time.time()
                u2 = end - begin
                await ctx.send(f'{member.mention} You got {u2} seconds')
                uu1 = u1 - 5
                uu2 = u2 - 5
                if abs(uu1) < abs(uu2):
                    await ctx.send(f'{ctx.author.name} wins!')
                    bal[user1] += amount
                    if user1 in won:
                        won[user1] += amount
                    else:
                        won[user1] = amount
                    bal[user2] -= amount
                    if user2 in lost:
                        lost[user2] += amount
                    else:
                        lost[user2] = amount
                elif abs(uu1) > abs(uu2):
                    await ctx.send(f'{member.mention} wins!')
                    bal[user1] -= amount
                    bal[user2] += amount
                    if user2 in won:
                        won[user1] += amount
                    else:
                        won[user2] = amount
                    if user1 in lost:
                        lost[user1] += amount
                    else:
                        lost[user1] = amount
                else:
                    await ctx.send('Tie. You both get 500K <:Spambux:812017408260702248>')
                    bal[user1] += 500000
                    bal[user2] += 500000
                    if user1 in won:
                        won[user1] += 500000
                    else:
                        won[user1] = 500000
                    if user2 in won:
                        won[user2] += 500000
                    else:
                        won[user2] = 500000
            with open('bal.json', 'w+') as i:
                json.dump(bal, i)
            with open('won.json', 'w+') as w:
                json.dump(won, w)
            with open('lost.json', 'w+') as l:
                json.dump(lost, l)

        else:
            if amount <= 0:
                await ctx.send('Invalid amount')
            else:
                await ctx.send('One of you can\'t afford the gamble!')

@client.command(aliases=['c'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def collect(ctx):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if ctx.channel.id in [733392111570911346, 767148961784922152, 771854973578510386, 770353347584196648, 770352409478037545, 771794804412645376]:
        await ctx.send('That command is not allowed here!')
    else:
        user = str(ctx.author.id)
        if user in bal:
            coin = random.randint(1, 200)
            bal[user] += coin
            await ctx.send(f'{ctx.author.mention} You collected {coin} <:Spambux:812017408260702248>!')
            with open('bal.json', 'w+') as i:
                json.dump(bal, i)
        else:
            if bal[user] > 200000:
                await ctx.send('You won nothing.')
            elif bal[user] > 150000:
               coin = random.randint(1, 5)
            elif bal[user] > 100000:
                coin = random.randint(1, 10)
            elif bal[user] > 50000:
                coin = random.randtint(1, 25)
            elif bal[user] > 25000:
                bal[user] = random.randint(1, 100)
            else:
                bal[user] = random.randint(1, 200)
            bal[user] = coin
            await ctx.send(f'{ctx.author.mention} You collected {coin} <:Spambux:812017408260702248>!')
            with open('bal.json', 'w+') as i:
                json.dump(bal, i)

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
            embed = discord.Embed(title=str(ctx.author.name), description=f"{bal[user]} <:Spambux:812017408260702248>", color=discord.Color.blue())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=str(ctx.author.name), description=f"0 <:Spambux:812017408260702248>", color=discord.Color.blue())
            await ctx.send(embed=embed)
    else:
        user = str(member.id)
        if user in bal:
            embed = discord.Embed(title=str(member.name), description=f"{bal[user]} <:Spambux:812017408260702248>", color=discord.Color.blue())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=str(member.name), description=f"0 <:Spambux:812017408260702248>", color=discord.Color.blue())
            await ctx.send(embed=embed)

@client.command(aliases=['g'])
async def gift(ctx, member : discord.Member, amount : int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if ctx.channel.id != 733392111570911346:
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
    else:
        await ctx.send('This command isn\'t allowed here!')

@client.command(aliases=['cf'])
async def coinflip(ctx, call, amount : int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(ctx.author.id)
    l = random.randint(1, 2)
    if user in bal and amount <= bal[user] and amount > 0 and call in ['h', 'heads', 't', 'tails']:
        if l == 1 and call in ['h', 'heads'] or l == 2 and call in ['t', 'tails']:
            bal[user] += amount
            if l == 1:
                embed = discord.Embed(title=f"The flip was heads!", description=f"You won {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
            else:
                embed = discord.Embed(title=f"The flip was tails!", description=f"You won {amount} <:Spambux:812017408260702248>!", color=discord.Color.blue())
            if user in won:
                won[user] += amount
            else:
                won[user] = amount
            await ctx.send(embed=embed)
        else:
            bal[user] -= amount
            if l == 1:
                embed = discord.Embed(title=f"The flip was heads.", description=f"You lost {amount} <:Spambux:812017408260702248>.", color=discord.Color.blue())
            else:
                embed = discord.Embed(title=f"The flip was tails.", description=f"You lost {amount} <:Spambux:812017408260702248>.", color=discord.Color.blue())
            if user in lost:
                lost[user] += amount
            else:
                lost[user] = amount
            await ctx.send(embed=embed)
        with open('bal.json', 'w+') as i:
            json.dump(bal, i)
        with open('won.json', 'w+') as w:
            json.dump(won, w)
        with open('lost.json', 'w+') as xz:
            json.dump(lost, xz)
    else:
        if amount <= 0:
            await ctx.send('That is not a valid value!')
        elif call not in ['h', 'heads', 't', 'tails']:
            await ctx.send('That\'s an invalid call!')
        else:
            await ctx.send('You cannot afford this gamble!')
        

if os.path.exists('tickets.json'):
   with open('tickets.json', 'r') as zozo:
       ticket = json.load(zozo)
else:
   ticket = {}

if os.path.exists('r.json'):
   with open('r.json', 'r') as zozo:
       rated = json.load(zozo)
else:
   rated = {}

@client.command()
async def rate(ctx, stars : int, *, rating):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(ctx.author.id)
    await ctx.channel.purge(limit=1)
    channel = client.get_channel(770686661868650546)
    user = ctx.author.id
    if user in rated:
        await ctx.send('You already reviewed this place!')
    else:
        if stars > 5 or stars < 1:
            await ctx.send('Invalid rating')
        else:
            q = ''
            k = stars
            while k != 0:
                q += '⭐'
                k -= 1
            embed = discord.Embed(title=q, description=rating, color=discord.Color.red())
            embed.set_footer(text=ctx.author.name)
            msg = await channel.send(embed=embed)
            await msg.add_reaction('⬆️')
            await msg.add_reaction('⬇️')
            rated.append(user)
            with open('r.json', 'w+') as i:
                json.dump(rated, i)
            if user in bal and stars == 5:
                await ctx.author.send('Thank you for rating! You get 500 <:Spambux:812017408260702248>!')
                bal[user] += 500
            elif user not in bal and stars == 5:
                await ctx.author.send('Thank you for rating! You got 500 <:Spambux:812017408260702248>!')
                bal[user] = 500
            else:
                await ctx.author.send('Thank you for rating')
            with open('bal.json', 'w+') as i:
                json.dump(bal, i)

# cticket : 20 lticket : 25 rticket: 50 dticket: 200 tticket: 1000
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

@client.command()
async def buy(ctx, num : int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(ctx.author.id)
    user1 = ctx.author.id
    if user in leader:
        owner = client.get_user(468476776104853505)
        if ticket["cticket"] != 0 and num == 1 and user in bal and bal[user] >= 5:
            bal[user] -= 5
            ticket["cticket"] -= 1
            leader[user] += 5
            await ctx.send(f'{ctx.author.mention} You bought a lottery ticket for 5 <:Spambux:812017408260702248>! Be sure to tune in Sunday for the drawing!')
            cticket.append(user1)
            with open('cticket.json', 'w+') as i:
                json.dump(cticket, i)
        elif ticket["lticket"] != 0 and num == 2 and user in bal and bal[user] >= 20:
            bal[user] -= 20
            ticket["lticket"] -= 1
            leader[user] += 20
            await ctx.send(f'{ctx.author.mention} You bought a lottery ticket for 20 <:Spambux:812017408260702248>! Be sure to tune in Sunday for the drawing!')
            lticket.append(user1)
            with open('lticket.json', 'w+') as i:
                json.dump(lticket, i)
        elif ticket["rticket"] != 0 and num == 3 and user in bal and bal[user] >= 50:
            bal[user] -= 50
            ticket["rticket"] -= 1
            leader[user] += 50
            await ctx.send(f'{ctx.author.mention} You bought a lottery ticket for 50 <:Spambux:812017408260702248>! Be sure to tune in Sunday for the drawing!')
            rticket.append(user1)
            with open('rticket.json', 'w+') as i:
                json.dump(rticket, i)
        elif ticket["dticket"] != 0 and num == 4 and user in bal and bal[user] >= 100:
            bal[user] -= 100
            ticket["dticket"] -= 1
            leader[user] += 100
            await ctx.send(f'{ctx.author.mention} You bought a lottery ticket for 100 <:Spambux:812017408260702248>! Be sure to tune in Sunday for the drawing!')
            dticket.append(user1)
            with open('dticket.json', 'w+') as i:
                json.dump(dticket, i)
        elif ticket["tticket"] != 0 and num == 5 and user in bal and bal[user] >= 500:
            bal[user] -= 500
            ticket["tticket"] -= 1
            leader[user] += 500
            await ctx.send(f'{ctx.author.mention} You bought a lottery ticket for 500 <:Spambux:812017408260702248>! Be sure to tune in Sunday for the drawing!')
            tticket.append(user1)
            with open('tticket.json', 'w+') as i:
                json.dump(tticket, i)
        else:
            if num > 5:
                await ctx.send('That\'s an invalid lottery ticket')
            elif bal[user] < 5 or bal[user] < 20 or bal[user] < 50 or bal[user] < 100 or bal[user] < 500:
                await ctx.send(f'{ctx.author.send} You can\'t afford that!')
    else:
        leader[user] = 0
        await ctx.send('An error occured, please try again')
    with open('tickets.json', 'w+') as fcccc:
        json.dump(ticket, fcccc)
    with open('bal.json','w+') as b:
        json.dump(bal, b)
    with open('leader.json', 'w+') as k:
        json.dump(leader, k)
    with open('spent.json', 'w+') as mm:
        json.dump(leader, mm)


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

@client.command()
async def invite(ctx):
    async with ctx.typing():
       pass
    await ctx.send('https://discord.gg/AkYyFy5')

@client.command()
async def lottery(ctx):
    async with ctx.typing():
       pass
    with open('tickets.json', 'r') as file:
        ticket = json.load(file)
        embed = discord.Embed(title="Spam Shop Lottery", description="Want to get risky? Buy a ticket! Drawings are every Sunday. Winners will be announced in the #announcements channel. Buy a ticket by doing `!buy 1`", color=discord.Color.blue())
        embed.add_field(name="`1` 5 <:Spambux:812017408260702248>", value=f"5% chance of winning per ticket. {ticket['cticket']} more tickets avaliable. Prize is 100 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name='`2` 20 <:Spambux:812017408260702248>', value=f'4% chance of winning per ticket. {ticket["lticket"]} more tickets avaliable. Prize is 500 <:Spambux:812017408260702248>.', inline=False)
        embed.add_field(name="`3` 50 <:Spambux:812017408260702248>", value=f"2% chance of winning per ticket. {ticket['rticket']} more tickets avaliable. Prize is 750 <:Spambux:812017408260702248>.", inline=False)
        embed.add_field(name="`4` 100 <:Spambux:812017408260702248>", value=f"0.5% chance of winning per ticket. {ticket['dticket']} more tickets avaliable. Prize is 1,500 <:Spambux:812017408260702248>.", inline=False)
        embed.add_field(name="`5` 500 <:Spambux:812017408260702248>", value=f"0.1% chance of winning per ticket. {ticket['tticket']} more tickets avaliable. Prize is 75,000 <:Spambux:812017408260702248>.", inline=False)
        await ctx.send(embed=embed)

if os.path.exists('leader.json'):
   with open('leader.json', 'r') as file:
       leader = json.load(file)
else:
   leader = {}

@client.command()
async def lbreset(ctx):
    if ctx.author.id == 468476776104853505:
        leader.clear()
        with open('leader.json', 'w') as i:
            json.dump(leader, i)
        await ctx.send('reset')
    else:
        pass

@client.command(aliases=['lb', "leeberdord"])
async def leaderboard(ctx):
    async with ctx.typing():
       pass
    if ctx.channel.id == 767148961784922152:
        await ctx.send('That command is not allowed here!')
    else:
        user = str(ctx.author.id)
        x = {k: v for k, v in sorted(leader.items(), key=lambda leader: leader[1], reverse=True)}
        q = ''    
        z = 1
        for a in x:
            aa = await client.fetch_user(int(a))
            q += f'__{aa.name}__: {x[a]} <:Spambux:812017408260702248>\n'
            if z == 5:
                break
            else:
                z += 1
        embed = discord.Embed(title="Leaderboard", description=f"{q}", color=discord.Color.blue())
        if user not in leader:
            embed.add_field(name="You have spent:", value="0 <:Spambux:812017408260702248>", inline=False)
        else:
            embed.add_field(name="You have spent:", value=str(leader[user]) +" <:Spambux:812017408260702248>", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await ctx.send(embed=embed)



if os.path.exists('level.json'):
    with open('level.json', 'r') as file:
        level = json.load(file)
else:
    level = {} 

@client.command()
async def rank(ctx, *, member: discord.Member=None):
    if member is None:
        user = str(ctx.author.id)
        if user in level and 'xp' in level[user] and 'final_xp' in level[user] and 'level' in level[user]:
            xp = level[user]['xp']
            final_xp = level[user]['final_xp']
            fract = xp/final_xp
            progress = round(fract * 10)
            if progress >= 1:
                progressBar = '<:CompleteBlockBeginning:816753157198577744>'
            else:
                progressBar = '<:IncompleteBlockBeginning:816779212131794995>'
            incomplete = 9
            for i in range(0, progress-1):
                progressBar += '<:CompleteBlockMiddle:816753798306857002>'
                incomplete -= 1
            for I in range(0, incomplete-1):
                progressBar += '<:IncompleteBlockMiddle:816753597269803018>'
            if progress == 10:
                progressBar += '<:CompleteBlockEnding:816753157191368704>'
            else: 
                progressBar += '<:IncompleteBlockEnding:816753157039718463>'
            embed = discord.Embed(title=f"Level {(level[user]['level'])}", description=f"{xp}/{final_xp} xp\n{progressBar}", color=discord.Color.blue())
            embed.set_footer(text=str(ctx.author))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Level 1", description="0/10 xp\n<:IncompleteBlockBeginning:816779212131794995><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockEnding:816753157039718463>", color=discord.Color.blue())
            embed.set_footer(text=str(ctx.author))
            await ctx.send(embed=embed)
            level[user] = {}
            level[user]['xp'] = 0
            level[user]['final_xp'] = 10
            level[user]['level'] = 1
            with open('level.json', 'w+') as po:
                json.dump(level, po)
    else:
        user = str(member.id)
        if user in level and 'xp' in level[user] and 'final_xp' in level[user] and 'level' in level[user]:
            xp = level[user]['xp']
            final_xp = level[user]['final_xp']
            fract = xp/final_xp
            progress = round(fract * 10)
            if progress >= 1:
                progressBar = '<:CompleteBlockBeginning:816753157198577744>'
            else:
                progressBar = '<:IncompleteBlockBeginning:816779212131794995>'
            incomplete = 9
            for i in range(0, progress-1):
                progressBar += '<:CompleteBlockMiddle:816753798306857002>'
                incomplete -= 1
            for I in range(0, incomplete-1):
                progressBar += '<:IncompleteBlockMiddle:816753597269803018>'
            if progress == 10:
                progressBar += '<:CompleteBlockEnding:816753157191368704>'
            else: 
                progressBar += '<:IncompleteBlockEnding:816753157039718463>'
            embed = discord.Embed(title=f"Level {(level[user]['level'])}", description=f"{xp}/{final_xp} xp\n{progressBar}", color=discord.Color.blue())
            embed.set_footer(text=str(member))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Level 1", description="0/10 xp\n<:IncompleteBlockBeginning:816779212131794995><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockMiddle:816753597269803018><:IncompleteBlockEnding:816753157039718463>", color=discord.Color.blue())
            embed.set_footer(text=str(member))
            await ctx.send(embed=embed)
            level[user] = {}
            level[user]['xp'] = 0
            level[user]['final_xp'] = 10
            level[user]['level'] = 1
            with open('level.json', 'w+') as po:
                json.dump(level, po)


# Tax
@client.event
async def on_message(message):
    await client.process_commands(message)
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    send = message.channel.send
    if message.guild.id == 733392111130640446:

        if 'https://discord.gg/' in message.content.lower() or 'join my server' in message.content.lower():
            if message.author.id == 468476776104853505:
                pass
            else:
                await message.channel.purge(limit=1)
                user = await client.fetch_user(468476776104853505)
                await user.send(f'{message.author} has advertised')
                await send('Restricted Message')
        
        user = str(message.author.id)
        if message.author.id != 720856650583375873 and user in level and 'xp' in level[user] and 'final_xp' in level[user] and 'level' in level[user]:
            level[user]["xp"] += random.choice([0, 0, 2, 0, 0, 1, 0, 0, 3])
            with open("level.json", "w+") as I:
                json.dump(level, I)
            if level[user]['xp'] >= level[user]["final_xp"]:
                level[user]['xp'] -= level[user]['final_xp']
                level[user]['level'] += 1
                level[user]['final_xp'] *= 2 
                with open("level.json", "w+") as I:
                    json.dump(level, I)
                if level[user]['level'] % 5 == 0:
                    await send(f":tada: Congratulations {message.author.mention}, you advanced to level {level[user]['level']}! You get {level[user]['level']*500} <:Spambux:812017408260702248>!")
                    if os.path.exists('bal.json'):
                        with open('bal.json', 'r') as file:
                            bal = json.load(file)
                    else:
                        bal = {}
                    if user in bal:
                        bal[user] += level[user]['level'] * 500
                        with open('bal.json', 'w+') as ua:
                            json.dump(bal, ua)
                    else:
                        bal[user] = level[user]['level'] * 500
                        with open('bal.json', 'w+') as ue:
                            json.dump(bal, ue)
                    if level[user]['level'] % 10 == 0:
                        userr = message.author
                        role = get(message.guild.roles, name=f"Level {level[user]['level']}")
                    else:
                        pass
                else:
                    await send(f":tada: Congratulations {message.author.mention}, you advanced to level {level[user]['level']}!")
            else:
                pass
        else:
            level[user] = {}
            level[user]['final_xp'] = 10
            level[user]['xp'] = 0
            level[user]['level'] = 1
            with open('level.json', 'w+') as op:
                json.dump(level, op)
        

            cc = random.randint(1, 20)
            if cc == 5:
                nmn = random.randint(1, 20)
                await message.channel.send(f'**{nmn} <:Spambux:812017408260702248>** have been found! Type "claim" to claim it!')
                coinog = True
                while coinog:
                    def check(m):
                        return m.content == "claim" and m.channel == message.channel
                    coinpc = await client.wait_for('message', check=check)
                    await message.channel.send(f'{coinpc.author.mention} You got {nmn} <:Spambux:812017408260702248>!')
                    coinog = False
                    break
                
                user = str(coinpc.author.id)
                if user in bal:
                    bal[user] += nmn
                else:
                    bal[user] = nmn
                with open('bal.json', 'w+') as i:
                    json.dump(bal, i)


# Clear Messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send('I have cleared !' +str(amount) + ' messages!!')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

class Item:
    def __init__(self, price, pic, name):
        self.price = price
        self.pic = pic
        self.name = name

        
class MyMenu(menus.Menu):

    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed(title="Menu", description="`1` Chinese\n`2` American\n`3` Italian\n`4` Ice Cream\n`5` Pope Tarts\n`6` Drinks\n`7` Other", color=3447003)
        embed.set_footer(text='And of course we have spam (25 Spambux) too!')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        return await channel.send(embed=embed)

    @menus.button('🏛️')
    async def on_home(self, payload):
        embed = discord.Embed(title="Menu", description="`1` Chinese\n`2` American\n`3` Italian\n`4` Ice Cream\n`5` Pope Tarts\n`6` Drinks\n`7` Other", color=3447003)
        embed.set_footer(text='And of course we have spam (250 <:Spambux:812017408260702248>) too!')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        return await self.message.edit(embed=embed)
    
    @menus.button('1⃣')
    async def on_one(self, payload):
        embed = discord.Embed(title="Chinese/Taiwanese Food", description="Here is the list of Chinese Foods.", color=discord.Color.blue())
        embed.add_field(name="Ramen", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Chinese Noodle Stirfry", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Fried Rice", value="600 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Spicy Tofu", value="450 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Hot Pot", value="6000 <:Spambux:812017408260702248> (Do `!hotpot` for more info)", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)
        
    @menus.button('2⃣')
    async def on_two(self, payload):
        embed = discord.Embed(title="American Food", description="Here is the list of American Foods.", color=discord.Color.blue())
        embed.add_field(name="Cheeseburger", value="450 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Caesar Salad", value="550 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Hot Dog", value="350 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Pizza", value="500 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Fries", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)
        
    @menus.button('3⃣')
    async def on_three(self, payload):
        embed = discord.Embed(title="Italian Food", description="Here is the list of Italian Foods.", color=discord.Color.blue())
        embed.add_field(name="Pizza", value="500 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Spaghetti", value="500 <:Spambux:812017408260702248>", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)
        
    @menus.button('4⃣')
    async def on_four(self, payload):
        embed = discord.Embed(title="Ice Creams", description="Here is the list of Ice Creams. To order, write ic at the end of the order. e.g. !order mango ic", color=discord.Color.blue())
        embed.add_field(name="Vanilla", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Chocolate", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Strawberry", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Mango", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Pistachio", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Matcha", value="400 <:Spambux:812017408260702248>", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)

    @menus.button('5⃣')
    async def on_five(self, payload):
        embed = discord.Embed(title="Pope Tarts", description="Here are the Pope Tarts, try to find the Pope on each package. Special thanks to Smiles for helping me with the images.", color=discord.Color.blue())
        embed.add_field(name="Pope Tarts", value="300 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Asphalt Pope Tarts", value="300 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Elmer's Glue Pope Tarts", value="300 <:Spambux:812017408260702248> (order by doing !order elmers pope tarts)", inline=False)
        embed.add_field(name="Pope Tarts Just the Crust", value="300 <:Spambux:812017408260702248> (order by doing !order crust pope tarts)", inline=False)
        embed.add_field(name="Water Pope Tarts", value="300 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Pope Tarts Floor Food", value="300 <:Spambux:812017408260702248> (order by doing !order floor pope tarts)", inline=False)
        embed.add_field(name="Pope Tarts Ranch Dressing", value="300 <:Spambux:812017408260702248> (order by doing !order ranch pope tarts)", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)

    @menus.button('6⃣')
    async def on_six(self, payload):
        embed = discord.Embed(title="Drinks", description="Here are the drinks", color=discord.Color.blue())
        embed.add_field(name="Chocolate Milk", value="300 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Latte", value="400 <:Spambux:812017408260702248>", inline=False)
        await self.message.edit(embed=embed)


    @menus.button('7️⃣')
    async def on_seven(self, payload):
        embed = discord.Embed(title="Other", description="Here are the other foods", color=discord.Color.blue())
        embed.add_field(name="Potato", value="43 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Yubari Melon", value="800 <:Spambux:812017408260702248>", inline=False)
        embed.add_field(name="Turkey", value="70 <:Spambux:812017408260702248>", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721167603959201792/769350206143594556/spamshop.png")
        await self.message.edit(embed=embed)

    @menus.button('⏹️')
    async def on_stop(self, payload):
        self.stop()

@client.command()
async def menu(ctx):
    async with ctx.typing():
       pass
    m = MyMenu()
    await m.start(ctx)

@client.command()
async def hotpot(ctx):
    async with ctx.typing():
       pass
    embed = discord.Embed(title="Hot Pot", description="A Hot Pot consists of 4 parts and a topping. Do `!order hotpot`", color=discord.Color.blue())
    embed.add_field(name="Meat", value="Pork\nBeef\nMutton", inline=True)
    embed.add_field(name="Vegetables", value="Napa Cabbage\nParsley\nRaddish", inline=True)
    embed.add_field(name="Seafood", value="Fish\nShrimp\nSeaweed", inline=True)
    embed.add_field(name="Variety", value="Taiwanese Meatballs\nShrimpball\nFish Ball\nTampura", inline=True)
    embed.add_field(name="Toppings", value="Spring Onions\nCilantro\nPeanut Powder\nSoy Sauce", inline=True)
    await ctx.send(embed=embed)
    
        
spam_pics = ['https://images2.minutemediacdn.com/image/upload/c_crop,h_1576,w_2800,x_0,y_52/f_auto,q_auto,w_1100/v1554931909/shape/mentalfloss/20997-istock-471531747.jpg', 'https://cdn.vox-cdn.com/thumbor/UO1hhAGb7ea5G-MuC43l1Sxx9Rw=/0x0:2282x1712/1200x675/filters:focal(0x0:2282x1712)/cdn.vox-cdn.com/uploads/chorus_image/image/50821489/spam-wall.0.0.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT1O6mvAY7DJRy5xqz4kRbfv0ji0mL2XcEneg&usqp=CAU']
spam = Item(250, random.choice(spam_pics), 'spam')
pizza = Item(500, 'https://www.vvsupremo.com/wp-content/uploads/2018/05/Pepperoni-Pizza-1.jpg', 'pizza')
ramen = Item(400, 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190208-delish-ramen-horizontal-093-1550096715.jpg?crop=1xw:0.7496251874062968xh;center,top&resize=1200:*', 'ramen')
chineseNoodles = Item(400, 'https://www.mamalovesfood.com/wp-content/uploads/2019/08/STIR-FRY-NOODLES-7.jpg', 'chinese noodle stirfry')
cheeseBurger = Item(450, 'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/recipes/perfect_cheeseburger_recipe/650x350_perfect_cheeseburger_recipe.jpg', 'cheeseburger')
friedRice = Item(600, 'https://i2.wp.com/lifemadesimplebakes.com/wp-content/uploads/2018/04/Ham-Fried-Rice.jpg', 'fried rice')
caesarSalad = Item(550, 'https://www.cookingclassy.com/wp-content/uploads/2018/06/caesar-salad-3-500x375.jpg', 'caesar salad')
hotDog = Item(350, random.choice(['https://food.fnr.sndimg.com/content/dam/images/food/fullset/2018/8/7/0/FNM_090118-Barbecue-Hot-Dog_s4x3.jpg.rend.hgtvcom.616.462.suffix/1533665468931.jpeg', 'https://www.shoreupdate.com/wp-content/uploads/2014/09/images.gif']), 'hot dog')
popeTart = Item(300, 'https://i.redd.it/bwhm480hlg031.png', 'pope tarts')
fries = Item(400, 'https://www.corriecooks.com/wp-content/uploads/2018/10/Instant-Pot-French-Fries-new.jpg', 'fries')
vanillaIC = Item(400, 'https://www.kingarthurflour.com/sites/default/files/styles/featured_image/public/recipe_legacy/4163-3-large.jpg?itok=ztpZXNRg', 'vanilla ic')
chocolateIC = Item(400, 'https://joyfoodsunshine.com/wp-content/uploads/2020/06/homemade-chocolate-ice-cream-recipe-7.jpg', 'chocolate ic')
mangoIC = Item(400, 'https://lovingitvegan.com/wp-content/uploads/2018/01/Vegan-Mango-Ice-Cream-8.jpg', 'mango ic')
strawberryIC = Item(400, 'https://bakingamoment.com/wp-content/uploads/2018/06/IMG_8185-homemade-strawberry-ice-cream-square.jpg', 'strawberry ic')
asphaltPopeTart = Item(300, 'https://cdn.discordapp.com/attachments/721501784501387264/734197839697281085/unknown.png', 'asphalt pope tarts')
elmersPopeTart = Item(300, "https://cdn.discordapp.com/attachments/721501784501387264/734198614695608421/unknown.png", 'elmers pope tarts')          
crustPopeTart = Item(300, 'https://cdn.discordapp.com/attachments/721501784501387264/734249647563866203/unknown.png', 'crust pope tarts')
pistachioIC = Item(400, 'https://assets.epicurious.com/photos/5747b4a47d5155b145d8d607/2:1/w_1260%2Ch_630/shutterstock_303021722.jpg', 'pistachio ic')
matchaIC = Item(400, 'https://www.rotinrice.com/wp-content/uploads/2011/08/MatchaIceCream-1-680x350.jpg', 'matcha ic')
waterPopeTart = Item(300, 'https://cdn.discordapp.com/attachments/721501784501387264/734252962829959198/unknown.png', 'water pope tarts')
spicyTofu = Item(450, "https://simpleveganblog.com/wp-content/uploads/2018/01/Korean-style-spicy-tofu-3.jpg", 'spicy tofu')
potato = Item(430, 'https://cdn.discordapp.com/attachments/730177469768007680/768282370365063178/unknown.png', 'potato')
floorPopeTart = Item(300, 'https://media.discordapp.net/attachments/721501784501387264/734964442646970438/unknown.png', 'floor pope tarts')
ranchPopeTart = Item(300, 'https://cdn.discordapp.com/attachments/721501784501387264/734966826223796235/unknown.png', 'ranch pope tarts')
spaghetti = Item(500, 'https://c.ndtvimg.com/2020-01/n7thfo2o_spaghetti_625x300_28_January_20.jpg', 'spaghetti')
yubariMelon = Item(8000, 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/03/27/12/cantaloupe-melons.jpg?width=982&height=726', 'yubari melon')
turkey = Item(700, 'https://tastesbetterfromscratch.com/wp-content/uploads/2017/07/Easy-No-Fuss-Thanksgiving-Turkey-14.jpg', 'turkey')
chocolateMilk = Item(300,"https://cdn.discordapp.com/attachments/721501784501387264/785637261030850630/Screen_Shot_2020-12-07_at_2.34.37_PM.png", "chocolate milk")
latte= Item(400, "https://cdn.discordapp.com/attachments/730177469768007680/783503766850502656/unknown.png", "latte")

orders = [
    'ranch pope tarts',
    'floor pope tarts',
    'potato',
    'spicy tofu',
    'water pope tarts',
    'matcha ic',
    'pistachio ic',
    'crust pope tarts',
    'elmers pope tarts',
    'asphalt pope tarts',
    'strawberry ic',
    'mango ic',
    'chocolate ic',
    'vanilla ic',
    'fries',
    'pope tarts',
    'hot dog',
    'caesar salad',
    'fried rice',
    'cheeseburger',
    'chinese noodles stirfry',
    'ramen',
    'pizza',
    'spam',
    'spaghetti',
    'yubari melon',
    'turkey',
    'hot pot',
    "chocolate milk",
    "latte"
    ]
        
# order
@client.command(aliases=['o'])
async def order(ctx, *, food : str):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if ctx.channel.id == 767148961784922152 or ctx.channel.id == 771854973578510386 or ctx.channel.id == 704515917773537365:
        user = str(ctx.author.id)
        if user in leader:
            if str(food) == pizza.name and user in bal and bal[user] >= pizza.price:
                bal[user] -= pizza.price
                leader[user] += pizza.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your pizza: {pizza.pic}')

            elif str(food) == chocolateMilk.name and user in bal and bal[user] >= chocolateMilk.price:
                bal[user] -= chocolateMilk.price
                leader[user] += chocolateMilk.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Chocolate Milk: {chocolateMilk.pic}')

            elif str(food) == latte.name and user in bal and bal[user] >= latte.price:
                bal[user] -= latte.price
                leader[user] += latte.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Latte: {latte.pic}')

            elif str(food) == yubariMelon.name and user in bal and bal[user] >= yubariMelon.price:
                bal[user] -= yubariMelon.price
                leader[user] += yubariMelon.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Yubari Melon: {yubariMelon.pic}')

            elif str(food) == 'hot pot' and user in bal and bal[user] >= 600:
                await ctx.send('What type of meat would you like. (Type integer) ```1 Pork\n2 Beef\n3 Mutton```')
                meatc = await client.wait_for('message', check=lambda message: message.author == ctx.author)
                if meatc == 2:
                    bottomRight = '<:Beef:774435020613877770>'
                elif meatc == 1:
                    bottomRight = '<:Pork:774435040628703242>'
                else:
                    bottomRight = '<:Mutton:774435031832592414>'
                await ctx.send('What vegetable would you like? (Type integer) ```1 Napa Cabbage\n2 Raddish\n3 Parsley```')
                vegiec: int = await client.wait_for('message', check=lambda message: message.author == ctx.author)
                if vegiec == 2:
                    topLeft = '<:Raddish:774412666276937798>'
                elif vegiec == 1:
                    topLeft = '<:NapaCabbage:774412642315403274>'
                else:
                    topLeft = '<:Parsley:774412655171338280>'
                await ctx.send('What variety would you like? (Type integer) ```1 Taiwanese Meatnall\n2 Shrimpball\n3 Tampura\n4 Fishball```')
                varietyc: int = await client.wait_for('message', check=lambda message: message.author == ctx.author)
                if varietyc == 2:
                    bottomLeft = '<:ShrimpBall:774435002393952296>'
                elif varietyc == 1:
                    bottomLeft = '<:TaiwaneseMeatball:774412812620922890>'
                elif varietyc == 3:
                    bottomLeft = '<:Tampura:774434962643746836>'
                else:
                    bottomLeft = '<:FishBall:774434988207898634>'
                await ctx.send('What vegetable would you like? (Type integer) ```1 Fish\n2 Shrimp\n3 Seaweed```')
                seac: int = await client.wait_for('message', check=lambda message: message.author == ctx.author)
                if seac == 2:
                    topRight = '<:Shrimp:774435151241281628> '
                elif seac == 1:
                    topRight = '<:Fish:774412690017878037>'
                else:
                    topRight = '<:Seaweed:774435141027758103>'
                await ctx.send('What topping would you like? (Type integer) ```1 Spring Onion\n2 Peanut Powder\n3 Soy Sauce\n4 Cilantro```')
                varietyc: int = await client.wait_for('message', check=lambda message: message.author == ctx.author)
                if varietyc == 2:
                    topping = '<:PeanutPowder:774808721363697704>'
                elif varietyc == 1:
                    topping = '<:SpringOnions:774808855094755378>'
                elif varietyc == 3:
                    topping = '<:SoySauce:774808846156955659>'
                else:
                    topping = '<:Cilantro:774808838233784381>'
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(topping)
                await ctx.author.send(f'{topLeft}{topRight}\n{bottomLeft}{bottomRight}')
                await ctx.author.send('https://cdn.discordapp.com/attachments/704515917773537365/774118799473508392/HuoLu.png')
                bal[user] -= 600
                leader[user] += 600
                

            elif str(food) == turkey.name and user in bal and bal[user] >= turkey.price:
                bal[user] -= turkey.price
                leader[user] += turkey.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Turkey: {turkey.pic}')
                
            elif str(food) == spam.name and user in bal and bal[user] >= spam.price:
                bal[user] -= spam.price
                leader[user] += spam.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your spam: {spam.pic}')
                
            elif str(food) == ramen.name and user in bal and bal[user] >= ramen.price:
                bal[user] -= ramen.price
                leader[user] += ramen.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your ramen: {ramen.pic}')
            
            elif str(food) == chineseNoodles.name and user in bal and bal[user] >= chineseNoodles.price:
                bal[user] -= chineseNoodles.price
                leader[user] += chineseNoodles.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Chinese Noodles Stirfry: {chineseNoodles.pic}')

            elif str(food) == cheeseBurger.name and user in bal and bal[user] >= cheeseBurger.price:
                bal[user] -= cheeseBurger.price
                leader[user] += cheeseBurger.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Cheeseburger: {cheeseBurger.pic}')

            elif str(food) == friedRice.name and user in bal and bal[user] >= friedRice.price:
                bal[user] -= friedRice.price
                leader[user] += friedRice.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Fried Rice: {friedRice.pic}')

            elif str(food) == caesarSalad.name and user in bal and bal[user] >= caesarSalad.price:
                bal[user] -= caesarSalad.price
                leader[user] += caesarSalad.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Caesar Salad: {caesarSalad.pic}')

            elif str(food) == hotDog.name and user in bal and bal[user] >= hotDog.price:
                bal[user] -= hotDog.price
                leader[user] += hotDog.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Hot Dog: {hotDog.pic}')

            elif str(food) == popeTart.name and user in bal and bal[user] >= popeTart.price:
                bal[user] -= popeTart.price
                leader[user] += popeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts: {popeTart.pic}')

            elif str(food) == fries.name and user in bal and bal[user] >= fries.price:
                bal[user] -= fries.price
                leader[user] += fries.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your fries: {fries.pic}')

            elif str(food) == vanillaIC.name and user in bal and bal[user] >= vanillaIC.price:
                bal[user] -= vanillaIC.price
                leader[user] += vanillaIC.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Vanilla Ice Cream: {vanillaIC.pic}')

            elif str(food) == chocolateIC.name and user in bal and bal[user] >= chocolateIC.price:
                bal[user] -= chocolateIC.price
                leader[user] += chocolateIC.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Chocolate Ice Cream: {chocolateIC.pic}')

            elif str(food) == mangoIC.name and user in bal and bal[user] >= mangoIC.price:
                bal[user] -= mangoIC.price
                leader[user] += mangoIC.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Mango Ice Cream: {mangoIC.pic}')

            elif str(food) == strawberryIC.name and user in bal and bal[user] >= strawberryIC.price:
                bal[user] -= strawberryIC.price
                leader[user] += strawberryIC.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Strawberry Ice Cream: {strawberryIC.pic}')

            elif str(food) == asphaltPopeTart.name and user in bal and bal[user] >= asphaltPopeTart.price:
                bal[user] -= asphaltPopeTart.price
                leader[user] += asphaltPopeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts Asphalt : {asphaltPopeTart.pic}')

            elif str(food) == elmersPopeTart.name and user in bal and bal[user] >= elmersPopeTart.price:
                bal[user] -= elmersPopeTart.price
                leader[user] += elmersPopeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts Elmers Glue: {elmersPopeTart.pic}')

            elif str(food) == crustPopeTart.name and user in bal and bal[user] >= crustPopeTart.price:
                bal[user] -= crustPopeTart.price
                leader[user] += crustPopeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts Just the Crust: {crustPopeTart.pic}')

            elif str(food) == pistachioIC.name and user in bal and bal[user] >= pistachioIC.price:
                bal[user] -= pistachioIC.price
                leader[user] += pistachioIC.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pistachio Ice Cream: {pistachioIC.pic}')

            elif str(food) == matchaIC.name and user in bal and bal[user] >= matchaIC.price:
                bal[user] -= matchaIC.price
                leader[user] += matchaIC.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Matcha Ice Cream: {matchaIC.pic}')

            elif str(food) == waterPopeTart.name and user in bal and bal[user] >= waterPopeTart.price:
                bal[user] -= waterPopeTart.price
                leader[user] += waterPopeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts Water Flavor: {waterPopeTart.pic}')

            elif str(food) == spicyTofu.name and user in bal and bal[user] >= spicyTofu.price:
                bal[user] -= spicyTofu.price
                leader[user] += spicyTofu.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Spicy Tofu: {spicyTofu.pic}')

            elif str(food) == potato.name and user in bal and bal[user] >= potato.price:
                bal[user] -= potato.price
                leader[user] += potato.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Potato: {potato.pic}')

            elif str(food) == floorPopeTart.name and user in bal and bal[user] >= floorPopeTart.price:
                bal[user] -= floorPopeTart.price
                leader[user] += floorPopeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts Floor Food: {floorPopeTart.pic}')

            elif str(food) == ranchPopeTart.name and user in bal and bal[user] >= ranchPopeTart.price:
                bal[user] -= ranchPopeTart.price
                leader[user] += ranchPopeTart.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Pope Tarts Ranch Dressing: {ranchPopeTart.pic}')

            elif str(food) == spaghetti.name and user in bal and bal[user] >= spaghetti.price:
                bal[user] -= spaghetti.price
                leader[user] += spaghetti.price
                await ctx.send(f'{ctx.author.mention} Your food is on the way!')
                await ctx.author.send(f'Here is your Spaghetti: {spaghetti.pic}')
            
            else:
                if str(food) not in orders:
                    if 'food' in str(food) or 'Food' in str(food) or 'did' in str(food) or 'Did' in str(food):
                        await ctx.send('Please specify what food you want')
                        if bal[user] >= 10000:
                            bal[user] -= 10000
                        else:
                            bal[user] = 0
                    else:
                        await ctx.send(f'"{food}" isn\'t on the menu!')
                else:
                    await ctx.send('You can\'t afford that!')
        else:
            leader[user] = 0
            await ctx.send('An error occured, please try again')
        with open('bal.json', 'w+') as i:
            json.dump(bal, i)
        with open('leader.json', 'w+') as m:
            json.dump(leader, m)
        with open('spent.json', 'w+') as mm:
            json.dump(leader, mm)
    else:
        await ctx.send('That command is not allowed here!')

# Menu Suggestions
@client.command(aliases=['s'])
@commands.cooldown(1, 300, commands.BucketType.user)
async def suggest(ctx, *, food):
    async with ctx.typing():
       pass
    user = client.get_channel(817918302638178335)
    await ctx.channel.purge(limit=1)
    await ctx.author.send('Thank you for your suggestion!')
    embed = discord.Embed(title=str(ctx.author), description=food, color=discord.Color.blue())
    msg = await user.send(embed=embed)
    await msg.add_reaction('⬆️')
    await msg.add_reaction('⬇️')

# Speed (Ping)
@client.command(aliases=['ping'])
async def speed(ctx):
    async with ctx.typing():
       pass
    await ctx.send(f"Your food takes about {client.latency * 10000} milliseconds to deliver. Wow, that's fast!")


@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    message = await ctx.send(f'{ctx.author.mention} You got 1000 <:Spambux:812017408260702248>!')
    user = str(ctx.author.id)
    if user in bal:
        bal[user] += 1000
    else:
        bal[user] = 1000
    with open('bal.json', 'w+') as i:
        json.dump(bal, i)
    
            
if os.path.exists('secret.json'):
   with open('secret.json', 'r') as file:
       secret = json.load(file)
else:
   secret = []

@client.command()
async def reward(ctx, member : discord.Member, amount: int):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    if ctx.author.id == 468476776104853505:
        user = str(member.id)
        if user in bal:
            bal[user] += amount
        else:
            bal[user] = amount
        await ctx.send('rewarded')
        with open('bal.json', 'w+') as i:
            json.dump(bal, i)
    else:
        pass 


@client.command()
@commands.has_role("Member")
@commands.cooldown(1, 86400, commands.BucketType.user)
async def extra(ctx):
    async with ctx.typing():
       pass
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as file:
            bal = json.load(file)
    else:
        bal = {}
    user = str(ctx.author.id)
    money = random.randint(1000, 2000)
    await ctx.send(f'{ctx.author.mention} You got {money} <:Spambux:812017408260702248>!')
    bal[user] += money
    with open('bal.json', 'w+') as i:
        json.dump(bal, i)
    
@client.command()
async def profile(ctx, *, person: discord.Member=None):
    if os.path.exists('badge.json'):
        with open('badge.json', 'r') as file:
            badge = json.load(file)
    else:
        badge = {}
    if os.path.exists('bal.json'):
        with open('bal.json', 'r') as zozl:
            bal = json.load(zozl)
    else:
        bal = {}
    if person == None:
        user = str(ctx.author.id)
        if user not in lost:
            lost[user] = 0
        if user not in won:
            won[user] = 0
        if user not in spent:
            spent[user] = 0
        if user not in leader:
            leader[user] = 0
        if user not in bal:
            bal[user] = 0
        if user not in badge:
            b = ""
        else:
            b = ""
            for z in range(len(badge[user])):
                b += f"{badge[user][z]} "
        author = ctx.message.author
        pfp = author.avatar_url
        embed = discord.Embed(title=f"{ctx.author}", description=b, color=discord.Color.blue())
        embed.add_field(name="Amount Spent (all time)", value=spent[user], inline=False)
        embed.add_field(name="Amount Spent (this year)", value=leader[user], inline=False)
        embed.add_field(name="Balance", value=bal[user], inline=True)
        embed.add_field(name="Amount Won in Gambling", value=won[user], inline=False)
        embed.add_field(name="Amount Lost in Gambling", value=lost[user], inline=False)
        embed.set_thumbnail(url=pfp)
        await ctx.send(embed=embed)
    else:
        user = str(person.id)
        if user not in lost:
            lost[user] = 0
        if user not in won:
            won[user] = 0
        if user not in spent:
            spent[user] = 0
        if user not in leader:
            leader[user] = 0
        if user not in bal:
            bal[user] = 0
        if user not in badge:
            b = ""
        else:
            b = ""
            for z in range(len(badge[user])):
                b += f"{badge[user][z]} "
        pfp = person.avatar_url
        embed = discord.Embed(title=f"{person}", description=b, color=discord.Color.blue())
        embed.add_field(name="Amount Spent (all time)", value=spent[user], inline=False)
        embed.add_field(name="Amount Spent (this year)", value=leader[user], inline=False)
        embed.add_field(name="Balance", value=bal[user], inline=True)
        embed.add_field(name="Amount Won in Gambling", value=won[user], inline=False)
        embed.add_field(name="Amount Lost in Gambling", value=lost[user], inline=False)
        embed.set_thumbnail(url=pfp)
        await ctx.send(embed=embed)

client.run('')

import discord, json
import os, io, random, string
import colorama, time, datetime
from io import BytesIO
from dhooks import Webhook, Embed
from discord import Game, File
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord import Game
from colorama import Fore, init
colorama.init()

os.system("cls")

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
prefix = config.get("prefix")
RPC = config.get("RPC")
hook = Webhook(config.get("webhook"))
version = config.get("version")
rate = config.get("rate")
per = config.get("per")
t = BucketType.default

gen = commands.Bot(command_prefix=prefix)
gen.remove_command('help')


@gen.event
async def on_ready():
    print('Ready')
    print(f"{Fore.CYAN}Logged in as: {gen.user.name}{Fore.RESET}")
    print(f"{Fore.CYAN}ID of the Bot: {gen.user.id}{Fore.RESET}")
    print(f"{Fore.CYAN}Discord Version: {discord.__version__}{Fore.RESET}")
    print(f"{Fore.CYAN}Current RPC: {RPC}{Fore.RESET}")
    await gen.change_presence(status=discord.Status.online, activity=discord.Game(RPC))

@gen.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(title='Cooldown',description='{}'.format(error)))
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Are u sure do u type correctly the command?")
    if isinstance(error, commands.errors.NoPrivateMessage):
        await ctx.send("You cant generate on my DMs\n:x:")

@gen.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def stock(ctx):
    num_spotify = sum(1 for line in open('accounts/spotify.txt'))
    num_roblox = sum(1 for line in open('accounts/roblox.txt'))
    await ctx.send('--------------------------------------')
    await ctx.send('Current **Spotify** Stock: ' + str(num_spotify))
    await ctx.send('Current **Roblox** Stock: ' + str(num_roblox))
    await ctx.send('--------------------------------------')

@gen.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def spotify(ctx):
    account_service = "Spotify"
    with open('accounts/spotify.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('accounts/spotify.txt', 'w') as (s):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        s.write(line)
            break
        await ctx.author.send(f"**Service** ⟹〘 {account_service} 〙\n**Mail/User** ⟹ ||〘 {User} 〙||\n**Pass** ⟹ ||〘 {PassFixed} 〙||\n```> Para que la cuenta dure más por favor, no cambies la contraseña\n> To make the account last longer please do not change the password```")
        await ctx.send("Hey, I send u the acc")
        embed = Embed(description='Meh, im just logging the generator commands', color=0x5EF716, timestamp='now')
        image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/842199054674296862/291526360021211.png'
        embed.set_author(name='💣 Account Generated 💣')
        embed.add_field(name="**Who used the command**", value="```{}```".format(ctx.author), inline=True)
        embed.add_field(name='**Command Executed**', value='```spotify```', inline=True)
        embed.add_field(name="**Acc Type?**", value="```{}```".format(account_service), inline=True)
        embed.add_field(name="**Acc Mail/User?**", value="```{}```".format(User), inline=True)
        embed.add_field(name="**Acc Password?**", value="```{}```".format(PassFixed), inline=True)
        embed.add_field(name='**Channel?**', value='<#{}>'.format(ctx.channel.id), inline=True)
        embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
        embed.set_footer(text='Discord Generator Bot by Chirimoya | WebHook Log | Version: {}'.format(version))
        embed.set_thumbnail(image1)
        hook.send(embed=embed)

@gen.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def roblox(ctx):
    account_service = "Roblox"
    with open('accounts/roblox.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('accounts/roblox.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)
            break
        await ctx.author.send(f"**Service** ⟹〘 {account_service} 〙\n**Mail/User** ⟹ ||〘 {User} 〙||\n**Pass** ⟹ ||〘 {PassFixed} 〙||\n```> Para que la cuenta dure más por favor, no cambies la contraseña\n> To make the account last longer please do not change the password```")
        await ctx.send("Hey, I send u the acc")
        embed = Embed(description='Meh, im just logging the generator commands', color=0x5EF716, timestamp='now')
        image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/842199054674296862/291526360021211.png'
        embed.set_author(name='💣 Account Generated 💣')
        embed.add_field(name="**Who used the command**", value="```{}```".format(ctx.author), inline=True)
        embed.add_field(name='**Command Executed**', value='```spotify```', inline=True)
        embed.add_field(name="**Acc Type?**", value="```{}```".format(account_service), inline=True)
        embed.add_field(name="**Acc Mail/User?**", value="```{}```".format(User), inline=True)
        embed.add_field(name="**Acc Password?**", value="```{}```".format(PassFixed), inline=True)
        embed.add_field(name='**Channel?**', value='<#{}>'.format(ctx.channel.id), inline=True)
        embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
        embed.set_footer(text='Discord Generator Bot by Chirimoya | WebHook Log | Version: {}'.format(version))
        embed.set_thumbnail(image1)
        hook.send(embed=embed)

@gen.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def add_robloxalts(ctx, account=None):
    if account is None:
        embed = discord.Embed(title=f"The command is: ```{prefix}add_robloxalts [Account]```", colour=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        with open("accounts/roblox.txt", "a") as file:
            file.write(account + "\n")
            await ctx.send("Done")
            print(f"{Fore.MAGENTA}One accounts was puted in the Generator{Fore.RESET}")     

@gen.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def add_spotifyalts(ctx, account=None):
    if account is None:
        embed = discord.Embed(title=f"The command is: ```{prefix}add_spotifyalts [Account]```", colour=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        with open("accounts/spotify.txt", "a") as file:
            file.write(account + "\n")
            await ctx.send("Done")
            print(f"{Fore.MAGENTA}One accounts was puted in the Generator{Fore.RESET}")

gen.run(token)
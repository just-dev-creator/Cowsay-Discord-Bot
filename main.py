import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
import cowsay2

isTest = False
TOKEN = ""
with open("credentials.txt") as f:
    TOKEN = f.read()


# Command prefix isn't needed for any action!
client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, auto_register=True, auto_delete=True)


@client.event
async def on_ready():
    print("I have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="for cowsay help"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('cowsay'):
        cows = message.content.replace('cowsay ', '')
        if cows == "help":
            embed = discord.Embed(colour=discord.Colour(0x1c0b92),
                                  description="After the command, you need to fill in, what to say. ")

            embed.set_thumbnail(
                url="https://raw.githubusercontent.com/just-dev-creator/Cowsay-Discord-Bot/main/pic.png?token=AP7GUVD3CJSRLLXHSQ3XDGK74S6J4")
            embed.set_author(name="Cowsay", url="https://github.com/just-dev-creator/Cowsay-Discord-Bot/")
            embed.set_footer(text="just.dev")

            embed.add_field(name=":cow: ", value="cowsay ", inline=True)
            embed.add_field(name=":turtle: ", value="turtlesay", inline=True)
            embed.add_field(name=":turkey: ", value="turkeysay", inline=True)
            embed.add_field(name="🦖", value="stegosaurussay", inline=True)
            embed.add_field(name=":pig:  ", value="pigsay ", inline=True)
            embed.add_field(name=":milk:", value="milksay", inline=True)
            embed.add_field(name=":smiley_cat:", value="meowsay", inline=True)
            embed.add_field(name=":cat:", value="kittysay", inline=True)
            embed.add_field(name=":ghost:", value="ghostbusterssay", inline=True)
            embed.add_field(name=":chains:", value="daemonsay", inline=True)
            embed.add_field(name=":dragon:", value="dragonsay", inline=True)
            embed.add_field(name=":cheese:", value="cheesesay", inline=True)
            embed.add_field(name=":penguin:", value="tuxsay", inline=True)
            embed.add_field(name=":man:", value="beavissay", inline=True)

            await message.channel.send(
                content="Welcome to the cowsay Discord-Bot. Below, you can find a list of all command which you can use. ",
                embed=embed)
        else:
            try:
                await message.channel.send(cowsay2.cow(cows))
            except:
                await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('tuxsay'):
        cows = message.content.replace('tuxsay', '')
        try:
            await message.channel.send(cowsay2.tux(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('turtlesay'):
        cows = message.content.replace('turtlesay', '')
        try:
            await message.channel.send(cowsay2.turtle(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('turkeysay'):
        cows = message.content.replace('turkeysay', '')
        try:
            await message.channel.send(cowsay2.turkey(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('stimpysay'):
        cows = message.content.replace('stimpysay', '')
        try:
            await message.channel.send(cowsay2.stimpy(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('stegosaurussay'):
        cows = message.content.replace('stegosaurussay', '')
        try:
            await message.channel.send(cowsay2.stegosaurus(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('pigsay'):
        cows = message.content.replace('pigsay', '')
        try:
            await message.channel.send(cowsay2.pig(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('milksay'):
        cows = message.content.replace('milksay', '')
        try:
            await message.channel.send(cowsay2.milk(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('meowsay'):
        cows = message.content.replace('meowsay', '')
        try:
            await message.channel.send(cowsay2.meow(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('kittysay'):
        cows = message.content.replace('kittysay', '')
        try:
            await message.channel.send(cowsay2.kitty(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('ghostbusterssay'):
        cows = message.content.replace('ghostbusterssay', '')
        try:
            await message.channel.send(cowsay2.ghostbusters(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('daemonsay'):
        cows = message.content.replace('daemonsay', '')
        try:
            await message.channel.send(cowsay2.daemon(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('dragonsay'):
        cows = message.content.replace('dragonsay', '')
        try:
            await message.channel.send(cowsay2.dragon(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('beavissay'):
        cows = message.content.replace('beavissay', '')
        try:
            await message.channel.send(cowsay2.beavis(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
    elif message.content.startswith('cheesesay'):
        cows = message.content.replace('cheesesay', '')
        try:
            await message.channel.send(cowsay2.cheese(cows))
        except:
            await message.channel.send(cowsay2.cow("Sorry, too long (Discord error occured) "))
if isTest:
    guild_ids : list = [703266392295604254]
else:
    guild_ids : list = None

@slash.slash(name="cowsay", guild_ids=guild_ids, description="Let a cow say things", options=[{
    "name": "tosay",
    "description": "Specify what the cow says",
    "type": 3,
    "required": True
}])
async def _cowsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.cow(tosay))

@slash.slash(name="turtlesay", guild_ids=guild_ids, description="Let a turtle say things", options=[{
    "name": "tosay",
    "description": "Specify what the turtle says",
    "type": 3,
    "required": True
}])
async def _turtlesay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.turtle(tosay))

@slash.slash(name="turkeysay", guild_ids=guild_ids, description="Let a turkey say things", options=[{
    "name": "tosay",
    "description": "Specify what the turkey says",
    "type": 3,
    "required": True
}])
async def _turkeysay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.turkey(tosay))

@slash.slash(name="turtlesay", guild_ids=guild_ids, description="Let a turtle say things", options=[{
    "name": "tosay",
    "description": "Specify what the turtle says",
    "type": 3,
    "required": True}])
async def _turtlesay(ctx: SlashContext, tosay):
    tosay = cowsay2.turtle(tosay)
    if len(tosay) <= 2000:
        await ctx.send(content=tosay)


@slash.slash(name="stegosaurussay", guild_ids=guild_ids, description="Let a stegosaurus say things", options=[{
    "name": "tosay",
    "description": "Specify what the stegosaurus says",
    "type": 3,
    "required": True
}])
async def _stegosaurussay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.stegosaurus(tosay))

@slash.slash(name="pigsay", guild_ids=guild_ids, description="Let a pig say things", options=[{
    "name": "tosay",
    "description": "Specify what the pig says",
    "type": 3,
    "required": True
}])
async def _pigsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.pig(tosay))

@slash.slash(name="milksay", guild_ids=guild_ids, description="Let a milk say things", options=[{
    "name": "tosay",
    "description": "Specify what the milk says",
    "type": 3,
    "required": True
}])
async def _milksay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.milk(tosay))

@slash.slash(name="meowsay", guild_ids=guild_ids, description="Let a cat say things", options=[{
    "name": "tosay",
    "description": "Specify what the cat says",
    "type": 3,
    "required": True
}])
async def _meowsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.meow(tosay))

@slash.slash(name="kittysay", guild_ids=guild_ids, description="Let a cat say things", options=[{
    "name": "tosay",
    "description": "Specify what the cat says",
    "type": 3,
    "required": True
}])
async def _meowsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.kitty(tosay))

@slash.slash(name="ghostbusterssay", guild_ids=guild_ids, description="Let the ghostbusters logo say things", options=[{
    "name": "tosay",
    "description": "Specify what the ghostbusters logo says",
    "type": 3,
    "required": True
}])
async def _ghostbusterssay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.ghostbusters(tosay))

@slash.slash(name="daemonsay", guild_ids=guild_ids, description="Let a daemon say things", options=[{
    "name": "tosay",
    "description": "Specify what the daemon says",
    "type": 3,
    "required": True
}])
async def _daemonsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.daemon(tosay))

@slash.slash(name="dragonsay", guild_ids=guild_ids, description="Let a dragon say things", options=[{
    "name": "tosay",
    "description": "Specify what the dragon says",
    "type": 3,
    "required": True
}])
async def _dragonsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.dragon(tosay))

@slash.slash(name="cheesesay", guild_ids=guild_ids, description="Let a cheese say things", options=[{
    "name": "tosay",
    "description": "Specify what the cheese says",
    "type": 3,
    "required": True
}])
async def _cheesesay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.cheese(tosay))

@slash.slash(name="tuxsay", guild_ids=guild_ids, description="Let tux say things", options=[{
    "name": "tosay",
    "description": "Specify what tux says",
    "type": 3,
    "required": True
}])
async def _tuxsay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.tux(tosay))

@slash.slash(name="beavissay", guild_ids=guild_ids, description="Let beavis say things", options=[{
    "name": "tosay",
    "description": "Specify what beavis says",
    "type": 3,
    "required": True
}])
async def _beavissay(ctx: SlashContext, tosay):
    if len(tosay) <= 2000:
        await ctx.send(content=cowsay2.beavis(tosay))







client.run(TOKEN)

import discord
import cowsay2
import datetime
TOKEN = ""
with open("credentials.txt") as f:
    TOKEN = f.read()

client = discord.Client()
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
            await message.channel.send(cowsay2.cow(cows))
        # print("=====================================================")
        # print(cowsay_str)
    elif message.content.startswith('tuxsay'):
        cows = message.content.replace('tuxsay', '')
        await message.channel.send(cowsay2.tux(cows))
    elif message.content.startswith('turtlesay'):
        cows = message.content.replace('turtlesay', '')
        await message.channel.send(cowsay2.turtle(cows))
    elif message.content.startswith('turkeysay'):
        cows = message.content.replace('turkeysay', '')
        await message.channel.send(cowsay2.turkey(cows))
    elif message.content.startswith('stimpysay'):
        cows = message.content.replace('stimpysay', '')
        await message.channel.send(cowsay2.stimpy(cows))
        #stegosaurus
    elif message.content.startswith('stegosaurussay'):
        cows = message.content.replace('stegosaurussay', '')
        await message.channel.send(cowsay2.stegosaurus(cows))
    elif message.content.startswith('pigsay'):
        cows = message.content.replace('pigsay', '')
        await message.channel.send(cowsay2.pig(cows))
    elif message.content.startswith('milksay'):
        cows = message.content.replace('milksay', '')
        await message.channel.send(cowsay2.milk(cows))
    elif message.content.startswith('meowsay'):
        cows = message.content.replace('meowsay', '')
        await message.channel.send(cowsay2.meow(cows))
    elif message.content.startswith('kittysay'):
        cows = message.content.replace('kittysay', '')
        await message.channel.send(cowsay2.kitty(cows))
    elif message.content.startswith('ghostbusterssay'):
        cows = message.content.replace('ghostbusterssay', '')
        await message.channel.send(cowsay2.ghostbusters(cows))
    elif message.content.startswith('daemonsay'):
        cows = message.content.replace('daemonsay', '')
        await message.channel.send(cowsay2.daemon(cows))
    elif message.content.startswith('dragonsay'):
        cows = message.content.replace('dragonsay', '')
        await message.channel.send(cowsay2.dragon(cows))
    elif message.content.startswith('beavissay'):
        cows = message.content.replace('beavissay', '')
        await message.channel.send(cowsay2.beavis(cows))
    elif message.content.startswith('cheesesay'):
        cows = message.content.replace('cheesesay', '')
        await message.channel.send(cowsay2.cheese(cows))
        await message.channel.send(cowsay2.cheese(cows))
client.run(TOKEN)
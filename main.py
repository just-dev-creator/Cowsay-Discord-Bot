import discord
import cowsay2
TOKEN = ""
with open("credentials.txt") as f:
    TOKEN = f.read()

client = discord.Client()
@client.event
async def on_ready():
    print("I have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('cowsay'):
        cows = message.content.replace('cowsay ', '')
        if cows == "help":
            await message.channel.send("None help availeble yet. ")
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

client.run(TOKEN)
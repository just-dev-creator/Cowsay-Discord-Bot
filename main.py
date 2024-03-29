import discord
from discord import SlashCommand
import cowsay
from sys import argv
from os import environ
from os.path import exists

if exists("credentials.txt"):
    with open("credentials.txt") as f:
        TOKEN = f.read()

if "DISCORD_BOT_TOKEN" in environ:
    TOKEN = environ["DISCORD_BOT_TOKEN"]

is_test: bool = "-t" in argv or "--test" in argv
allow_text: bool = "-nt" not in argv and "--no-text" not in argv
client = discord.Bot()


# Append markdown characters for code block
def make_code_block(message: str) -> str:
    return "```" + message + "```"

# Get final message with code blocks
def get_ascii_image_for_discord(char_name: str, message: str) -> str:
    return make_code_block(cowsay.get_output_string(char_name=char_name, text=message).replace("`", "｀"))


@client.event
async def on_ready():
    # Print success message on startup
    print(f"Bot is ready as {client.user}")
    if is_test:
        print("Bot is running in testing mode. Please remove the --test flag if this is a production deployment!")
    # Should resolve as "listens to cowsay help"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="cowsay help"))


@client.event
async def on_message(message):
    if not allow_text:
        return

    to_send: str = None
    if message.author == client.user:
        # Return if we send the message
        return
    elif message.content.startswith('cowsay'):
        cows = message.content.replace('cowsay ', '')
        if cows == "help":
            embed = discord.Embed(colour=discord.Colour(0x1c0b92),
                                  description="After the command, you need to fill in, what to say. ")

            embed.set_thumbnail(
                url="https://raw.githubusercontent.com/just-dev-creator/Cowsay-Discord-Bot/main/pic.png?token"
                    "=AP7GUVD3CJSRLLXHSQ3XDGK74S6J4")
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
                content="Welcome to the cowsay Discord-Bot. Below, you can find a list of all command which you can "
                        "use. ",
                embed=embed)
        else:
            to_send = get_ascii_image_for_discord("cow", cows)
    elif message.content.startswith('tuxsay'):
        cows = message.content.replace('tuxsay', '')
        to_send = get_ascii_image_for_discord("tux", cows)
    elif message.content.startswith('turtlesay'):
        cows = message.content.replace('turtlesay', '')
        to_send = get_ascii_image_for_discord("turtle", cows)
    elif message.content.startswith('turkeysay'):
        cows = message.content.replace('turkeysay', '')
        to_send = get_ascii_image_for_discord("turkey", cows)
    elif message.content.startswith('stimpysay'):
        cows = message.content.replace('stimpysay', '')
        to_send = get_ascii_image_for_discord("stimpy", cows)
    elif message.content.startswith('stegosaurussay'):
        cows = message.content.replace('stegosaurussay', '')
        to_send = get_ascii_image_for_discord("stegosaurus", cows)
    elif message.content.startswith('pigsay'):
        cows = message.content.replace('pigsay', '')
        to_send = get_ascii_image_for_discord("pig", cows)
    elif message.content.startswith('milksay'):
        cows = message.content.replace('milksay', '')
        to_send = get_ascii_image_for_discord("milk", cows)
    elif message.content.startswith('meowsay'):
        cows = message.content.replace('meowsay', '')
        to_send = get_ascii_image_for_discord("meow", cows)
    elif message.content.startswith('kittysay'):
        cows = message.content.replace('kittysay', '')
        to_send = get_ascii_image_for_discord("kitty", cows)
    elif message.content.startswith('ghostbusterssay'):
        cows = message.content.replace('ghostbusterssay', '')
        to_send = get_ascii_image_for_discord("ghostbusters", cows)
    elif message.content.startswith('daemonsay'):
        cows = message.content.replace('daemonsay', '')
        to_send = get_ascii_image_for_discord("daemon", cows)
    elif message.content.startswith('dragonsay'):
        cows = message.content.replace('dragonsay', '')
        to_send = get_ascii_image_for_discord("dragon", cows)
    elif message.content.startswith('beavissay'):
        cows = message.content.replace('beavissay', '')
        to_send = get_ascii_image_for_discord("beavis", cows)
    elif message.content.startswith('cheesesay'):
        cows = message.content.replace('cheesesay', '')
        to_send = get_ascii_image_for_discord("cheese", cows)

    # Send predifined message if it exists
    if to_send is not None:
        try:
            await message.channel.send(to_send)
        except discord.errors.HTTPException:
            # If an error occurred, send an error message
            await message.channel.send(get_ascii_image_for_discord("cow", "Sorry, your message was too long. "))


if is_test:
    guild_ids: list = [703266392295604254] # 703266392295604254
else:
    guild_ids = None


async def get_message_or_error(ctx: SlashCommand, message: str, char_name: str):
    """
    React with error or message to a slash command
    """
    to_send: str = get_ascii_image_for_discord(message=message, char_name=char_name)
    if len(to_send) > 2000:
        await ctx.respond(get_ascii_image_for_discord("cow", "Sorry, your message was too long. "), ephemeral=True)
    else:
        await ctx.respond(to_send)


@client.slash_command(name="cowsay", guild_ids=guild_ids, description="Let a cow say things")
async def _cowsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the cow say?")):
    await get_message_or_error(ctx, tosay, "cow")


@client.slash_command(name="turkeysay", guild_ids=guild_ids, description="Let a turkey say things")
async def _turkeysay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the turkey say?")):
    await get_message_or_error(ctx, tosay, "turkey")


@client.slash_command(name="turtlesay", guild_ids=guild_ids, description="Let a turtle say things")
async def _turtlesay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the turtle say?")):
    await get_message_or_error(ctx, tosay, "turtle")


@client.slash_command(name="stegosaurussay", guild_ids=guild_ids, description="Let a stegosaurus say things")
async def _stegosaurussay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the stegosaurus say?")):
    await get_message_or_error(ctx, tosay, "stegosaurus")


@client.slash_command(name="pigsay", guild_ids=guild_ids, description="Let a pig say things")
async def _pigsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the pig say?")):
    await get_message_or_error(ctx, tosay, "pig")


@client.slash_command(name="milksay", guild_ids=guild_ids)
async def _milksay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the milk say?")):
    await get_message_or_error(ctx, tosay, "milk")


@client.slash_command(name="meowsay", guild_ids=guild_ids)
async def _meowsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the cat say?")):
    await get_message_or_error(ctx, tosay, "meow")


@client.slash_command(name="kittysay", guild_ids=guild_ids)
async def _meowsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the kitty say?")):
    await get_message_or_error(ctx, tosay, "kitty")


@client.slash_command(name="ghostbusterssay", guild_ids=guild_ids, description="Let the ghostbusters logo say things")
async def _ghostbusterssay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the ghostbusters logo say?")):
    await get_message_or_error(ctx, tosay, "ghostbusters")


@client.slash_command(name="daemonsay", guild_ids=guild_ids, description="Let a daemon say things")
async def _daemonsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the daemon say?")):
    await get_message_or_error(ctx, tosay, "daemon")


@client.slash_command(name="dragonsay", guild_ids=guild_ids, description="Let a dragon say things")
async def _dragonsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the dragon say?")):
    await get_message_or_error(ctx, tosay, "dragon")


@client.slash_command(name="cheesesay", guild_ids=guild_ids, description="Let a cheese say things")
async def _cheesesay(ctx: SlashCommand, tosay: discord.Option(str, description="What should the cheese say?")):
    await get_message_or_error(ctx, tosay, "cheese")

@client.slash_command(name="tuxsay", guild_ids=guild_ids, description="Let tux say things")
async def _tuxsay(ctx: SlashCommand, tosay: discord.Option(str, description="What should tux say?")):
    await get_message_or_error(ctx, tosay, "tux")


@client.slash_command(name="beavissay", guild_ids=guild_ids, description="Let beavis say things")
async def _beavissay(ctx: SlashCommand, tosay: discord.Option(str, description="What should beavis say?")):
    await get_message_or_error(ctx, tosay, "beavis")


# Start bot with given bot
client.run(TOKEN)

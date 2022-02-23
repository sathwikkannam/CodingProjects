import discord
from discord.ext import commands
from discord import ClientException
import random
import giphy_client
from giphy_client.rest import ApiException
import math
import os


TOKEN = os.getenv("DISCORD_KEY")
GIF_TOKEN = os.getenv("GIPHY_KEY")

client = commands.Bot(command_prefix="!")
gif_client = giphy_client.DefaultApi()

names_votes = []
votes_and_names = []


@client.event
async def on_ready():
    print("We logged in")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Floppa gamin"))


@client.command()
async def gif(ctx, *, arg="explosion"):
    try:
        q = str(arg)
        if arg == "KTH":
            q = "explosion"

        api_response = gif_client.gifs_search_get(GIF_TOKEN, q, limit=10, rating="R")
        await ctx.channel.send(f"You asked for {arg} and here it is:")
        await ctx.channel.send(random.choice(list(api_response.data)).embed_url)

    except ApiException:
        print("Something brokey with GIFHY API")


@client.command()
async def add(ctx, *, expression):
    split_expression = expression.split()

    list_express = list(split_expression)

    for i in range(0, len(list_express)):
        list_express[i] = int(list_express[i])

    product = sum(list_express)
    await ctx.channel.send(f"The sum of the black is: {product}")


@client.command()
async def vote(ctx, *, state):
    if state not in names_votes:
        names_votes.append(state)
        await ctx.channel.send(f"The following vote has been stored: '{state}'")
    else:
        await ctx.channel.send(f"Someone already voted '{state}'. ")


@client.command()
async def show_votes(ctx):
    length = len(names_votes)

    if length == 0:
        await ctx.channel.send("There are no votes")
    elif length > 0:
        for i in range(length):
            msg = await ctx.channel.send(f"{i+1}. {names_votes[i]}")
            await msg.add_reaction("⬆")


@client.command()
async def remove_vote(ctx, *, number, length=len(names_votes)):
    if length > 0:
        num = number - 1
        names_votes.remove(names_votes[num])

    while length == 0:
        await ctx.channel.send("There are no votes. Can't remove")
        break


@client.command()
async def floppa(ctx):
    await ctx.channel.send("Floppa")
    file = "qloppa.jpg"
    await ctx.channel.send(file=discord.File(file))


@client.command()
async def maze(ctx):
    counter = 0
    position_x = 7
    position_y = 3
    up_or_down = 1
    right_or_left = 1

    await ctx.channel.send("""
        To move around use:
        w = up
        a = left
        s = down
        d = right
        """)

    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 0
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],  # row 1
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],  # row 2
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],  # row 3
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],  # row 4
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],  # row 5
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],  # row 6
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],  # row 7
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],  # row 8
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # row 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # filler row
        ]

    while counter < 20:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
                   msg.content.lower() in ["w", "s", "a", "d"]

        direction_input = await client.wait_for("message", check=check)

        if direction_input.content.lower() == "w":
            if grid[position_x - up_or_down][position_y] == 1:
                position_x -= 1
                counter += 1
            elif grid[position_x - up_or_down][position_y] == 0:
                await ctx.channel.send("Ouch! I can not walk through walls…")

        elif direction_input.content.lower() == "s":
            if grid[position_x + up_or_down][position_y] == 1:
                position_x += 1
                counter += 1
            elif grid[position_x + up_or_down][position_y] == 0:
                await ctx.channel.send("Ouch! I can not walk through walls…")

        elif direction_input.content.lower() == "a":
            if grid[position_x][position_y - right_or_left] == 1:
                position_y -= 1
                counter += 1
            elif grid[position_x][position_y - right_or_left] == 0:
                await ctx.channel.send("Ouch! I can not walk through walls…")

        elif direction_input.content.lower() == "d":
            if grid[position_x][position_y + right_or_left] == 1:
                position_y += 1
                counter += 1
            elif grid[position_x][position_y + right_or_left] == 0:
                await ctx.channel.send("Ouch! I can not walk through walls…")

        if position_x == 9 and position_y == 4 or position_x == 1 and position_y == 7:
            await ctx.channel.send("Oh no, a trap!")
            position_x = 7
            position_y = 3
        elif position_x == 3 and position_y == 10:
            await ctx.channel.send("Oh no, a trap!")
            position_x = 7
            position_y = 3

        if position_x == 1 and position_y == 5 or position_x == 6 and position_y == 9:
            await ctx.channel.send("A chocolate bar, I feel stronger.")
            counter -= 20

        if counter == 20:
            await ctx.channel.send("Game over! You did not reach the exit in time.")

        if position_x == 1 and position_y == 9:
            await ctx.channel.send("You survived! Well done adventurer!")


@client.command()
async def commands(ctx):
    all_commands = """
!maze
!gif <name>
!add <numbers with space>
!vote <name>
!show_votes
!remove_votes <index>
!floppa
!quad
!join
!leave
    """
    await ctx.send(all_commands)


@client.command()
async def quad(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.channel.send("Enter A:")
    av = await client.wait_for("message", check=check)
    await ctx.channel.send("Enter B:")
    bv = await client.wait_for("message", check=check)
    await ctx.channel.send("Enter C:")
    cv = await client.wait_for("message", check=check)

    a = int(av.content)
    b = int(bv.content)
    c = int(cv.content)

    plus = (-1 * b) + math.sqrt((b ** 2) - 4 * a * c)
    calc_plus = plus / (2 * a)

    minus = (-1 * b) - math.sqrt((b ** 2) - 4 * a * c)
    calc_neg = minus / (2 * a)

    if calc_plus != calc_neg:
        await ctx.channel.send(f"X1: {calc_plus}")
        await ctx.channel.send(f"X2: {calc_neg}")
    else:
        await ctx.channel.send(f"X: {calc_plus}")


@client.command()
async def join(ctx):
    global voice_client
    global canal
    try:
        canal = ctx.author.voice.channel
        voice_client = await canal.connect()
        await ctx.channel.send(f"Floppa bot joined {canal}")
    except ClientException or AttributeError:
        await ctx.channel.send("You are not connected to a channel!")


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.channel.send(f"Floppa bot left {canal}")


@client.command()
async def clear(ctx, *, number):
    pass

client.run(TOKEN)
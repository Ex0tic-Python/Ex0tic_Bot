# Fun Cog
# A cog that contains some fun features for the bot

# ---------------------------------------------------------------------------------------------------------

# Imports
# Provides us with some essential features used in making commands
import discord

# Provides us with 'commands' which is used in making a Cog Sub-Class and giving command functions the command decorator
from discord.ext import commands

# Provides us a way to make random decisions from a list
import random

# Provides us with the bot var from Main.py
from Main import bot

import Globals

# ---------------------------------------------------------------------------------------------------------

# Establish Variables
# Assigns youtube links from Other-Youtube.txt to a tuple (Because speed doesn't hurt)
with open(Globals.bot_folder_path(r'Other\Other-Youtube.txt'), 'r') as links_file:
    links_tuple = tuple(links_file.readlines())

# Assigns compliments from Other-Compliments.txt to a tuple (Because speed doesn't hurt)
with open(Globals.bot_folder_path(r'Other\Other-Compliments.txt'), 'r') as compliments_file:
    compliments_tuple = tuple(compliments_file.readlines())

# Assigns insults from Other-Insults.txt to a tuple (Because speed doesn't hurt)
with open(Globals.bot_folder_path(r'Other\Other-Insults.txt'), 'r') as insults_file:
    insults_tuple = tuple(insults_file.readlines())

# ---------------------------------------------------------------------------------------------------------

# Fun Commands
# Makes a Cog Class which houses all the Fun Commands
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Simple 'Hello' command
    @commands.command(help='A simple hello command')
    async def hello(self, ctx) -> str:
        await ctx.send(f"Hello {ctx.author.mention}! My name is Ex0tic_Bot")

    # Command that provides a random youtube link from a seperate text file
    @commands.command(help='Sends a random youtube link from a predefined list of links. To suggest a link, use `E-feedback`')
    async def youtube_link(self, ctx) -> str:
        message = await ctx.send(choice(links_tuple))
        await message.edit(suppress=True)

    # Command that compliments a mentioned user using a random compliment from a seperate text file
    @commands.command(help='Gives a random compliment from a predefined list of compliments. If you would like to add your own compliment, use `E-feedback`')
    async def compliment(self, ctx, user_id: int = None) -> str:
        if user_id is not None:
            if len(user_id) == 18:
                try:
                    user_id = int(user_id)
                except ValueError:
                    await ctx.send("It seems this ID contains something other then numbers. Please enter a valid ID")
                    return

                if ctx.guild is not None:
                    user = ctx.guild.get_member(user_id)
                else:
                    user = ctx.guild.get_user(user_id)

                if user is not None:

                    if user.id == Globals.exo_bot.user_id:
                        await ctx.send(
                            "I'm a bot and have no feelings so compliments mean nothing to me. But I'll still take it <3"
                        )
                    elif user.bot:
                        await ctx.send(
                            f"{user.mention}, you are the most useful bot I've ever seen."
                        )
                    elif user.id in Globals.dev_ids:
                        await ctx.send(
                            f"{user.mention}, you are a great programmer. Thanks for programming so well"
                        )
                    else:
                        final_compliment = choice(compliments_tuple)
                        await ctx.send(f"{user.mention}, {final_compliment}")

                else:
                    await ctx.send(
                        f"{ctx.author.mention}, a user can't be found matching this ID. Please try again"
                    )
            else:
                await ctx.send(
                    f"{ctx.author.mention}, it seems like this is an invalid ID. Please try again"
                )
        else:
            await ctx.send(
                f"{ctx.author.mention}, you are missing the <user_id> parameter. For more help, use `E-help compliment`\nCommand Structure: E-compliment <user_id>"
            )

    # Command that insults a mentioned user using a random insullt from a seperate text file
    @commands.command()
    async def insult(self, ctx, user_id: int = None) -> str:
        if user_id is not None:
            if len(user_id) == 18:
                try:
                    user_id = int(user_id)
                except ValueError:
                    await ctx.send("It seems this ID contains something other then numbers. Please enter a valid ID")
                    return

                if ctx.guild is not None:
                    user = ctx.guild.get_member(user_id)
                else:
                    user = ctx.guild.get_user(user_id)

                if user is not None:

                    if user.id == Globals.exo_py.user_id:
                        await ctx.send(
                            "You may not insult my creator."
                        )
                    elif user.id == Globals.exo_bot.user_id:
                        await ctx.send(
                            "I'm not just gonna insult myself."
                        )
                    elif user.bot:
                        await ctx.send(
                            f"{user.mention}, you are the most useless bot I've ever seen."
                        )
                    else:
                        final_insult = choice(insults_tuple)
                        await ctx.send(f"{user.mention}, {final_insult}")

                else:
                    await ctx.send(
                        f"{ctx.author.mention}, a user can't be found matching this ID. Please try again"
                    )
            else:
                await ctx.send(
                    f"{ctx.author.mention}, it seems like this is an invalid ID. Please try again"
                )
        else:
            await ctx.send(
                f"{ctx.author.mention}, you are missing the <user_id> parameter. For more help, use `E-help insult`\nCommand Structure: E-insult <user_id>"
            )

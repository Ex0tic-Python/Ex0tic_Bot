# Other Cog

# ---------------------------------------------------------------------------------------------------------

# Imports
# Provides us with some essential features used in making commands
import discord

# Provides us with 'commands' which is used in making a Cog Sub-Class and giving command functions the command decorator
from discord.ext import commands

# Provides us with a way to get the current date and time
import datetime

import Globals

# ---------------------------------------------------------------------------------------------------------

# Cog Commands
# Makes a Class which houses all the 'Other' commands and inherits from the 'Cog' Class
class Other_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command that provides the most info about a user avaliable using the discord.py lib
    @commands.command(help='Gets info on a user using their ID\n\nParameters:\nuser_id - Takes a user ID')
    async def get_user_info(self, ctx, user_id=None):
        if user_id is not None:
            if len(user_id) == 18:
                try:
                    user_id = int(user_id)
                except ValueError:
                    await ctx.send(f"{ctx.author.mention}, it seems like this ID contains characters other then numbers. Please try again")
                    return

                if ctx.guild is not None:
                    user = ctx.message.guild.get_member(user_id)
                    if user is not None:
                        user_info = discord.Embed(title=f"**{user.name}#{user.discriminator}'s Info**", color=0x36393E)
                        user_info.timestamp = datetime.utcnow()
                        user_info.set_thumbnail(url=str(user.avatar_url))
                        user_info.add_field(name="Username", value=f"*{user.name}#{user.discriminator}*", inline=True)
                        user_info.add_field(name="Server Nickname", value=f"*{user.display_name}#{user_discriminator}*", inline=True)
                        user_info.add_field(name="User ID", value=f"*{str(user.id)}*", inline=True)
                        user_info.add_field(name="User Discriminator", value=f"*{user.discriminator}*", inline=True)
                        user_info.add_field(name="Is Bot", value=f"*{str(user.bot)}*", inline=True)
                        user_info.add_field(name="Account Creation Date", value=f"*{*", inline=True)
                        user_info.add_field(name="User Avatar Link", value=f"*{str(user.avatar_url)}*", inline=False)
                        user_info.add_field(name="User Default Avatar Link", value=f"*{str(user.default_avatar_url)}*", inline=True)
                        embed.set_footer(text=f"Requested by {ctx.author.name} at ", icon_url=Globals.bot.pfp)
                        await ctx.send(embed=user_info)
                    else:
                        await ctx.send(f"{ctx.author.mention}, a user matching this ID could not be found")

                else:
                    user = bot.get_user(user_id)
                    if user is not None:
                        date = user.created_at
                        user_info = discord.Embed(title=f"**{user.name}#{user.discriminator}'s Info**", color=0x36393E)
                        user_info.set_thumbnail(url=str(user.avatar_url))
                        user_info.add_field(name="Username", value=f"*{user.name}#{user.discriminator}*", inline=True)
                        user_info.add_field(name="User Discriminator", value=f"*{user.discriminator}*", inline=True)
                        user_info.add_field(name="User ID", value=f"*{str(user.id)}*", inline=True)
                        user_info.add_field(name="Is Bot", value=f"*{str(user.bot)}*", inline=True)
                        user_info.add_field(name="Account Creation Date", value=f"*{date.month}/{date.day}/{date.year} {date.hour}:{date.minute}:{date.second} UTC\n(MM/DD/YYYY HH:MM:SS)*", inline=True)
                        user_info.add_field(name="User Avatar Link", value=f"*{str(user.avatar_url)}*", inline=False)
                        user_info.add_field(name="User Default Avatar Link", value=f"*{str(user.default_avatar_url)}*", inline=True)
                        await ctx.send(embed=user_info)
                    else:
                        await ctx.send(f"{ctx.author.mention}, a user matching this ID could not be found")

            else:
                await ctx.send(f"{ctx.author.mention}, it doesn't seem like this is a valid ID. Please try again")
        else:
            await ctx.send(f"{ctx.author.mention}, you are missing the <user_id> parameter\nFor help, use `E-help get_user_info`")

    # Command that provides the most info about the guild as possible using the discord.py lib
    @commands.command(help='Gets info on the server which the command is called from\n\nParameters:\nextended - Takes the optional `-extended` parameter')
    async def get_guild_info(self, ctx, extended=None):
        if ctx.guild is not None:
            if extended is None:
                guild_info = discord.Embed(title=f"**{ctx.guild.name}'s Info**", color=0x0302c0)

            elif extended == '-extended':
                guild_info = discord.Embed(title=f"**{ctx.guild.name}'s Info**", color=0x0302c0)

            else:
                return
        else:
            await ctx.send(f"This command is only avaliable for use in servers")

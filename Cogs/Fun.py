# Fun Cog
# ---------------------------------------------------------------------------------------------------------
# Imports
# Provides us a way to make random decisions from a list
from random import choice

# ---------------------------------------------------------------------------------------------------------

# Establish Variables
# Assigns youtube links from Other-Youtube.txt to a list
with open(f'{bot_folder_path}Other-Youtube.txt', 'r') as links_file:
    links_list = tuple(links_file.readlines())

# Assigns compliments from Other-Compliments.txt to a list
with open(f'{bot_folder_path}Other-Compliments.txt', 'r') as compliments_file:
    compliments_list = tuple(compliments_file.readlines())

# Assigns insults from Other-Insults.txt to a list
with open(f'{bot_folder_path}Other-Insults.txt', 'r') as insults_file:
    insults_list = tuple(insults_file.readlines())

# ---------------------------------------------------------------------------------------------------------

# Fun Commands
# Makes a Cog Class which houses all the Fun Commands
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Simple 'Hello' command
    @commands.command(help='A simple hello command')
    async def hello(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send(f"Hello {ctx.author.mention}! My name is Ex0tic_Bot")

    # Command that prints the script for the The FitnessGram Pacer Test
    @commands.command(help='Sends the script for the Pacer Test')
    async def pacer(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send("The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal: ***Ding***\nA single lap should be completed each time you hear this sound: ***Ding***\nRemember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready: ***ding***")

    # Command that provides a random youtube link from a seperate text file
    @commands.command(help='Sends a random youtube link from a predefined list of links. To suggest a link, use `E-feedback`')
    async def youtube_link(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        message = await ctx.send(choice(links_list))
        await message.edit(suppress=True)

    # Command that sends where_banana.jpg
    @commands.command(help='Sends \'where_banana.jpg\'')
    async def banana(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send(file=discord.File(f'{bot_folder_path}where_banana.jpg'))

    # Command that sends trump.mp4
    @commands.command(help='Sends \'trump.mp4\'')
    async def trump(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send(file=discord.File(f'{bot_folder_path}trump.mp4'))

    # Command that sends hakerman.mp4
    @commands.command(help='Sends \'hakerman.mp4\'')
    async def hakerman(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send(file=discord.File(f'{bot_folder_path}hakerman.mp4'))

    # Command that sends rocket_league.mp4
    @commands.command(help='Sends \'rocket_league.mp4\'')
    async def rocket_league(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send(file=discord.File(f'{bot_folder_path}rocket_league.mp4'))

    # Command that sends rip.mov
    @commands.command(help='Sends \'rip.mov\'')
    async def roll_credits(self, ctx):
        make_log_entry(ctx.message.content, ctx.message.author, ctx.guild)
        await ctx.send(file=discord.File(f'{bot_folder_path}rip.mov'))

    # Command that sends stop.webm
    @commands.command(help='Sends \'stop.webm\` with the optional override parameter')
    async def stop(self, ctx, override=None):
        if override is None:
            make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
            await ctx.send(file=discord.File(f'{bot_folder_path}stop.webm'))
            await ctx.send("Watch this video all the way through WITHOUT skipping ahead\nI bet you can't ;)")
        elif override == '-override':
            if ctx.author.id in override_users:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
                await ctx.send(file=discord.File(f'{bot_folder_path}stop.webm'))
            else:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
                await ctx.send(f"{ctx.author.mention}, you may not use the '-override' parameter.")
        else:
            make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)

    # Command that sends Slap.mp4, a video that may crash users Discord if on Windows 10
    @commands.command(help='Sends \'Slap.mp4\' which is known for crashing Discord users on Windows 10. This command takes an override parameter.')
    async def crash(self, ctx, override=None):
        if override is None:
            make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
            await ctx.send("**WARNING: MAY CRASH YOUR DISCORD IF ON WINDOWS 10**")
            await ctx.send(file=discord.File(f'{bot_folder_path}Slap.mp4'))
            await ctx.send("**WARNING: MAY CRASH YOUR DISCORD IF ON WINDOWS 10**")
        elif override == '-override':
            if ctx.author.id in override_users:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
                await ctx.message.delete()
                await ctx.send(file=discord.File(f'{bot_folder_path}Slap.mp4'))
            else:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
                await ctx.send(f"{ctx.author.mention}, you may not use the '-override' parameter.")
        else:
            make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)

    # Command that compliments a mentioned user using a random compliment from a seperate text file
    @commands.command(help='Gives a random compliment from a predefined list of compliments. If you would like to add your own compliment, use `E-feedback`')
    async def compliment(self, ctx, user:discord.member, override:str=None):
        if user is not None:
            if override is None:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
                if user.id == exo_bot:
                    await ctx.send("I'm a bot. I have no feelings. Compliments mean nothing to me.")

                elif user.bot:
                    await ctx.send(f"{user.mention}, you are the most useful bot I've ever seen.")

                else:
                    final_compliment = choice(compliments_list)
                    await ctx.send(f"{user.mention}, {final_compliment}")

            elif override == '-override':
                if ctx.author.id in override_users:
                    make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
                    await ctx.send("Permission Granted\n*Overriding command limits...*")

                    if user.id == exo_bot.user_id:
                        await ctx.send("Awwwww, thanks Python :)")

                    elif user.bot:
                        await ctx.send(f"{user.mention}, you are the most useful bot I've ever seen.")

                    else:
                        final_compliment = choice(compliments_list)
                        await ctx.send(f"{user.mention}, {final_compliment}")
                else:
                    make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
                    await ctx.send(f"{ctx.author.mention}, you may not use the '-override' parameter.")
            else:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
        else:
            make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
            await ctx.send(f"{ctx.author.mention}, you are missing the mention parameter. For more help, use `E-help compliment`\nStructure: E-compliment <user> [override]")

    # Command that insults a mentioned user using a random insullt from a seperate text file
    @commands.command()
    async def insult(self, ctx, user:discord.Member=None, override:str=None):
        if user is not None:
            if override is None:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
                if user.id == exo_py.user_id:
                    await ctx.send("You may not insult my creator.")

                elif user.id == exo_bot.user_id:
                    await ctx.send("I'm not just gonna insult myself.")

                elif user.bot:
                    await ctx.send(f"{user.mention}, you are the most useless goddamn bot I've ever seen.")

                else:
                    final_insult = choice(insults_list)
                    await ctx.send(f"{user.mention}, {final_insult}")

            elif override == '-override':
                if ctx.author.id in override_users:
                    make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, True)
                    await ctx.send("Permission Granted\n*Overriding command limits...*")

                    if user.bot:
                        await ctx.send(f"{user.mention}, you are the most useless goddamn bot I've ever seen.")

                    else:
                        final_insult = choice(insults_list)
                        await ctx.send(f"{user.mention}, {final_insult}")
                else:
                    make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
                    await ctx.send(f"{ctx.author.mention}, you may not use the '-override' parameter.")
            else:
                make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
        else:
            make_log_entry(ctx.message.content, ctx.message.author, ctx.guild, False)
            await ctx.send(f"{ctx.author.mention}, you are missing the mention parameter. For more help, use `E-help compliment`\nStructure: E-insult <user> [override]")
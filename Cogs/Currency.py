# Currency Cog
# ---------------------------------------------------------------------------------------------------------
# Imports
# Provides us with a way to work with JSON Files
from json import load, dump

# ---------------------------------------------------------------------------------------------------------

# Establish Variables
# Get the Currency dictionary from Currency-Accounts.json
with open(f'{bot_folder_path}Currency-Accounts.json', 'r') as currency_file:
    currency_dict = load(currency_file)

# ---------------------------------------------------------------------------------------------------------

# Establish Functions
# Check whether the user has an account with us, and returns their account if they do
def check_for_user(user_id):
    try:
        return currency_dict[str(user_id)]
    except KeyError:
        return False

# ---------------------------------------------------------------------------------------------------------

# Currency Commands
# Makes a Cog Class which houses all the currency commands
class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Checks if the user has an account, if they don't, one is made
    @commands.command()
    async def make_account(self, ctx):
        user_account = check_for_user(ctx.author.id)
        if user_account is not False:
            """



            do stuff



            """
            pass
        else:
            await ctx.send(f"{ctx.author.mention}, you already have an account with us!")
        
    # Displays the users balance or mentioned users balance
    @commands.command()
    async def balance(self, ctx, user:discord.Member=None):
        if user is None:
            user_account = check_for_user(ctx.author.id)
            if user_account is not False:
                embed=discord.Embed(title=">Balance", color=0x0302c0)
                embed.add_field(name=f"Exo${str(user_account['balance'])}", value=f"{ctx.author.display_name}'s Balance", inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"{ctx.author.mention}, it seems like you don't have an account with us. Use `E-make_account` to create an account.")
        
        elif user is not None:
            user_account = check_for_user(user.id)
            if user_account is not False:
                embed=discord.Embed(title=">Balance", color=0x0302c0)
                embed.add_field(name=f"Exo${str(user_account['balance'])}", value=f"{user.display_name}'s Balance", inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"{ctx.author.mention}, it seems like the mentioned user doesn't have an account with us. Use `E-make_account` to create an account.")
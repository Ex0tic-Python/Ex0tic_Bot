# Global Stuff
# Basically a Python file that stores stuff (Vars, Funcs, etc.) that I may need in one or more Python files
# Also stores vars that may change constantly, mking it easier for me to access them and change them

# ---------------------------------------------------------------------------------------------------------

# Imports
# Provides us with a way to work with paths (Used in the bot_folder_path function)
from os import path

# ---------------------------------------------------------------------------------------------------------

# Variables
# Makes a class which houses some info about important users
class Profiles:
    def __init__(self, username, user_discriminator, user_id):
        self.username = username
        self.discriminator = discriminator
        self.user_id = user_id

# Makes some objects in the class
exo_bot = Profiles('Ex0tic_Python', 7571, 546390125425459211)
exo_py - Profiles('Ex0tic_Bot', 2986, 842537874544132157)

# Path to bots image
bot_pfp = r'C:\Users\AnibalF6725\Documents\Code\Python\DiscordBot\Ex0tic_Bot.jpg'

# Bot version (Used in extra_info command)
bot_version = 0.5

# Total commands of the bot (Used in extra_info command)
total_commands = 999

# A variable which stores the number of lines of the script (Used in extra_info command)
script_lines = 999

# Link to update notes (Used in extra_info command)
update_notes = 'https://github.com/Ex0tic-Python/Ex0tic_Bot/blob/main/UPDATE%20NOTES.md'

# List containing the ID's of the bot dev team (Used in commands which require special access) (Currently only me :/ )
dev_ids = (546390125425459211)

# Dictionary that houses emojis the bot uses
emojis = {
    'exotic_bot': '<:Ex0tic_Bot:864541148647391232>',
    'discord_online': '<:discord_online:864533505534197821>',
    'discord_offline': '<:discord_offline:864533501066608660>',
    'discord_typing': '<a:discord_typing:864533501189423144>',
    'discord_message': '<:discord_message:864548909152731147>',
    'database': '<:database:864548909199392798>',
    'spinning_cog': '<a:spinning_cog:864580163021963294>'
}

# ---------------------------------------------------------------------------------------------------------

# Functions
# Funtion that returns a joined path
def bot_folder_path(path_to_join: str) -> str:
    return os.path.join(r'C:\Users\AnibalF6725\Documents\Code\Python\DiscordBot', path_to_join)

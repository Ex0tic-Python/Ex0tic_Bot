# Functions
# ---------------------------------------------------------------------------------------------------------
# Imports
# OS for joining paths
import os

# ---------------------------------------------------------------------------------------------------------

# Variables
# A variable which stores the number of lines of the script
script_lines = 999

# Bot version
bot_version = 999

# Total commands of the bot
total_commands = 999

# Link to update notes
update_notes = 'https://pastebin.com/zBtqhaaT'

# Path to bots image
bot_pfp = r'C:\Users\AnibalF6725\Documents\Code\Python\DiscordBot\Ex0tic_Bot.jpg'

# Dictionary that houses emojis the bot uses
emojis = {
    'discord_typing':'<a:discord_typing:864533501189423144>',
    'discord_online':'<:discord_online:864533505534197821>',
    'discord_offline':'<:discord_offline:864533501066608660>',
    'discord_ex0tic_bot':'<:Ex0tic_Bot:864541148647391232>',
    'discord_message':'<:discord_message:864548909152731147>',
    'discord_db':'<:discord_db:864548909199392798>'
}

# ---------------------------------------------------------------------------------------------------------

# Functions
# Funtion that returns the path to a certain File in the Bot Folder
def bot_folder_path(file_to_join: str) -> str:
    return os.path.join(r'C:\Users\AnibalF6725\Documents\Code\Python\DiscordBot', file_to_join)

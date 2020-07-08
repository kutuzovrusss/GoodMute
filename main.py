import os
import config
import discord
from discord.ext import commands
from colorama import Fore, Style  # Цветная консоль
from colorama import init  # Цветная консоль


TOKEN = config.TOKEN
PREFIX = config.PREFIX

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')
init()


# Запуск Бота
@client.event
async def on_ready():
    print(" ")
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(Fore.CYAN + '|' + Style.RESET_ALL + f'        Бот активирован!         ' + Fore.CYAN + '|' + Style.RESET_ALL)
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(f'  Имя бота - {client.user.name}')
    print(f'  ID бота  - {client.user.id}  ')
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(" ")


@client.event
async def on_message(message):
    if not message.author.bot and message.author.roles:
        if message.guild:
            mute_role = discord.utils.get(message.guild.roles, name="Muted")
            if mute_role in message.author.roles:
                await message.delete()
            else:
                await client.process_commands(message)


for filename in os.listdir('./Modules'):
    if filename.endswith('.py'):
        client.load_extension(f'Modules.{filename[:-3]}')
        print(Fore.YELLOW + "[G-M] " + Style.RESET_ALL + f"Загружен модуль - {filename[:-3]}")

client.run(TOKEN)

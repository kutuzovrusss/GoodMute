# Импорт
import discord
import config
from discord.ext import commands


# Код
class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Информация"]

    @commands.command(
        aliases=["help", "comms", "commands"],
        description="This message",
        usage="help [module]")
    async def helps(self, ctx, name=None):
        prefix = config.PREFIX

        cogs = []
        for i in self.bot.cogs:
            cog = self.bot.cogs[i]
            hide = len(cog.cog_name)
            if hide == 1:
                cogs.append(f"{cog.cog_name[0]}")

        if not name:
            embed = discord.Embed(
                description=f"{ctx.author.display_name}, The module was not found! \nTo get a list of commands write {config.PREFIX}help [module]\n"
                            f"**Available Modules:** {', '.join(cogs)}")
            await ctx.send(embed=embed)
        else:
            if name in cogs:
                cog = None
                namec = None
                for i in self.bot.cogs:
                    coge = self.bot.cogs[i]
                    if name in coge.cog_name:
                        cog = coge
                        namec = i
                        break

                name = cog.cog_name[0]
                comm_list = []

                for command in self.bot.commands:
                    if command.cog_name == namec:
                        if not command.hidden:
                            comm_list.append(
                                f"**{command.aliases[0]}:** {command.description}\n`{prefix}{command.usage}`\n\n")

                embed = discord.Embed(
                    title=f"Help | {name}",
                    description=f"".join(comm_list))
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/695787093242282055/707320024473534485/what.png')

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    description=f"{ctx.author.display_name}, The module was not found! \nTo get a list of commands write {config.PREFIX}help [module]\n"
                                f"**Available Modules:** {', '.join(cogs)}")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(information(client))

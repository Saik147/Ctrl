from discord.ext import commands
import discord

from helpers.db_manager import add_welcome, get_welcome

class Greet(commands.Cog, command_attrs=dict (hidden=True)):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        id=await get_welcome(member.guild.id)
        if member.guild.id == id:
	        embed=discord.Embed(color=0x2f3136, title=f"Hey {member.name}", description="● Welcome to BackYard Coders\n● Thanks for joining\n● Make sure to read rules\n● Chat with new friends")
	        embed.set_thumbnail(url=member.display_avatar.url)
	        embed.set_footer(text="Eat Sleep Code", icon_url=member.display_avatar.url)
	        # role = discord.utils.get(member.guild.roles, name="Coder")
	        # await member.add_roles(role)
	        await self.bot.get_channel(1064154848997670983).send(embed=embed)
	        await self.bot.get_channel(1064154848997670983).send(member.mention, delete_after=1)
        else:
            return

    @commands.hybrid_group(invoke_without_command=True)
    async def welcome(self,ctx):
        await ctx.send('Available Setup Commands: \nwelcome channel <#channel>')
    @welcome.command()
    async def set(self, ctx, channel:discord.TextChannel):
        await add_welcome(ctx.guild.id, channel.id)
        embed=discord.Embed(description=f"Welcome channel set to `{channel.name}`")
        await ctx.send(embed=embed)
        

async def setup(bot):
    await bot.add_cog(Greet(bot))
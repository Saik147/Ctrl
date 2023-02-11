import asyncio, discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

from gpt.GPT import generate_gpt3_response

class Beta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
		name="ask_gpt",
		description="Get answer of a question"
	)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ask_gpt(self, ctx, *, prompt: str):
	    await ctx.defer(ephemeral=False)
	    result = generate_gpt3_response(user_text=prompt)
	    embed=discord.Embed(description=f"**Query** : ```{prompt}```\n**Response**; ```{result}```", color=0x2f3136)
	    await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Beta(bot))
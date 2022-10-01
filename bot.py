import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()

alulaBot = commands.Bot(command_prefix = "!", description = "AlulaBot", intents = discord.Intents.all())

@alulaBot.event
async def on_ready():
    print(">> Running...")

@alulaBot.command()
async def coucou(ctx):
    print(f">> Command from {ctx.author} | {ctx.author.mention} : coucou")
    await ctx.send("Hello")

alulaBot.run(os.getenv("ALULABOT_TOKEN"))
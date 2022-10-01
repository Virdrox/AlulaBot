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
async def annonce(ctx, title):
    print(f">> Command from {ctx.author} | {ctx.author.mention} : annonce")
    
    embed = discord.Embed(
        title = 'Test',
        description = 'This is a description',
        colour = discord.Colour.red()
    )

    embed.set_footer(text = 'This is a footer')
    embed.add_field(name = 'Field Name', value = 'FieldValue', inline = False)
    embed.add_field(name = 'Field Name', value = 'FieldValue', inline = False)
    embed.add_field(name = 'Field Name', value = 'FieldValue', inline = False)

    await ctx.send(embed = embed)

@alulaBot.hybrid_group(fallback="get")
async def tag(ctx, name):
    await ctx.send(f"Showing tag: {name}")

@alulaBot.command()
async def create(ctx, name):
    await ctx.send(f"Created tag: {name}")

alulaBot.run(os.getenv("ALULABOT_TOKEN"))
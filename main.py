import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "MTQ4NTc5MjY2NzQ2MzA1NzQwOA.GlXf4k.HyPdJHDluwoR6gNVeoD2TafW2mZNzTbiwIQBHY"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="drewhi", description="Say hi")
async def drewhi(interaction: discord.Interaction):
    await interaction.response.send_message("hi")

bot.run(TOKEN)



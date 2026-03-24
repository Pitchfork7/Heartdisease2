import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "MTQ4NTc5MjY2NzQ2MzA1NzQwOA.GlXf4k.HyPdJHDluwoR6gNVeoD2TafW2mZNzTbiwIQBHY"

class MyBot(commands.Bot):
    def __init__(self):
        # We add message_content intent so the bot can see prefix commands
        intents = discord.Intents.default()
        intents.message_content = True 
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # This runs before the bot fully connects
        # Use this to sync your tree instead of on_ready
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.tree.command(name="drewhi", description="Say hi")
async def drewhi(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@bot.tree.command(name="talk", description="send heartdisease2 a message")
async def drewhi(interaction: discord.Interaction):
    await interaction.response.send_message("message recieved")

bot.run(TOKEN)

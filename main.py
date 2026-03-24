import discord
from discord import app_commands
from discord.ext import commands

import asyncio

from duckai import DuckAI

TOKEN = "MTQ4NTc5MjY2NzQ2MzA1NzQwOA.GlXf4k.HyPdJHDluwoR6gNVeoD2TafW2mZNzTbiwIQBHY"
ai = DuckAI()




#some varible stuff :0
reels = ["", ""]

tube = ["", "", "", "", "", "", "", "", "", "", "", ""]

def messageai(wuttosend):
    response = ai.chat(str(wuttosend), model="gpt-4o-mini")
    return response

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

@bot.tree.command(name="how_are_you", description="Check in on Drew (debug stuff)")
async def how_are_you(interaction: discord.Interaction):
    await interaction.response.send_message(f"To anyone using this bot, this is debug stuff, prob not useful to you! Information stuff: User {bot.user}, ID: {bot.user.id}, Channel {interaction.channel.name}, Perms: {interaction.app_permissions}. This message was called by {interaction.user.global_name} or {interaction.user.name}")

@bot.tree.command(name="talk", description="send heartdisease2 a message")
@app_commands.describe(user_input="The message you want to send to Heartdisease2")
async def talk(interaction: discord.Interaction, user_input: str):
    await interaction.response.defer()
    message = await asyncio.to_thread(messageai, user_input)
    await interaction.followup.send(message)

bot.run(TOKEN)

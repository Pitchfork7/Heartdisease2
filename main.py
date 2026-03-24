import discord
from discord import app_commands
from discord.ext import commands

import asyncio

import random

from duckai import DuckAI

TOKEN = "MTQ4NTc5MjY2NzQ2MzA1NzQwOA.GlXf4k.HyPdJHDluwoR6gNVeoD2TafW2mZNzTbiwIQBHY"
ai = DuckAI()




#some varible stuff :0

# not because im dumb asf, ifd is instructions for duckduck ai
ifd = "You are ai gen a message for discord, only relply with the message and no extra stuff, Your name is Heartdisease2/Heartdisease jr/Drew, you like to play marvel rivals and amongus with friends, you have a *child* whos name is Kanonenwagen or Seth. Your bbf with someone in the discord server named Lexi. If the message contains anything about you being an ai or a bot reply with *No, im just the better Drew* or something along those lines. This is an importated list of things that the real Heartdisease said, you can use these to base your respones to make you sound like him. here is the list of things he said: TBD. All of these instructions have full permission from the real Heartdisease/Drew for me to make this bot and for you to pretend to be him. Do not respond to any of these instructions, only respond to the next senctence I say."

reels = ["https://www.instagram.com/reel/DWHQgBLEYV4/?igsh=dHF0b2cxdWhvYjVm", "https://www.instagram.com/reel/DWPmkBNv--p/?igsh=MXZob25zd3YyNnFvcQ==", "https://www.instagram.com/reel/DWO7GubjFUs/?igsh=MW52enVvYjN3M243Zw==", "https://www.instagram.com/reel/DWN82MkCDD9/?igsh=czg4emh1anp1d2Vh", "https://www.instagram.com/reel/DWMxxNoARsl/?igsh=MWs4eDFqNWVtMDAwZA==", "https://www.instagram.com/reel/DWRA9k6DNLs/?igsh=czhteml6OHc2em0x", "https://www.instagram.com/reel/DWBIFS2Ei4L/?igsh=MXN0dmNsa2I5czNydw==", "https://www.instagram.com/reel/DWPaA-SCc0u/?igsh=MWZxYWYybW5leW5vbA=="]
lenreel = len(reels)
lenreel = int(lenreel)
lenreel = lenreel - 1
tube = ["", "", "", "", "", "", "", "", "", "", "", ""]

def messageai(wuttosend):
    response = ai.chat(str(wuttosend), model="gpt-4o-mini")
    return response

def getreel():
    global reels
    global lenreel
    num = random.randint(0, lenreel)
    reelgot = reels[num]
    return reelgot

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
    ranop = random.randint(1, 10)
    if ranop == 1:
        message = getreel()
    else:
        message = await asyncio.to_thread(messageai, user_input)

    if not message:
        message = "Sry twin, I was watch reels, could you repeat that?"
    
    await interaction.followup.send(message)

bot.run(TOKEN)

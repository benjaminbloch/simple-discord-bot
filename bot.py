import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass

BOT_TOKEN = "PUT_YOUR_TOKEN_HERE"
CHANNEL_ID = 1240326597580427370

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print("Hello! Study bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Bot Is Online.")

@bot.command()
async def start(ctx):
        await ctx.send("Hello, lets start! what are you trying to do. A Purchase  B Claim Roles  C Talk To A Human. Please run the command ! then the option you picked.")
        return


    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start()
    await ctx.send(f"New session started at {human_readable_time}")



    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))
    break_reminder.stop()
    await ctx.send(f"Session ended after {human_readable_duration}.")


bot.run(BOT_TOKEN)

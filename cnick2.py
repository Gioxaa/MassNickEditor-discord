import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

original_nicknames = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Melayani TITIT WISYAM"))
    clear()
    print(f"BOT is online!")
    os.system("title SUPPORT BOT BY GIOXA")

@bot.command()
@commands.has_permissions(administrator=True)
async def call(ctx, *, new_nickname: str):
    guild = ctx.guild
    await ctx.send(f"Changing everyone's nickname to: {new_nickname}")
    
    for member in guild.members:
        try:
            if member != guild.owner and not member.bot:
                if member.id not in original_nicknames:
                    original_nicknames[member.id] = member.nick if member.nick else None
                await member.edit(nick=new_nickname)
                print(f"Changed nickname for {member.display_name}")
        except discord.Forbidden:
            print(f"Error: insufficient permissions to change nickname for {member.display_name}")
        except discord.HTTPException as e:
            print(f"Error: failed to change nickname for {member.display_name} due to: {e}")
    
    await ctx.send("Finished changing nicknames!")

@bot.command()
@commands.has_permissions(administrator=True)
async def backnick(ctx):
    guild = ctx.guild
    await ctx.send("Restoring original nicknames...")
    
    for member in guild.members:
        try:
            if member != guild.owner and not member.bot:
                original_nickname = original_nicknames.get(member.id)
                await member.edit(nick=original_nickname)
                print(f"Restored nickname for {member.display_name}")
        except discord.Forbidden:
            print(f"Error: insufficient permissions to restore nickname for {member.display_name}")
        except discord.HTTPException as e:
            print(f"Error: failed to restore nickname for {member.display_name} due to: {e}")
    
    await ctx.send("Finished restoring original nicknames!")

bot.run('token bot')

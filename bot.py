import discord
#導入discord模組
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
#command_prefix=一個字串、要呼叫機器人時的命令字首

#async重新定義on_ready的函式
@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run("ODc1NDk1NjQxNjAwNjMwODQ1.YRWW2g.OrrAJguFIXBkjo4F6mCSqzTKlpQ")
#bot.run("Token")
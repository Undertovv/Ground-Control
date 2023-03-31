#!/usr/bin/python3

import discord
from discord.ext import commands
from requests import get
from json import load

#/* --- Init & boot confirm --- */#
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '>', intents=intents) #Set command prefix

#Context test && commented deconstruction of command
@bot.command(pass_context = True) #Make new command (active, needs user to call)
async def test(ctx): #Name command, executes function on call
    await ctx.send("Ground control to Major Tom") 


#/* --- Anti-bottom brigade --- */#
@bot.event #Define event (passive, always reading)
async def on_message(message): #Read all messages visible to bot
    if "🥺" in message.content.lower(): #Look for :pleading:
        await message.channel.send('Haha bottom') #Bully.

    await bot.process_commands(message) #Repeat


#/* --- Post public IP as message --- */#
@bot.command(pass_context = True)
async def ip(ctx):
    myIP = get("https://ipinfo.io/json").json() #get public IP
    await ctx.send(myIP['ip']) #doxx myself lmao


#/* --- Get bot token and run bot --- */#
with open("botToken.json", "r") as token:
    botToken = load(token)
botToken = botToken["token"]

bot.run(botToken) #Token

import discord
from discord.ext.commands import bot
from discord.ext import commands

Client = discord.Client()
bot_prefix="?"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))

@client.command(pass context=True)
async def ping(ctx):
	await client.say("Pong!")

client.run("NDYyMjcyMDcyMjM2NzkzODU2.Dh2ULg.1q_9bL0XLirQ8GVb6sa1Y8vgwe0")

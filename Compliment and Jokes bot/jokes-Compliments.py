#  Import the discord.py library
import discord
from discord.ext.commands import Bot #import the external discord libraries
from random import choice # import the random modules choice function

# Create a bot instance with command prefix as !
bot = Bot("!")

# open and read the compliments file and turn it into a list of strings
with open("compliments.txt","r") as file:
	complimentList = list(file)

# open and read the jokes file and turn it inot a list of strings
with open("jokes.txt","r") as file:
	jokesList = list(file)

# Generate a random compliment to send
def getCompliment():
	return choice(complimentList)

# Generate a random joke to send
def getRandomJoke():
	return choice(jokesList)

@bot.event # this decorator binds the function to discord
async def on_ready(): # on ready runs only when the code establishes a connection to discord 
	print('We have logged in')

@bot.event
async def on_message(message): # on ready runs whenever a new message arrives
	print(message.author,message.content,message.channel)
	if message.content[0]!="!": # Checks if the content starts with a !
		if message.author != bot.user: # check whether the message was not made by the bot
			await message.channel.send("HI" + " " + str(message.author.mention))
	await bot.process_commands(message) # makes the function pass the message to be used by the other bot commands


@bot.command(pass_context=True) # binds the function as a bot command
async def compliment(ctx:discord.ext.commands.Context,member:discord.Member):
	complimentToSend = getCompliment() # Get a random compliment
	complimentToSend += member.mention # add a mention to the member tagged
	await ctx.send(complimentToSend) # send the message back in the same channel

@bot.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick) # edit the nickname of the member mentioned with the nickname given
    await ctx.send(f'Nickname was changed for {member.mention} ') # send a message in the same channel
	

@bot.command(pass_context=True)
async def joke(ctx):
	jokeToSend = getRandomJoke() # generate a randon joke
	await ctx.send(jokeToSend) # send joke in same channel
	
# Runs bot 
bot.run("TOKEN HERE")
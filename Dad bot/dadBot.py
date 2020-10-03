# DAD BOT
# This bot checks the messages and if it can make a dad joke ( ie of the form "IM X", "Hi X , Im dad" )
# Will reply back with the appropriate text

import os # import OS module
import discord # import discord.py module

# Create discord client
client = discord.Client()

@client.event # this decorator binds the function to discord
async def on_ready(): # on ready runs only when the code establishes a connection to discord 
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message :discord.Message): # on ready runs whenever a new message arrives
	if message.author != client.user: # Check to make sure the bots message isnt consumed and used 
		if message[:2]replace("'","").lower == "im": # Check for the im  part
			response = "hi " + message[2:] + " , I'm Dad." # returns hi X , im dad
			await message.channel.send(response) # sends the message back in the same channel
client.run("TOKEN HERE")
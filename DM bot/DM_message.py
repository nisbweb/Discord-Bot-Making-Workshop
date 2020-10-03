# DM bot
# This bot will constantly check the server and anytime anyone joins it will DM them about the server 

import os # import os module
import discord # import discord.py module

# Create a discord client
client = discord.Client()

@client.event # this decorator binds the function to discord
async def on_ready(): # on ready runs only when the code establishes a connection to discord 
	print(f'{client.user.name} has connected to Discord!')

@client.event 
async def on_member_join(member): # this decorator runs only when a member joins the server
	await member.create_dm() # creates a DM channel to the member who joined
	await member.dm_channel.send(  # sends the message to the user
		f'Hi {member.name}, welcome to my Discord server!'
	)

client.run("TOKEN HERE")
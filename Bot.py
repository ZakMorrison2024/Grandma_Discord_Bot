# Grandma_Discord_Bot
import discord # import discord libarires
import random # import random libraries

client = discord.Client() # discord client

# client event on message
@client.event 
async def on_message(message): # when client types a message

  if message:
         list = ["What was that deary??", "Not since 1958!","Sweetie.", "Let grandma see you."]
         await message.channel.send(random.choice(list)) # discord sends data back



client.run() # discord run client

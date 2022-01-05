#A Discord bot that answers questions about the wiki from Pixar's Cars (https://pixar.fandom.com/wiki/Cars) using GPT-III to answer


#!pip install transformers
#!pip install discord.py
#!pip install wikipedia
import discord
from discord.ext import commands
import asyncio
import wikipedia
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoConfig, AutoModelWithLMHead, AutoTokenizer


token = "239f0e664d11fa8a00ea3ee099a4da7f7d0bab975a5fc2360763f4b974df12e5" 


class MyClient(discord.Client):

    def __init__(self):
        super().__init__()

        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2") #load the tokenizer from the pretrained model on the gpt2 github page 
        self.model = GPT2LMHeadModel.from_pretrained("gpt2") #load the model from the same place 

        #self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        #self.model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content == "Hello":
            await message.channel.send("World")

        elif message.content == "!cars":  #this is the command that triggers the bot to answer a question about cars 

            await message.channel.send("What do you want to know about cars?")

            def check(m):  #this function checks if the bot can find an answer to the question in wikipedia and returns true if it can 
                return m.author == message.author and m.channel == message.channel

            try:  #try except block for handling errors with the bot finding an answer from wikipedia 
                msg = await client1.wait_for('message', timeout=60, check=check)   #wait for a response from the user for 60 seconds (the timeout value can be changed)

                search = msg  #store the users response as a string called search 

                await message.channel("I found this on Wikipedia: " + wikipedia .summary(search, sentences=2))   #print out 2 sentences from the summary of the wikipedia page about cars using the search string as a search term 

            except asyncio .TimeoutError:   #if no response is given within 60 seconds of asking for one then print out this error message and restart the process again by asking what they want to know about cars again 
                await message .channel("Sorry, you took too long.")  

        
client1 = MyClient()   #create an instance of MyClient called client1 which will be used to run our discord bot 
client1.run(token)     #run the discord bot using the token we created at the start of this code
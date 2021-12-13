#Discord bot that answers questions about the "Pixar's Cars" wiki (https://pixar.fandom.com/wiki/Cars) with GPT-III. Huge amount of critical information there that future generations will need to access.


import discord
from discord.ext import commands
import requests
import json
import re
import os
import openai
import time
import asyncio

TOKEN = os.environ.get(OPENAI_KEY) #add discord key

#bot settings
bot = commands.Bot(command_prefix='!')

#haven't set up GPT3 api access yet, gonna have to rework this whole part w/ the chronology library (https://github.com/OthersideAI/chronology)

tokenizer =
model = #
openai.api_key = os.getenv() #add openai key
max_length = 40

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#bot answer scripting
@bot.event
async def on_message(message):
    #Prevents bot from answering own message as prompt
    if message.author == bot.user:
        return

    #Tokenize user message
    user_message = message.content
    answer = generate_answer(user_message)
    if answer == '':
        await message.channel.send('Sorry, I dont understand.')
    else:
        await message.channel.send(answer)


#Answering function
def generate_answer(user_message):

    if user_message == '':
        return '' 

    else:

        #Encodes the user's message with GPT-3 tokenizer 
        input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')
        max_length = 40
        min_length = 15
        temperature = 0.7
        top_k = 0  
        top_p = 0.9 
        repetition_penalty = 1.0
        num_return_sequences = 1

      	#Answer generation 
        outputs = model.generate(input_ids=input_ids, max_length=max_length, min_length=min_length, temperature=temperature, top_k=top_k, top_p=top_p, repetition_penalty=repetition_penalty, num_return_sequences=num_return_sequences, bad_words_ids=bad_words_ids)

        #Decoding the answer with GPT-3 tokenizer 
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        #Returning the answer 
        return answer

#Running the bot
bot.run(TOKEN)
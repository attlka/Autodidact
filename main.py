#Discord bot that answers questions about the "Pixar's Cars" wiki (https://pixar.fandom.com/wiki/Cars) with GPT-III. Huge amount of critical information there that future generations will need to access.


import discord
from discord.ext import commands
import json
import os
import openai
import asyncio

#add discord key
TOKEN = os.environ.get(key= 239f0e664d11fa8a00ea3ee099a4da7f7d0bab975a5fc2360763f4b974df12e5)

#bot settings
bot = commands.Bot(command_prefix='!')

#haven't set up GPT3 api access yet, gonna have to rework this whole part w/ the chronology library (https://github.com/OthersideAI/chronology)

tokenizer =
model = #
openai.api_key = os.getenv(OPENAI_KEY) #add openai key
max_length = 40

@bot.event
async def on_ready():
    print(f'{bot.user.name} is dialed in!')

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
        await message.channel.send('Hmm, Im not sure I quite understand.')
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


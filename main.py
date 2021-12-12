#Create a Discord bot that answer questions about the "Pixar's Cars" wiki (https://pixar.fandom.com/wiki/Cars) with GPT-III.


#Importing the libraries
import discord
from discord.ext import commands
import requests
import json
import re
import os
import time
import asyncio

#Importing the GPT-3 model
from transformers import GPT2Tokenizer, GPT2LMHeadModel

#Importing the token
TOKEN = os.environ.get('DISCORD_TOKEN')

#Setting the bot
bot = commands.Bot(command_prefix='!')

#Setting the tokenizer and the model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

#Setting the max length of the answer
max_length = 40




#Setting the bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')




#Setting the bot
@bot.event
async def on_message(message):
    #Avoiding the bot to answer itself
    if message.author == bot.user:
        return

    #Getting the message of the user
    user_message = message.content

    #Getting the answer of the user's message with GPT-3 model and tokenizer
    answer = generate_answer(user_message)

    #If there is no answer, we send a default one (sorry I don't understand)
    if answer == '':
        await message.channel.send('Sorry, I don\'t understand.')

    #Else, we send the answer of the user's message with GPT-3 model and tokenizer
    else:
        await message.channel.send(answer)




#Function that generates an answer from a user's message with GPT-3 model and tokenizer 
def generate_answer(user_message):

    #If there is no user's message, we return an empty string (no answer) 
    if user_message == '':
        return ''

    #Else, we generate an answer from a user's message with GPT-3 model and tokenizer 
    else:

        #We encode the user's message with GPT-3 tokenizer 
        input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')

        #We set a maximum length for the generated text 
        max_length = 40

        #We set a minimum length for the generated text 
        min_length = 15

        #We set a temperature for our text generation process 
        temperature = 0.7

        #We set a top k or top p value for our text generation process 
        top_k = 0       #If top k is 0, we generate all words of our text generation process 

        top_p = 0.9     #If top p is 1, we generate all words of our text generation process 

        repetition_penalty = 1.0   #If repetition penalty is 1, we don't take into account repeated words in our text generation process 

        num_return_sequences = 1   #If num return sequences is 1, we only get one sentence as output (we don't want to get several sentences as output) 

        bad_words_ids = [tokenizer.encode(badword) for badword in ['idiot', 'stupid', 'shut up']]   #List of bad words that we want to avoid in our text generation process 

      	#Generating an answer from a user's message with GPT-3 model and tokenizer  
        outputs = model.generate(input_ids=input_ids, max_length=max_length, min_length=min_length, temperature=temperature, top_k=top_k, top_p=top_p, repetition_penalty=repetition_penalty, num_return_sequences=num_return_sequences, bad_words_ids=bad_words_ids)

        #Decoding the answer with GPT-3 tokenizer 
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        #Returning the answer 
        return answer




#Running the bot
bot.run(TOKEN)
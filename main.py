#Code for the Jordan Peterson Discord Bot

#Importing Libraries
import discord #discord library
import os
import requests
import pandas
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
from keep_alive import keep_alive

#Getting The Data-JP Quotes
url='https://www.overallmotivation.com/quotes/jordan-peterson-quotes/'
page=urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

#storing it in list
quotes=[]
for e in soup.find_all('ol'):
    for item in e.find_all('li'):
        quotes.append(item.get_text())

#Adding new functionality
sad_words=["Sad", "sad", "depressed", "angry", "frustrated", "miserable", "depressing"]

encourage_words= ["Ok, Clean your room.", "Embrace The Chaos", "Rule-3: Treat yourself as someone you are responsible for helping"]


#creating/instantiating a discord client
client = discord.Client()

def get_quote():
  msg = random.choice(quotes)
  return (msg)

#defining bot functionality
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send("Hey There, Have you cleaned your room ?")
  
  if msg.startswith('$inspire'):
    quote =get_quote()
    await message.channel.send(quote)

  if any (word in msg for word in sad_words):
    await message.channel.send(random.choice(encourage_words))


keep_alive()
client.run(os.environ['token'])

















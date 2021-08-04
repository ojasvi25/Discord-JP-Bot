#Code for the Jordan Peterson Discord Bot

#Importing Libraries
import discord #discord library
import os
import requests
import pandas
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random


#Getting The Data
url='https://www.overallmotivation.com/quotes/jordan-peterson-quotes/'
page=urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

#storing it in list
quotes=[]
for e in soup.find_all('ol'):
    for item in e.find_all('li'):
        quotes.append(item.get_text())


#creating/instantiating a discord client
client = discord.Client()

def get_quote():
  x=random.randrange(0,66)
  msg = quotes[x]
  return (msg)

#defining bot functionality
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  
  if msg.content.startswith('$hello'):
    await msg.channel.send("Hey There, Have you cleaned your room ?")
  elif msg.content.startswith('$inspire'):
    quote =get_quote()
    await msg.channel.send(quote)


client.run(os.environ['token'])

















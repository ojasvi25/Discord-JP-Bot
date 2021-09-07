#Code for the Jordan Peterson Discord Bot

#Importing Libraries
import discord #discord library
import os
import requests
import pandas
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
#import chromedriver
from keep_alive import keep_alive
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.chrome.options import Options

#Getting The Data-JP Quotes
url='https://www.overallmotivation.com/quotes/jordan-peterson-quotes/'
page=urlopen(url)
soup = BeautifulSoup(page, 'html.parser')



#storing JP Quotes in list
quotes=[]
for e in soup.find_all('ol'):
    for item in e.find_all('li'):
        quotes.append(item.get_text())

#storing JP Videos in list
vids = ['https://www.youtube.com/watch?v=dHXxtyUVTGU',
 'https://www.youtube.com/watch?v=_OtZ49i-yyk',
 'https://www.youtube.com/watch?v=z3cjksFFKAQ',
 'https://www.youtube.com/watch?v=rHI0Lhy0Q2s',
 'https://www.youtube.com/watch?v=fIEKfr9CaZA',
 'https://www.youtube.com/watch?v=Ddzf9Mm4hdY&t=9s',
 'https://www.youtube.com/watch?v=mFzFUM9Ulvg',
 'https://www.youtube.com/watch?v=1opHWsHr798&t=270s',
 'https://www.youtube.com/watch?v=IFmQ5waavJY',
 'https://www.youtube.com/watch?v=fElCVe836o0',
 'https://www.youtube.com/watch?v=9Xc7DN-noAc&t=191s',
 'https://www.youtube.com/watch?v=_9N6-VugF-E',
 'https://www.youtube.com/watch?v=fesSvXKxYd0',
 'https://www.youtube.com/watch?v=qEGkBDAuTmQ',
 'https://www.youtube.com/watch?v=wwi9Q9apHGI',
 'https://www.youtube.com/watch?v=RSmfp83_MkU',
 'https://www.youtube.com/watch?v=oteAPGPB6Uw',
 'https://www.youtube.com/watch?v=SN6vOFXL514',
 'https://www.youtube.com/watch?v=o0jyjxvReJk',
 'https://www.youtube.com/watch?v=3O_7O9_nV10',
 'https://www.youtube.com/watch?v=tOA0-bhNB5g',
 'https://www.youtube.com/watch?v=yZYQpge1W5s&t=1839s',
 'https://www.youtube.com/watch?v=Rc_NNjV0s1o',
 'https://www.youtube.com/watch?v=EOh1Gflu7Uw',
 'https://www.youtube.com/watch?v=n-SVPsGMPi8',
 'https://www.youtube.com/watch?v=dem0-UlKiZ4',
 'https://www.youtube.com/watch?v=x0vUsxhMczI',
 'https://www.youtube.com/watch?v=dHXxtyUVTGU',
 'https://www.youtube.com/watch?v=_OtZ49i-yyk',
 'https://www.youtube.com/watch?v=PpZZXkLsUic',
 'https://www.youtube.com/watch?v=IpPr5i1aHjE',
 'https://www.youtube.com/watch?v=iVym9wtopqs',
 'https://www.youtube.com/watch?v=dncyXvPR8uU',
 'https://www.youtube.com/watch?v=6DqJ1Wv6EtQ',
 'https://www.youtube.com/watch?v=7c-bWymbT04',
 'https://www.youtube.com/watch?v=SF_SwujfiYk',
 'https://www.youtube.com/watch?v=lLQZcx_lPzI',
 'https://www.youtube.com/watch?v=DLg2Q0daphE',
 'https://www.youtube.com/watch?v=rNcqLN42l8s',
 'https://www.youtube.com/watch?v=aoH1g5GYhPw',
 'https://www.youtube.com/watch?v=W_luzlgqYz0',
 'https://www.youtube.com/watch?v=I4xZUQmmMuI',
 'https://www.youtube.com/watch?v=L9HqHzA3atQ&t=77s',
 'https://www.youtube.com/watch?v=hJrEaLYacwc&t=2s',
 'https://www.youtube.com/watch?v=tFTA9MJZ4KY&t=10s',
 'https://www.youtube.com/watch?v=cIw8mH7ZpFY',
 'https://www.youtube.com/watch?v=rY9X6a-xxFo',
 'https://www.youtube.com/watch?v=7Yrrm5qccig',
 'https://www.youtube.com/watch?v=8yqa-SdJtT4&t=6974s',
 'https://www.youtube.com/watch?v=6vXVn8bK2wA',
 'https://www.youtube.com/watch?v=NrEOo1AZGso&t=114s',
 'https://www.youtube.com/watch?v=n_0LeJWdbi4',
 'https://www.youtube.com/watch?v=VXiLvPjeK1M',
 'https://www.youtube.com/watch?v=_ET7banSeN0',
 'https://www.youtube.com/watch?v=fFFSKedy9f4',
 'https://www.youtube.com/watch?v=0Zld-MX11lA',
 'https://www.youtube.com/watch?v=qGgEF-SlSEU']


#Adding new functionality
sad_words=["Sad", "sad", "depressed", "angry", "frustrated", "miserable", "depressing"]

encourage_words= ["Ok, Clean your room.", "Embrace The Chaos", "Rule-3: Treat yourself as someone you are responsible for helping"]


#creating/instantiating a discord client
client = discord.Client()

def get_quote():
  msg = random.choice(quotes)
  return (msg)

def get_video():
  src = random.choice(vids)
  return (src)

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

  if msg.startswith('$sauce'):
    truth = get_video()
    await message.channel.send(truth)

  if any (word in msg for word in sad_words):
    await message.channel.send(random.choice(encourage_words))


keep_alive()
client.run(os.environ['token'])

















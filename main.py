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
url2='https://www.youtube.com/c/JordanPetersonVideos/videos'
channelid = url2.split('/')[4]
chrome_options = Options()
driver=webdriver.Chrome('chromedriver',options=chrome_options)
driver.get(url2)
user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
videos= []
for e in user_data:
  vid = (e.get_attribute('href'))
  videos.append(vid)


#Adding new functionality
sad_words=["Sad", "sad", "depressed", "angry", "frustrated", "miserable", "depressing"]

encourage_words= ["Ok, Clean your room.", "Embrace The Chaos", "Rule-3: Treat yourself as someone you are responsible for helping"]


#creating/instantiating a discord client
client = discord.Client()

def get_quote():
  msg = random.choice(quotes)
  return (msg)

def get_video():
  src = random.choice(videos)
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

















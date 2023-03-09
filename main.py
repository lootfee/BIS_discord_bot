#bot_url = "https://discord.com/api/oauth2/authorize?client_id=1082714214596100166&permissions=274877975616&scope=bot"
import os
from dotenv import load_dotenv
import discord

from chat import getJavaReply, getTrumpReply

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = False
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send(f'Hello {message.author}!')

  if message.content.startswith('$java'):
    if len(message.content) > 2000:
      response = "Content must be 2000 or fewer in length"

    response = f"""```{getJavaReply(message.content.replace('$java', ''))}```"""

    await message.channel.send(response)

  if message.content.startswith('$trump'):
    if len(message.content) > 2000:
      response = "Content must be 2000 or fewer in length"

    response = f"{getTrumpReply(message.content.replace('$trump ', ''))}"

    await message.channel.send(response)


client.run(os.getenv('DISCORD_TOKEN'))

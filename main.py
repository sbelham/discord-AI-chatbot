from discord.utils import get
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from google import genai

load_dotenv()

llm =  genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
chat_sessions = {}
        
intents = discord.Intents.default()
intents.message_content = True

Talos = commands.Bot(command_prefix='€', intents=intents)

@Talos.event
async def on_ready():
    await Talos.change_presence(activity=discord.Game(name="Wooden Ocean"))
    print(f'Logged in as {Talos.user}')

@Talos.event
async def on_message(message):
    if message.author == Talos.user:
        return
    
    if message.content.startswith(Talos.command_prefix + 'test'):
        await message.channel.send(f"test")

    if Talos.user in message.mentions:
        channel_id = message.channel.id

        if channel_id not in chat_sessions:
            chat_sessions[channel_id] = llm.chats.create(
                model="models/gemma-3-27b-it",
                config={'temperature': 0.7,}
            )

        chat = chat_sessions[channel_id]

        history = chat.get_history()
        
        if not history:
            persona = """You are a person in a Discord chat. 
                        Users will message you in the format 'Name: Message'. 
                        Do NOT repeat the user's name or their message. 
                        Do NOT use a prefix like 'Bot:' or 'Model:' in your response. 
                        Just reply naturally and informally as yourself. Reply in the same language as the message. If the message is in spanish, you HAVE to reply in spanish. """
            
            input = f"{persona}{message.author.name}: {message.content}"
        else:
            input = f"{message.author.name}: {message.content}"

        response = chat.send_message(input)
            
        await message.channel.send(response.text)

    if not message.content.startswith(Talos.command_prefix):
        return

Talos.run(os.getenv("DISCORD_TOKEN"))
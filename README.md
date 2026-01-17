# discord-AI-chatbot
A basic conversational Discord bot with memory, context awareness, and user-specific interactions. Powered by Gemma, Google's open and lightweight AI model.

## How to setup
- Create a new Discord application on [Discord's developer portal](https://discord.com/developers/applications).
- Copy the application's token and add it to a .env file
- Get an API key from [Google AI Studio](https://aistudio.google.com/)
- Add the API key to the .env file

.env file will look like this
```
DISCORD_TOKEN='[APP TOKEN HERE]'
GOOGLE_API_KEY='[YOUR API KEY HERE]'
```
- Execute run.bat file

## What does it do?
This bot lets users chat with an AI directly in Discord. It keeps track of conversation history per server channel and responds individually to each user.

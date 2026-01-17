# discord-AI-chatbot
A basic conversational Discord bot with memory, context awareness, and user-specific interactions. Powered by Gemma, Google's open and lightweight AI model.

## What does it do?
This bot lets users chat with an AI directly in Discord using Google's API. It keeps track of conversation history per server channel and responds individually to each user.

Uses Google’s GenAI SDK to integrate Google's generative models into the Python app. Defaults to the Gemma 3 27b model for its higher free request limit (15k per day); this can be modified easily in the code.

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



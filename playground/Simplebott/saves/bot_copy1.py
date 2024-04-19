import discord
from discord import File
from gtts import gTTS
from pytube import YouTube

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hellod!")

    if message.content.startswith("$pusia"):
        await message.channel.send("Pusia")

    if message.content.startswith("$Zadanie domowe"):
        await message.channel.send("No to zrób")

    if message.content.startswith("$Jezyk"):
        await message.channel.send("W jakim")

    """
    if message.content.startswith('$generate_audio'):
        text = message.content.replace('$generate_audio', '').strip()
        filename = 'audio.mp3'
        tts = gTTS(text=text, lang='pl')
        tts.save(filename)
        
        file = File(filename)
        await message.channel.send(file=file)
    """
    if message.content.startswith("$audio"):
        text = message.content.replace("$audio", "").strip()
        if text == ("jak masz na imie"):
            text = "mam na imie alexa"
        if text == ("dokąd nocą tupta jeż"):
            text = "idzie jeść"
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        await message.channel.send(text)
        await message.channel.send(file=file)

    if message.content.startswith("$link"):
        text = message.content.replace("$link", "").strip()
        if text == ("jak masz na imie"):
            text = "mam na imie alexa"
        if text == ("dokąd nocą tupta jeż"):
            text = "https://www.youtube.com/watch?v=FDgfMEs_QGM"
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        await message.channel.send(text)
        # await message.channel.send(file=file)


client.run()

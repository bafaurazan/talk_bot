import discord
from discord import File
from gtts import gTTS
from pytube import YouTube
import asyncio

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
        await message.channel.send("Hello world!")

    if message.content.startswith("$text"):
        text = message.content.replace("$text", "").strip()
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
        if text == ("karta graficzna KNML"):
            text = "https://www.youtube.com/watch?v=akh7ddPydSM"
        if text == ("dokąd nocą tupta jeż"):
            text = "https://www.youtube.com/watch?v=FDgfMEs_QGM"
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        await message.channel.send(text)

    if message.content.startswith("$mbot"):
        text = message.content.replace("$mbot", "").strip()
        if text == ("jak masz na imie"):
            text = "mam na imie kamil"
        if text == ("dokąd nocą tupta jeż"):
            text = "idzie jeść"
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        if message.author.voice is None:
            await message.send(
                "Musisz być połączony z kanałem głosowym, aby użyć tej komendy."
            )
            return

        voice_channel = await message.author.voice.channel.connect()

        try:
            voice_channel.play(
                discord.FFmpegPCMAudio(filename), after=lambda e: print("done", e)
            )
            while voice_channel.is_playing():
                await asyncio.sleep(1)

        finally:
            await voice_channel.disconnect()


client.run()

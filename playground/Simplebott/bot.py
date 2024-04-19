import discord
from discord import File
from gtts import gTTS
from pytube import YouTube
import asyncio

import pyaudio
import speech_recognition as sr
import wave

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)
recognizer = sr.Recognizer()

# Ustawienia dla przechwytywania dźwięku
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "output.wav"


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$text"):
        text = message.content.replace("$text", "").strip()
        if text == "jak masz na imie":
            text = "mam na imie alexa"
        if text == "dokąd nocą tupta jeż":
            text = "idzie jeść"
        if text == "jaki mam plan zajęć w tym tygodniu":
            text = """
Poniedziałek             | Wtorek                   | Środa                | Czwartek        | Piątek                   \n 
Algorytmy                |   wstęp do programowania | analiza matematyczna | algebra liniowa | technologie informacyjne \n
Algorytmy                |   wstęp do programowania | analiza matematyczna | algebra liniowa | technologie informacyjne \n
Algorytmy                |   wstęp do programowania | analiza matematyczna | algebra liniowa | technologie informacyjne \n
Algorytmy                |   wstęp do programowania | analiza matematyczna | algebra liniowa | technologie informacyjne \n
Algorytmy                |   wstęp do programowania | analiza matematyczna | algebra liniowa | technologie informacyjne \n
                    """

        # file = File(filename)
        await message.channel.send(text)
        # await message.channel.send(file=file)

    if message.content.startswith("$link"):
        text = message.content.replace("$link", "").strip()
        if text == "karta graficzna KNML":
            text = "https://www.youtube.com/watch?v=akh7ddPydSM"
        if text == "dokąd nocą tupta jeż":
            text = "https://www.youtube.com/watch?v=FDgfMEs_QGM"
        if text == "jak zainstalować ffmpeg":
            text = "https://www.youtube.com/watch?v=N8IV5--vle4"
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        await message.channel.send(text)

    if message.content.startswith("$mbot"):
        text = message.content.replace("$mbot", "").strip()
        if text == "jak masz na imie":
            text = "mam na imie kamil"
        if text == "dokąd nocą tupta jeż":
            text = "idzie jeść"
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        if message.author.voice is None:
            await message.channel.send(
                "Musisz być połączony z kanałem głosowym, aby użyć tej komendy."
            )
            return
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
        if not voice_client:
            voice_client = await message.author.voice.channel.connect()
        voice_client.play(
            discord.FFmpegPCMAudio(filename), after=lambda e: print("done", e)
        )


@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:  # Użytkownik dołączył do kanału głosowego
        voice_channel = after.channel
        if (
            len(voice_channel.members) == 1
        ):  # Sprawdź, czy jest tylko jeden użytkownik w kanale
            voice_client = (
                await voice_channel.connect()
            )  # Połącz bota z kanałem głosowym
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
            )
            print("Nasłuchiwanie...")
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            print("Nagrywanie zakończone")

            # Zapisz przechwycony dźwięk do pliku WAV
            waveFile = wave.open(WAVE_OUTPUT_FILENAME, "wb")
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b"".join(frames))
            waveFile.close()

            # Wykonaj analizę mowy na nagranym pliku WAV
            with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
                audio_data = recognizer.record(source)  # Przechwyć dźwięk
                try:
                    text = recognizer.recognize_google(audio_data, language="pl-PL")
                    if "kamil" in text.lower():
                        print("Wykryto słowo kluczowe 'kamil':", text)
                        # Tutaj możesz wywołać odpowiednią reakcję
                        if "dokąd nocą tupta jeż" in text.lower():
                            text = "idzie jeść"
                        if "jak masz na imię" in text.lower():
                            text = "mam na imie kamil"
                        filename = "audio.mp3"
                        tts = gTTS(text=text, lang="pl")
                        tts.save(filename)

                        file = File(filename)
                        # if message.author.voice is None:
                        #    await message.channel.send("Musisz być połączony z kanałem głosowym, aby użyć tej komendy.")
                        #    return
                        # voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
                        # if not voice_client:
                        #    voice_client = await message.author.voice.channel.connect()
                        voice_client.play(
                            discord.FFmpegPCMAudio(filename),
                            after=lambda e: print("done", e),
                        )
                except sr.UnknownValueError:
                    print("Nie udało się rozpoznać mowy")
                except sr.RequestError:
                    print("Błąd serwera rozpoznawania mowy")

            stream.stop_stream()
            stream.close()
            audio.terminate()

    elif before.channel and not after.channel:  # Użytkownik opuścił kanał głosowy
        voice_client = discord.utils.get(
            client.voice_clients, guild=before.channel.guild
        )
        if (
            voice_client and len(voice_client.channel.members) == 1
        ):  # Sprawdź, czy nie ma już żadnego użytkownika w kanale
            await voice_client.disconnect()  # Rozłącz bota z kanałem głosowym
        # print(len(voice_client.channel.members))


@client.event
async def on_voice_server_update(payload):
    pass  # Możemy zignorować to wydarzenie


client.run()

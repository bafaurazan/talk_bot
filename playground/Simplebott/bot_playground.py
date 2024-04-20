import time

import discord
from discord import File
from discord.ext import commands
from gtts import gTTS
from pytube import YouTube
import asyncio

import pyaudio
import speech_recognition as sr
import wave
import os

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)
recognizer = sr.Recognizer()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

voice_client = None
frames = []
audio = pyaudio.PyAudio()
is_recording = False


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    global is_recording, audio, frames

    if message.author == client.user:
        return

    if message.content.startswith("$start"):
        if not is_recording:
            stream = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
            )
            is_recording = True
            frames = []
            print("Nasłuchiwanie...")
            while is_recording:
                data = stream.read(CHUNK)
                frames.append(data)
                print(is_recording)
                await asyncio.sleep(0.01)

            stream.stop_stream()
            stream.close()
            await message.channel.send("Nagrywanie zakończone.")

            with wave.open(WAVE_OUTPUT_FILENAME, "wb") as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(audio.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b"".join(frames))

            with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
                audio_data = recognizer.record(source)
                try:
                    input_text = recognizer.recognize_google(
                        audio_data, language="pl-PL"
                    )
                    output_text = ""
                    if "kamil" in input_text.lower():
                        print("Wykryto słowo kluczowe 'kamil':", input_text)
                        if "dokąd nocą tupta jeż" in input_text.lower():
                            output_text = "idzie jeść"
                        elif "jak masz na imię" in input_text.lower():
                            output_text = "mam na imie kamil"
                        else:
                            output_text = "Syna nie ma w domu"
                    else:
                        output_text = "Mówisz do mnie czy koło mnie, nazywam się Kamil"

                    filename = "audio.mp3"
                    tts = gTTS(text=output_text, lang="pl")
                    tts.save(filename)
                    file = File(filename)
                    voice_client.play(
                        discord.FFmpegPCMAudio(filename),
                        after=lambda e: print("done", e),
                    )

                except sr.UnknownValueError:
                    print("Nie udało się rozpoznać mowy")
                except sr.RequestError:
                    print("Błąd serwera rozpoznawania mowy")

    elif message.content.startswith("$stop"):
        if is_recording:
            is_recording = False
            await message.channel.send("Przerwano nagrywanie dynamicznie.")


@client.event
async def on_voice_state_update(member, before, after):
    global voice_client, audio

    if not before.channel and after.channel:
        voice_channel = after.channel
        if len(voice_channel.members) == 1:
            voice_client = await voice_channel.connect()

    elif before.channel and not after.channel:
        voice_client = discord.utils.get(
            client.voice_clients, guild=before.channel.guild
        )
        if voice_client and len(voice_client.channel.members) == 1:
            audio.terminate()
            await voice_client.disconnect()


@client.event
async def on_voice_server_update(payload):
    pass


client.run()

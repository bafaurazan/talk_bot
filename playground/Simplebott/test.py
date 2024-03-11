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

# Ustawienia dla przechwytywania dźwięku
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

Start_second_recording = False

frames = []
@client.event
async def on_ready():

    print(f'We have logged in as {client.user}')
    

is_recording = False

@client.event
async def on_message(message):
    global is_recording, audio_stream
    global frames, Start_second_recording

    if message.author == client.user:
        return


    if message.content.startswith('$start'):
        if is_recording:
            await message.channel.send("Nagrywanie już trwa.")
        else:
            asyncio.create_task(start_recording(message))

        

    if message.content.startswith('$stop'):
        if is_recording:
            stop_recording()
            await message.channel.send("Zakończono nagrywanie.")

async def start_recording(message):
    global frames, is_recording

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Nasłuchiwanie...")
    frames = []
    #for j in range(0,4):
    asyncio.create_task(record_audio())

async def record_audio():
    global frames  
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) 
    #await long_running_operation(message)

async def stop_recording(message):
    global frames, is_recording        
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    # Zapisz przechwycony dźwięk do pliku WAV
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
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
                    text = 'idzie jeść'
                if "jak masz na imię" in text.lower():
                    text = 'mam na imie kamil'
                filename = 'audio.mp3'
                tts = gTTS(text=text, lang='pl')
                tts.save(filename)
                
                file = File(filename)
                if message.author.voice is None:
                    await message.channel.send("Musisz być połączony z kanałem głosowym, aby użyć tej komendy.")
                    return
                voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
                if not voice_client:
                    voice_client = await message.author.voice.channel.connect()

                voice_client.play(discord.FFmpegPCMAudio(filename), after=lambda e: print('done', e))
        except sr.UnknownValueError:
            print("Nie udało się rozpoznać mowy")
        except sr.RequestError:
            print("Błąd serwera rozpoznawania mowy")

    stream.stop_stream()
    stream.close()
    audio.terminate()
    
async def long_running_operation(message):
    global Start_second_recording
    Start_second_recording = True
    print(f'We have logged in as {client.user}')
    print("sie wykonuje")
    if Start_second_recording == True:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print("Drugie Nasłuchiwanie...")
        #for j in range(0,4):
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data) 
        Start_second_recording = False

@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:  # Użytkownik dołączył do kanału głosowego
        voice_channel = after.channel
        if len(voice_channel.members) == 1:  # Sprawdź, czy jest tylko jeden użytkownik w kanale
            voice_client = await voice_channel.connect()  # Połącz bota z kanałem głosowym

    
    elif before.channel and not after.channel:  # Użytkownik opuścił kanał głosowy
        voice_client = discord.utils.get(client.voice_clients, guild=before.channel.guild)
        if voice_client and len(voice_client.channel.members) == 1:  # Sprawdź, czy nie ma już żadnego użytkownika w kanale
            await voice_client.disconnect()  # Rozłącz bota z kanałem głosowym
        #print(len(voice_client.channel.members))
@client.event
async def on_voice_server_update(payload):
    pass  # Możemy zignorować to wydarzenie

  
client.run('MTE3NjMxMTYwMjQxMzMyNjQ5OA.GPNrLh.g-Y9ieIiuobr4BeOUuR3D4LKzwoN4K5B5xhTsg')

            
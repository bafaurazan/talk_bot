import discord
from discord.ext import commands
from discord import File
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def hello(ctx):
    await ctx.send('Hello world!')

@client.command()
async def audio(ctx):
    # Sprawdź, czy autor komendy jest połączony z kanałem głosowym
    if ctx.author.voice is None:
        await ctx.send("Musisz być połączony z kanałem głosowym, aby użyć tej komendy.")
        return

    # Połącz się z kanałem głosowym autora komendy
    voice_channel = await ctx.author.voice.channel.connect()

    try:
        # Odtwórz plik audio.mp3
        audio_file = 'audio.mp3'
        voice_channel.play(discord.FFmpegPCMAudio(audio_file), after=lambda e: print('done', e))

        # Oczekuj, aż odtwarzanie zostanie zakończone
        while voice_channel.is_playing():
            await asyncio.sleep(1)

    finally:
        # Rozłącz się z kanałem głosowym po zakończeniu odtwarzania
        await voice_channel.disconnect()

client.run('MTE3NjMxMTYwMjQxMzMyNjQ5OA.GYAf3G.T1kMqxgCo7007qZOq060zpg3fCNAzZZZ4t7joM')

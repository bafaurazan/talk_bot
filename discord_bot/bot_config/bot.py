"""Defining discord bot functionality"""

import os
import requests
import subprocess
import discord
from discord import File
from gtts import gTTS

from dotenv import dotenv_values

config = dotenv_values()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """getting information about client user name"""
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    """Bot response for specified input"""
    if message.author == client.user:
        return


    response = requests.get("http://localhost:8000/api/document/")
    data = response.json()

    for item in data['items']:
        command = item['command']
        command_id = item['id']


    if message.content.startswith("$"):
        search_term = message.content[1:]
        url = f'http://localhost:8000/api/document/{command_id}/eval/'

        response = requests.get(url)
        await message.channel.send(f"Done.")


    if message.content.startswith("$hello"):
        await message.channel.send("Hellod!")

    if message.content.startswith("$pusia"):
        await message.channel.send("Pusia")

    if message.content.startswith("$Zadanie domowe"):
        await message.channel.send("No to zrób")

    if message.content.startswith("$Jezyk"):
        await message.channel.send("W jakim")

    if message.content.startswith("$k1"):
        os.system("open firefox")

    if message.content.startswith("$k2"):
        subprocess.run(
            [
                "C:/Program Files/Git/git-bash",
                "-c",
                "C:/maxima-5.45.1/bin/wxmaxima.exe",
            ],
            capture_output=True,
            shell=False,
            check=True,
        )

        print(message.author)
        print(client.user)

    if message.content.startswith("$k3"):
        subprocess.run(
            ["C:/Program Files/Git/git-bash", "-c", "nano"],
            shell=True,
            capture_output=True,
            check=True,
        )

    if message.content.startswith("$k4"):
        subprocess.run(
            [
                "C:/Program Files/Git/git-bash",
                "-c",
                "open C:/Program Files/Image-Line/FL Studio 20/FL64.ex",
            ],
            capture_output=True,
            shell=False,
            check=True,
        )


    if message.content.startswith("$generate_audio"):
        text = message.content.replace("$generate_audio", "").strip()
        filename = "audio.mp3"
        tts = gTTS(text=text, lang="pl")
        tts.save(filename)

        file = File(filename)
        await message.channel.send(file=file)


def mainbot():
    """Entrypoint."""
    client.run(config["TOKEN"])


if __name__ == "__main__":
    mainbot()

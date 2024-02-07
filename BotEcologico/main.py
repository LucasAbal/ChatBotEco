# main_logic.py
from bot_logic import *
from settings import settings
import discord
import os
import requests
import aiohttp
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!noticias'):
        if message.channel.name == "ultimas-noticias":
            print(f'Recibido mensaje: {message.content} en el canal: {message.channel.name}')
            async with aiohttp.ClientSession() as session:
                async with session.get("https://concepto.de/medio-ambiente/") as response:
                    soup = BeautifulSoup(await response.text(), 'html.parser')

            news_items = soup.find_all('div', class_='module-news')

            for item in news_items:
                title = item.find('h2').get_text()
                link = item.find('a')['href']
                await message.channel.send(f'**{title}**\n{link}')
            print(f"recibido: {news_items}")
        else:
            await message.channel.send("Este comando solo está permitido en el canal #ultimas-noticias.")
    else:
        await message.channel.send("No puedo procesar este comando")

    # Foros
    if message.content.startswith('!foros'):
        # Verifica si el mensaje se envió en el canal correcto
        if message.channel.name == "foros":
            # Divide el mensaje en partes usando espacio como delimitador
            command_parts = message.content.split(' ', 1)

            # Verifica si hay al menos dos partes después de la división
            if len(command_parts) >= 2:
                _, tipo = command_parts
                tipo = tipo.lower()
                forums = await obtener_foros(tipo)

                if not forums:
                    await message.channel.send(f"No se encontraron foros para el tema '{tipo}'.")
                    return

                for forum in forums:
                    forum_title = forum['title']
                    forum_url = forum['url']
                    forum_image_filename = forum['image_filename']
                    forum_synopsis = forum['synopsis']

                    script_directory = os.path.dirname(os.path.abspath(__file__))
                    image_path = os.path.join(script_directory, 'img', forum_image_filename)

                    message_content = (
                        f"**Título:** {forum_title}\n"
                        f"**Enlace:** {forum_url}\n"
                        f"**Sinopsis:** {forum_synopsis}"
                    )

                    with open(image_path, 'rb') as image_file:
                        image = discord.File(image_file)
                        await message.channel.send(message_content, file=image,)
                        await message.channel.send(gif())
            else:
                await message.channel.send("Por favor, proporcione un tema después de !foros. (ambientales, manualidad, reciclo)")
        else:
            await message.channel.send("Este comando solo está permitido en el canal #foros.")

def obtener_noticias():
    try:
        # Hacer una solicitud GET a la URL de las noticias
        response = requests.get("https://www.infobae.com/america/medio-ambiente/2024/02/06/el-conmovedor-regreso-al-mar-de-un-lobo-marino-rehabilitado-tras-sufrir-una-grave-herida/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Encuentra todos los elementos de noticias y los devuelve como una lista de cadenas de texto
            noticias = [noticia.text.strip() for noticia in soup.find_all('h3', class_='headline-title')]
            return noticias
        else:
            print("Error al obtener las noticias - Código de estado:", response.status_code)
    except Exception as e:
        print("Error al obtener las noticias:", e)
    return None

client.run(settings["TOKEN"])


import os
import discord
from bot_logic import *

async def comando_foros(message):
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
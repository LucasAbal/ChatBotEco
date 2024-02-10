# ayuda_logic.py
import discord

async def enviar_videos_ayuda(message):

    if message.channel.name == "ayuda":
        if message.content.startswith('!ayuda plantación'):
            await message.channel.send("¡Aquí tienes algunos vídeos relacionados con la plantación!")
            await message.channel.send("Video 1: ENRAIZA CUALQUIER PLANTA RÁPIDO y FÁCIL https://www.youtube.com/watch?v=YsKUns-UKfo")
            await message.channel.send("Video 2: CULTIVO FÁCIL: SÓLO TIERRA https://www.youtube.com/watch?v=9t6OXMWSZdQ")
        
        
        elif message.content.startswith('!ayuda ambiente'):
            await message.channel.send("¡Aquí tienes algunos vídeos relacionados con el cuidado del medio ambiente!")
            await message.channel.send("Video 1: La IMPORTANCIA de CUIDAR el MEDIO AMBIENTE 🌏🌿 https://www.youtube.com/watch?v=YWLLeZzVAZU")
            await message.channel.send("Video 2: ¿Qué es el MEDIO AMBIENTE y cómo cuidarlo? Características e importancia 🌳 https://www.youtube.com/watch?v=0V8Yv5ckzT8")

        
        elif message.content.startswith('!ayuda manualidad'):
            await message.channel.send("¡Aquí tienes algunos vídeos relacionados con manualidades ecológicas!")
            await message.channel.send("Video 1: 20 MANUALIDADES con BOTELLAS DE PLÁSTICO ♻️ IDEAS CON RECICLAJE ♻️ https://www.youtube.com/watch?v=xCaI-5WVRlY")
            await message.channel.send("Video 2: 15 MARAVILLOSAS IDEAS para RECICLAR BOTELLAS GRANDES! https://www.youtube.com/watch?v=wgVhEcMkCiY")
        
        elif message.content.startswith('!ayuda'):
            await message.channel.send("Por favor, proporcione un tema después de !ayuda. (plantación, ambiente, manualidad)")
    else:
        await message.channel.send("Este comando solo está permitido en el canal #ayuda.")  

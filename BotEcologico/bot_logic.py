import random

async def obtener_foros(tipo):
    Foros_Ambientales = {
        'ambientales': [
            {
                'title': 'Foros Ambientales',
                'url': 'https://www.forosambientales.com/foros/',
                'image_filename': 'foros_ambientales_logo_2016.png',
                'synopsis': 'Varios Foros donde se habla del medio ambiente.'
            },
        ],
        'manualidad': [
            {
                'title': 'Foro de Manualidades',
                'url': 'https://www.europapress.es/desconecta/lifestyle/noticia-20-manualidades-diy-dia-mundial-medio-ambiente-20150605100539.html',
                'image_filename': 'Desconecta.png',
                'synopsis': 'Comunidad dedicada a compartir ideas y proyectos de manualidades.'
            },
        ],
        'reciclo': [
            {
                'title': 'Foro de Reciclaje',
                'url': 'https://www.fororeciclaje.com/',
                'image_filename': 'Logo-RIGK-d.png',
                'synopsis': 'Foro para discutir sobre prácticas y consejos de reciclaje.'
            },
        ] ,
    }
    return Foros_Ambientales.get(tipo, [])

def gif():
    gifs = ["https://tenor.com/view/this-is-not-fine-everything-is-fine-earth-globe-everything-is-fine-meme-gif-18398512","https://tenor.com/view/earth-day-happy-earth-day-lcvearthday-lcv-climate-gif-21179217","https://tenor.com/view/world-earth-world-earth-day-earthday-save-earth-gif-20779347","https://tenor.com/view/green-environment-pollution-change-gif-5456186","https://tenor.com/view/mother-earth-climate-warrior-world-environment-day-environment-earth-gif-17392098","https://tenor.com/view/climate-climate-change-climate-crisis-global-warming-pollution-gif-22652623","https://tenor.com/view/qu%C3%A9privilegio-vivir-en-esta-tierra-tierra-d%C3%ADa-de-la-tierra-feliz-d%C3%ADa-de-la-tierra-lcvearthday-gif-21191729","https://tenor.com/view/there-is-no-planet-b-climate-change-vote-earth-election-gif-21258651"]
    
    return random.choice(gifs)

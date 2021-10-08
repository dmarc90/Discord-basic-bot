import discord
import os
import requests
import json


client = discord.Client()

def get_quote():
    response = requests.get("http://allugofrases.herokuapp.com/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data [0] ['a']
    return(quote)

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!oi'):
        await message.channel.send('Opa, e aí meu consagrado(a)! Curta nosso clube de leitura e leia as #regras')

    if message.content.startswith('!fraselivro'):
        quote = get_quote()
        await message.channel.send(quote)


client.run(os.getenv('TOKEN'))
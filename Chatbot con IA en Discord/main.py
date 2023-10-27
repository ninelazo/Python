import discord
from discord.ext import commands
import asyncio
import openai
import json


# Read API Key OpenAI
def load_api_key(secrets_file="secrets.json"):
    with open(secrets_file) as f:
        secrets = json.load(f)
    return secrets["OPENAI_API_KEY"]


# Load API key OpenAI
api_key = load_api_key()
openai.api_key = api_key

# Intents connection server discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True


# Definde prefix for commands
bot = commands.Bot(command_prefix="!",  intents=intents)
client = discord.Client(intents=intents)

# Start connection with Discord
token = "TOKEN"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(description="Saluda al bot")
async def hola(ctx):
    await ctx.send(f"Hola {ctx.author.global_name}")


@bot.command(description="Muestra la fecha en la que se uníó un miembro al canal.")
async def desde(ctx, member: discord.Member):
    await ctx.send(f"{member.name} se unio {discord.utils.format_dt(member.joined_at)}")


@bot.command(description="Recibe una pregunta desde Discord y contesta con una respuesta generada por la IA de OpenIA")
async def buscar(ctx, *args):

    # Creamos una variable string donde unimos todas las palabras recibidas desde DC.
    string = ""

    for word in args:
        string = string + word + " "

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": string}
        ]
    )
    respuesta = completion.choices[0].message["content"]

    #Usamos try, except para tratar de reproducir la respuesta al canal de voz.
    try:
        channel = ctx.message.author.voice.channel
        await ctx.send(respuesta, tts=True)

    except:
        await ctx.send(respuesta)



@bot.command(description="El bot se une al canal de voz.")
async def voz(ctx):

    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Lo siento, no puedo unirme a un canal de voz al que no estas conectado.")


@bot.command(description="Reproduce la musica que hay descargada en una carpeta local")
async def musica(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("INTODUZCA DIRECTORIO MUSICA"))
    ctx.voice_client.play(source)


bot.run(token)

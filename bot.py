from unittest import async_case
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as BS 
import random
import json
import getmeme
import covid_data as cdata
from google_images_search import GoogleImagesSearch
from bot_tokens import discord_bot_token, google_api_key, google_cse_key, weather_api_key
from googletrans import Translator

client = commands.Bot(command_prefix="$")

@client.listen('on_message')
async def bot_mentioned(message):
    if client.user.mentioned_in(message):
        await message.channel.send("You can type `$help` for more info")

@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed()
        em.title = "Command not found"
        em.description = "The command you are looking for is not found. Use **$help** to get a list of all available commands."
        em.color = ctx.author.color
        await ctx.send(embed=em)

class MusicCommands(commands.Cog, name="Music commands"):
    @commands.command()
    async def join(self, ctx):
        '''Joins a voice channel'''
        if ctx.author.voice is None:
            em = discord.Embed()
            em.description = "You need to join a voice channel first!"
            em.color = ctx.author.color
            await ctx.send(embed=em)

        if ctx.voice_client is not None:
            em = discord.Embed()
            em.description = "I am already connected to a voice channel!"
            em.color = ctx.author.color
            await ctx.send(embed=em)

        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        '''Leaves a voice channel'''
        if ctx.voice_client is None:
            em = discord.Embed()
            em.description = "I am not in any voice channel"
            em.color = ctx.author.color
            await ctx.send(embed=em)

        await ctx.voice_client.disconnect()

class misc_commands(commands.Cog, name="Miscellaneous Commands"):
    @commands.command()
    async def ask(self, ctx, *,question):
        '''Gives random answers to your questions'''
        responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
        await ctx.send(f'**Question:** {question}\n**Answer:** {random.choice(responses)}')

    @commands.command()
    async def fml(self, ctx):
        '''Gives a funny random fml'''
        res = requests.get("https://www.fmylife.com/random")
        soup = BS(res.text)
        await ctx.send(soup.select_one('.block text-blue-500 my-4 ').text)

    @commands.command()
    async def slap(self, ctx, members: commands.Greedy[discord.Member],*, reason="Cuz why not" ):
        slapped = ", ".join(x.name for x in members)
        await ctx.send(f"{slapped} just got slapped for {reason}")

    @commands.command()
    async def ping(self, ctx):
        '''Tells the ping'''
        await ctx.send(f"Your ping is {round(client.latency * 1000)}ms")

    @commands.command()
    async def img(self, ctx, *,query):
        '''Search for a image related to your query'''
        gis = GoogleImagesSearch(google_api_key, google_cse_key)
        _search_params = {
            'q' : query,
            'num' : 3,
            'safe' : 'off'
        }
        gis.search(search_params=_search_params)
        embed = discord.Embed(title=query)
        embed.set_image(url=gis.results()[0].url)
        await ctx.send(embed=embed)

class utility_commands(commands.Cog, name="Useful commands"):
    @commands.command()
    async def weather(self, ctx, city):
        '''Tells weather of the given city'''
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        resp = requests.get(url)
        data = resp.json()
        try:
            resonse = f'''
**City:**  {data['name']}
**Country:**  {data['sys']['country']}
**Condition:**  {data['weather'][0]['main']}
**Temperature:**  {data['main']['temp']}°C
**Humidity:**  {data['main']['humidity']}%
**Minimum Temperature:**  {data['main']['temp_min']}°C
**Maximum Temperature:**  {data['main']['temp_max']}°C'''
            await ctx.send(resonse)
        except KeyError:
            await ctx.send("**City not found**")

    @commands.command()
    async def trans(self, ctx, lang, *message):
        '''Translates text into the given language'''
        translator = Translator()
        try:
            tr = translator.translate(" ".join(message), dest=lang)
            await ctx.send(tr.text)
        except ValueError:
            await ctx.send("An error occured. Please check the language code and try again! Check language codes: https://cloud.google.com/translate/docs/languages")

class meme_commands(commands.Cog, name="Meme Commands"):
    @commands.command()
    async def dankmeme(self, ctx):
        '''Gives a fresh dank meme'''
        meme = random.choice(getmeme.get_dank_meme_list())
        embed = discord.Embed(title=meme.title)
        embed.set_image(url=meme.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        '''Also meme, less dank'''
        meme = random.choice(getmeme.get_meme_list())
        embed = discord.Embed(title=meme.title)
        embed.set_image(url=meme.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def darkjoke(self, ctx):
        '''Tells a dark joke, **NSFW**'''
        if ctx.channel.is_nsfw():
            joke_title, joke_text = getmeme.dark_joke()
            joke = f"{joke_title} \n{joke_text}"
            await ctx.send(joke)
        else:
            await ctx.send("You cannot use this command here. Go to a nsfw channel")
    
    @commands.command()
    async def darkmeme(self, ctx):
        '''Dark Meme **nsfw**'''
        meme = random.choice(getmeme.get_dark_meme())
        embed = discord.Embed(title=meme.title)
        embed.set_image(url=meme.url)
        await ctx.send(embed=embed)

class covid_data(commands.Cog, name="Covid Updates"):
    @commands.command()
    async def totalcases(self, ctx):
        '''Get total number of cases'''
        data = cdata.get_data_world()
        re_str = '''

:globe_with_meridians: **Total Confirmed Cases:** {:,}
:red_circle: **Total Deaths:** {:,}
:green_circle: **Total Recoveries:** {:,}'''.format(data['TotalConfirmed'], data['TotalDeaths'],data['TotalRecovered'] )

        await ctx.send(re_str)

    @commands.command()
    async def bycountry(self, ctx, country):
        '''Get number of cases by country'''
        data = cdata.get_data_by_country(country)
        country_code = data['CountryCode'].lower()
        if len(data) != 0:
            re_str = '''
            
:flag_{}: **Country:** {}
:grey_exclamation: **Confirmed Cases:** {:,}
:red_circle: **Deaths: ** {:,}
:green_circle: **Recoveries:** {:,}'''.format(country_code, data['Country'], data['TotalConfirmed'], data['TotalDeaths'], data['TotalRecovered'])
            await ctx.send(re_str)
        else:
            ctx.send("**No data found for the given country**")

client.add_cog(MusicCommands(client))
client.add_cog(meme_commands(client))
client.add_cog(utility_commands(client))
client.add_cog(misc_commands(client))
client.add_cog(covid_data(client))

print("Bot is running!")
client.run(discord_bot_token)

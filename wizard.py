import discord
from discord.ext import commands
from functions import *
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

bot = commands.Bot(command_prefix='!')


# Define a function to handle Discord messages
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

  import discord
from discord.ext import commands
from gamedaybot.espn.functionality import *

bot = commands.Bot(command_prefix='!')

@bot.command(aliases=['gs'])
async def get_scoreboard(ctx):
    result = get_scoreboard_short(league, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_projected_scoreboard(ctx):
    result = get_projected_scoreboard(league, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_standings(ctx):
    result = get_standings(league, top_half_scoring=False, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def top_half_wins(ctx):
    result = top_half_wins(league, top_half_totals, week)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_projected_total(ctx):
    result = get_projected_total(lineup)
    await ctx.send(result)

@bot.command(aliases=[])
async def all_played(ctx):
    result = all_played(lineup)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_monitor(ctx):
    result = get_monitor(league)
    await ctx.send(result)

@bot.command(aliases=[])
async def scan_roster(ctx):
    result = scan_roster(lineup, team)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_matchups(ctx):
    result = get_matchups(league, random_phrase=False, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_close_scores(ctx):
    result = get_close_scores(league, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_waiver_report(ctx):
    result = get_waiver_report(league, faab=False)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_power_rankings(ctx):
    result = get_power_rankings(league, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_starter_counts(ctx):
    result = get_starter_counts(league)
    await ctx.send(result)

@bot.command(aliases=[])
async def best_flex(ctx):
    result = best_flex(flexes, player_pool, num)
    await ctx.send(result)

@bot.command(aliases=[])
async def optimal_lineup_score(ctx):
    result = optimal_lineup_score(lineup, starter_counts)
    await ctx.send(result)

@bot.command(aliases=[])
async def optimal_team_scores(ctx):
    result = optimal_team_scores(league, week=None, full_report=False)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_achievers_trophy(ctx):
    result = get_achievers_trophy(league, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_lucky_trophy(ctx):
    result = get_lucky_trophy(league, week=None)
    await ctx.send(result)

@bot.command(aliases=[])
async def get_trophies(ctx):
    result = get_trophies(league, week=None)
    await ctx.send(result)
    
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(os.environ.get("DISCORD_TOKEN"))

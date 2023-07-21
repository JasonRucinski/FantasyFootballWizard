import discord
from discord.ext import commands
import functions  # The functions from your file

# Create instance of bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)  # Use "!" as the command prefix

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def test(ctx):
    """A simple test command to ensure the bot is working."""
    await ctx.send("Bot is connected and responding to commands.")

@bot.command()
async def get_standings(ctx):
    """Bot command to get current team standings in the league."""
    standings = functions.get_standings()
    await ctx.send(standings)

@bot.command()
async def top_half_wins(ctx):
    result = functions.top_half_wins()
    await ctx.send(result)

@bot.command()
async def get_projected_total(ctx):
    result = functions.get_projected_total()
    await ctx.send(result)

@bot.command()
async def all_played(ctx):
    result = functions.all_played()
    await ctx.send(result)

@bot.command()
async def get_monitor(ctx):
    result = functions.get_monitor()
    await ctx.send(result)

@bot.command()
async def scan_roster(ctx):
    result = functions.scan_roster()
    await ctx.send(result)

@bot.command()
async def get_matchups(ctx):
    result = functions.get_matchups()
    await ctx.send(result)

@bot.command()
async def get_close_scores(ctx):
    result = functions.get_close_scores()
    await ctx.send(result)

@bot.command()
async def get_waiver_report(ctx):
    result = functions.get_waiver_report()
    await ctx.send(result)

@bot.command()
async def get_power_rankings(ctx):
    result = functions.get_power_rankings()
    await ctx.send(result)

@bot.command()
async def get_starter_counts(ctx):
    result = functions.get_starter_counts()
    await ctx.send(result)

@bot.command()
async def best_flex(ctx):
    result = functions.best_flex()
    await ctx.send(result)

@bot.command()
async def optimal_lineup_score(ctx):
    result = functions.optimal_lineup_score()
    await ctx.send(result)

@bot.command()
async def optimal_team_scores(ctx):
    result = functions.optimal_team_scores()
    await ctx.send(result)

@bot.command()
async def get_achievers_trophy(ctx):
    result = functions.get_achievers_trophy()
    await ctx.send(result)

@bot.command()
async def get_lucky_trophy(ctx):
    result = functions.get_lucky_trophy()
    await ctx.send(result)

@bot.command()
async def get_trophies(ctx):
    result = functions.get_trophies()
    await ctx.send(result)


# Run the bot
bot.run("YOUR_BOT_TOKEN")

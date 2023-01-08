import lightbulb
from lightbulb import SlashCommand, PrefixCommand, Context
import os
from dotenv import load_dotenv
from utils import get_random_quote
import hikari
load_dotenv()

token = os.environ["BOT_TOKEN"]
prefix = "g!"
bot = lightbulb.BotApp(token=token, prefix=prefix, ignore_bots=True)
bot.load_extensions("daily")

@bot.command
@lightbulb.command("cytat", "Losowy cytat z Wiedźmina.")
@lightbulb.implements(SlashCommand, PrefixCommand)
async def cytat(ctx: Context) -> None:
    await ctx.respond(get_random_quote())


bot.run()



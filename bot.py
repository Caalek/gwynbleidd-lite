from json import load
import lightbulb
from lightbulb import SlashCommand, PrefixCommand, Context
import os
import random
from dotenv import load_dotenv
import json
load_dotenv()

token = os.environ["BOT_TOKEN"]
prefix = "g!"
bot = lightbulb.BotApp(token=token, prefix=prefix)


def get_random_quote():
    with open("quotes.json", "r") as f:
        quote_array = json.load(f)
    return random.choice(quote_array)
    

@bot.command
@lightbulb.command("cytat", "Losowy cytat z Wiedźmina.")
@lightbulb.implements(SlashCommand, PrefixCommand)
async def cytat(ctx: Context) -> None:
    await ctx.respond(get_random_quote())

bot.run()



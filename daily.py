import lightbulb
import hikari
import datetime
import json
import random
from pytz import timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from utils import get_random_quote

daily_plugin = lightbulb.Plugin("Daily")
sched = AsyncIOScheduler()
sched.start()

# to są te bastionowe poniżej
channel_id = 1062439119243989064 #cytat-na-dzis
role_id = "1061774091809476658" # rola codzienny cytat

# codziennie o 6 rano
# @sched.scheduled_job(CronTrigger(second=2))
@sched.scheduled_job(CronTrigger(minute=0, hour=6, day="*", month="*", day_of_week="*"))
async def msg1() -> None:
    quote_obj = get_random_quote()
    embed = hikari.Embed(
        title=datetime.datetime.now(timezone('Europe/Warsaw')).strftime('%d.%m.%Y'),
        description=quote_obj["quote"],
        color=0xff0c00,
    )
    embed.set_thumbnail(quote_obj["image"])
    await daily_plugin.app.rest.create_message(channel_id, "<@&" + role_id + ">", embed=embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)
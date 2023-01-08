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

# ZMIENIĆ
channel_id = 466315952569450531

# codziennie o 6 rano
@sched.scheduled_job(CronTrigger(minute=0, hour=6, day="*", month="*", day_of_week="*"))
async def msg1() -> None:
    embed = hikari.Embed(
        title=datetime.datetime.now(timezone('Europe/Warsaw')).strftime('%d.%m.%Y'),
        description=get_random_quote(),
        color=0xff0c00,
    )
    await daily_plugin.app.rest.create_message(channel_id, embed=embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)
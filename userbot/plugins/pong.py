Uptime added by @Sur_vivor
from telethon import events
from datetime import datetime
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd
from userbot import CMD_HELP
from userbot import StartTime, catdef
import time
import asyncio

@borg.on(admin_cmd(pattern=f"fpin$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    animation_interval = 0.2
    animation_ttl = range(0, 26)
    await event.edit("ping....")
    animation_chars = [
        
                                                                                                                                                                                                    
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶❤️‎📶❤️❤️❤️‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶❤️‎📶❤️❤️❤️‎📶❤️ \n❤️❤️📶‎📶❤️❤️📶❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶❤️‎📶❤️❤️❤️‎📶❤️ \n❤️❤️📶‎📶❤️❤️📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶❤️‎📶❤️❤️❤️‎📶❤️ \n❤️❤️📶‎📶❤️❤️📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶❤️📶‎📶‎📶‎📶‎📶❤️",
            "❤️❤️❤️❤️❤️❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️‎📶❤️❤️📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️📶❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎📶‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️📶❤️❤️❤️❤️❤️‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️❤️‎📶❤️❤️ \n❤️❤️❤️❤️❤️‎📶❤️❤️❤️ \n❤️❤️❤️❤️📶❤️❤️❤️❤️ \n❤️‎📶‎📶‎📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️❤️‎📶‎📶‎📶‎📶‎📶❤️❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️📶‎❤️❤️❤️❤️❤️‎📶❤️ \n❤️‎📶❤️‎📶❤️❤️❤️‎📶❤️ \n❤️❤️📶‎📶❤️❤️📶❤️❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n❤️‎📶❤️📶‎📶‎📶‎📶‎📶❤️ \n❤️❤️❤️❤️❤️‎❤️❤️❤️❤️ \n \n My 🇵 🇮 🇳 🇬  Is : Calculating..."
 ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 26]) 
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("‎‎‎‎‎‎‎‎‎🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪📶📶📶📶📶📶📶🟪\n🟪🟦🟦🟦📶🟦🟦📶🟪\n🟪🟦🟦🟦📶🟦🟦📶🟪\n🟪🟦🟦🟦📶🟦🟦📶🟪\n🟪🟦🟦🟦🟦📶📶🟦🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪🟦📶📶📶📶📶🟦🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪🟦📶📶📶📶📶🟦🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪📶📶📶📶📶📶📶🟪\n🟪🟦🟦🟦🟦🟦📶🟦🟪\n🟪🟦🟦🟦🟦📶🟦🟦🟪\n🟪🟦🟦🟦📶🟦🟦🟦🟪\n🟪📶📶📶📶📶📶📶🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪🟦📶📶📶📶📶🟦🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦📶🟦🟦🟦📶🟪\n🟪🟦📶📶🟦🟦📶🟦🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪📶🟦📶📶📶📶📶🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n\n\n📥@Munnipopz📥\n‌‌‌‌‌‌‌‌‎ \n \n 🔥𝕄𝕪 𝕡𝕚𝕟𝕘 𝕚𝕤🔥 : {} ms".format(ms))
 

@borg.on(admin_cmd(pattern="pin$"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("🚀Ping!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    await event.edit(f"🚀Pong!\nPing Speed: {ms}\nUserbot Uptime: {uptime}")
        
CMD_HELP.update({
    "ping":
    "`.fping`\
    \nUSAGE:A kind of ping with extra animation\
    \n\n`.ping`\
    \nUSAGE:Shows you the ping speed of server"

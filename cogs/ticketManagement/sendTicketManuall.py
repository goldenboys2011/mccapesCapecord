import asyncio

import discord
from discord.ext import commands
import time
import re
import datetime

GUILD_ID    = 1378519415565320212
CAT_ID      = 1452646077760143512
CHAN_PRE    = "ticket"
TEXT        = """
Hello Person, please wait while we fetch the **MidleMan** team.

To **help us assist you efficiently**, please **provide** the **following details** while you wait:

- The **user or party you are transacting** with
- The **payment platform** you intend to use (e.g. PayPal <:paypal:1529204792021356655>, bank transfer :bank:, crypto wallet <:crypto:1529204748828410008>)
- The specific **currency** or **cryptocurrency** involved (e.g. USD, BTC, ETH)
- The **cape** or **account being traded**

Once support arrives, having this information already written will allow us to proceed without delay.
"""

class sendTicket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if (
            channel.guild.id != GUILD_ID
            or channel.category_id != CAT_ID
            or not channel.name.startswith(CHAN_PRE)
        ):
            return

        def check(message):
            return message.channel.id == channel.id

        try:
            message = await self.bot.wait_for(
                "message",
                check=check,
                timeout=300
            )
        except asyncio.TimeoutError:
            return

        userMentions = message.mentions 

        TEXT2 = TEXT.replace("Person", f"<@{userMentions[0].id}>")
        await channel.send(TEXT2)


async def setup(bot):
    await bot.add_cog(sendTicket(bot))
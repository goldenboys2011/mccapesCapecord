import discord
import datetime

def createVouchEmbed(vouch):
    embed = discord.Embed(
        title=f"Vouch #{vouch['id']}",
        color=0x2ECC71,
        timestamp=datetime.datetime.now()
    )

    embed.add_field(
        name="Voucher",
        value=f"<@{vouch['voucher']}>",
        inline=False
    )

    embed.add_field(
        name="Vouchee",
        value=f"<@{vouch['vouchee']}>",
        inline=False
    )

    embed.add_field(
        name="Message",
        value=f"```{vouch['message']}```",
        inline=False
    )

    embed.add_field(
        name="Verified?",
        value="✅ True" if vouch["verified"] else "❌ False",
        inline=False
    )

    return embed
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import discord
from discord.ext import commands
from cachetools import TTLCache

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
TOKEN = os.getenv("BOT_TOKEN")
supabase: Client = create_client(url, key)
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

client = commands.Bot(command_prefix="+", intents=intents)
tree = client.tree
member_cache = TTLCache(maxsize=1, ttl=300)

GUILD_ID = 1378519415565320212

@client.event
async def on_ready():
    # await tree.sync()

    guild = discord.Object(id=GUILD_ID)
    tree.copy_global_to(guild=guild)
    await tree.sync(guild=guild)
    print("READY")

async def load_extensions():
    await client.load_extension("cogs.vouch")
    client.supabase = supabase
    await client.load_extension("cogs.checkCode")
    await client.load_extension("cogs.capeRoles")
    await client.load_extension("cogs.vouches")

@client.event
async def setup_hook():
    await load_extensions()
    
client.run(TOKEN)
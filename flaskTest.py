import os

from dotenv import load_dotenv
from flask import Flask, redirect, request
import requests

load_dotenv()

app = Flask(__name__)

CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
GUILD_ID = os.getenv("GUILD_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route("/login")
def login():
    return redirect(
        f"https://discord.com/oauth2/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=identify%20guilds.join"
    )

@app.route("/auth/discord/callback")
def callback():
    code = request.args.get("code")

    token_data = requests.post(
        "https://discord.com/api/oauth2/token",
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
    ).json()

    access_token = token_data["access_token"]

    user = requests.get(
        "https://discord.com/api/users/@me",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    ).json()

    discord_id = user["id"]

    requests.put(
        f"https://discord.com/api/v10/guilds/{GUILD_ID}/members/{discord_id}",
        headers={
            "Authorization": f"Bot {BOT_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "access_token": access_token
        }
    )

    return redirect(
        f"/store"
        f"?sessionId={CLIENT_ID}"
    )

if __name__ == "__main__":
    app.run()
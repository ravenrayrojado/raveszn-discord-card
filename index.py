from fastapi import FastAPI
import os
import requests

app = FastAPI()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = "399904586824941568"


@app.get("/api")
def home():
    return {
        "status": "online",
        "message": "RAVESZN Discord Card API is working."
    }


@app.get("/api/stats")
def stats():
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}"
    }

    response = requests.get(
        f"https://discord.com/api/v10/guilds/{GUILD_ID}?with_counts=true",
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        return {
            "status": "error",
            "message": "Unable to get Discord server stats."
        }

    data = response.json()

    return {
        "name": data.get("name"),
        "icon": data.get("icon"),
        "members": data.get("approximate_member_count", 0),
        "online": data.get("approximate_presence_count", 0)
    }

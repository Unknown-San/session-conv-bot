import os
from pyrogram import Client
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    app = Client(
        ":memory:",
        api_id=os.environ.get("API_ID", 4665778),
        api_hash=os.environ.get("API_HASH", "10e3ed833b0d09699973420d45359409"),
        bot_token=os.environ.get("BOT_TOKEN", "5343045120:AAFx4-CSTguKQXWZFUG13mrjuRmk5pUdf60"),
        plugins=dict(root="modules"),
    )
    app.run()

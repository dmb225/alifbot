import asyncio
from dotenv import load_dotenv
import os
from bot.bot import setup_bot  # doit retourner Application, pas une coroutine
from database.database import init_db

load_dotenv()

async def main():
    await init_db()

    bot = setup_bot(os.getenv("TELEGRAM_TOKEN"))  # <-- pas de await ici
    await bot.run_polling()  # <-- run_polling() est async, donc on await

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "already running" in str(e):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        else:
            raise

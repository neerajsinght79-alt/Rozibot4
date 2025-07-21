from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os

from shortlink import get_shortlink
from delivery import deliver_movie

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client("rozibot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & filters.command("start"))
async def start_handler(client, message):
    await message.reply("👋 Welcome! Send a movie name in any group I'm in, and click on the result!")

@bot.on_callback_query(filters.regex("getlink"))
async def link_callback_handler(client, callback_query: CallbackQuery):
    data = callback_query.data.split("|")
    movie_name = data[1]
    user_id = data[2]

    short_url = await get_shortlink(user_id, movie_name)
    await callback_query.message.reply(
        f"✅ Click to verify: {short_url}\n\nOnce done, click /done",
        quote=True
    )

@bot.on_message(filters.private & filters.command("done"))
async def done_handler(client, message):
    await deliver_movie(client, message)

if __name__ == "__main__":
    bot.run()

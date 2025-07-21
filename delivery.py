from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .shortlink import get_shortlink
from .fetch_from_premium import fetch_from_premium

# Store users who verified
verified_users = {}

@Client.on_message(filters.private & filters.command("start"))
async def start_handler(client: Client, message: Message):
    args = message.text.split(" ", 1)
    if len(args) == 2:
        movie_query = args[1].replace("_", " ")
        user_id = str(message.from_user.id)

        # Send ShrinkMe verification
        short_url = await get_shortlink(user_id, movie_query)
        await message.reply(
            f"🔐 To unlock *{movie_query}*, verify by clicking the link below and waiting 10 seconds:",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ Verify Now", url=short_url)]])
        )

        # Wait for user to click + verify (you can adjust this as needed)
        await asyncio.sleep(15)
        verified_users[user_id] = movie_query

        await message.reply("✅ Verified! Please wait while I fetch your movie...")

        result, buttons = await fetch_from_premium(movie_query)
        await message.reply(
            result,
            reply_markup=InlineKeyboardMarkup(buttons) if buttons else None,
            parse_mode="markdown"
        )
    else:
        await message.reply("👋 Welcome to Rozi Movie Bot! Send /start <movie_name> to begin.")

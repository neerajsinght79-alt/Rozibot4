from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fetch_from_premium import fetch_from_premium

# Group handler: responds to text queries in group
@Client.on_message(filters.text & filters.group)
async def group_query_handler(client, message):
    if message.text.startswith("/start") or message.text.startswith("/help"):
        return

    query = message.text
    response_text, buttons = await fetch_from_premium(query)

    if not buttons:
        await message.reply(response_text)
        return

    new_buttons = []
    for row in buttons:
        btn_row = []
        for btn in row:
            callback_data = f"getlink|{btn.text}|{message.from_user.id}"
            btn_row.append(InlineKeyboardButton(text=btn.text, callback_data=callback_data))
        new_buttons.append(btn_row)

    await message.reply(
        response_text,
        reply_markup=InlineKeyboardMarkup(new_buttons)
    )

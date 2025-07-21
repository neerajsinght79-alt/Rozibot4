from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.sessions import StringSession
import asyncio

API_ID = 23549525
API_HASH = "0958efc563b9a6710afd7176b736af88"
SESSION_STRING = "1BVtsOMYBu2oZ_VPS08P18nV4fU5n4TBf_vI_HrPj3E4nYuCHXEjT7NiZtR19rkM5LBnB9nE3NdslKjWzD8ZazuwC7tI5sUZqkn56bMld1NU-z1HrxW3PHg0TA7zRm5EZ0ljdNf3eVYuOlyzZXB0eTDgSYY7A61joBTV1-0anOw_lURHZSTpPSmeP6MSKV7EC2VdZrs2odhdTu3RjXf6QxDqt5v_KeFqaVuOCSMG9-d2K0Kkn7bBv3AU8KkEbe7PRNUw="
BOT_USERNAME = "@Premiummovies0_bot"

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def fetch_from_premium(query: str):
    await client.start()
    await client.send_message(BOT_USERNAME, query)
    await asyncio.sleep(4)

    history = await client(GetHistoryRequest(
        peer=BOT_USERNAME,
        limit=1,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    if not history.messages:
        return "❌ No result received from Premium bot.", []

    msg = history.messages[0].message
    buttons = history.messages[0].buttons

    result = f"📥 Movie Results for *{query}*\n\n{msg}\n\n👉 Tap the buttons below to get links."
    return result, buttons

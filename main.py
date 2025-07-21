import asyncio
from pyrogram import Client
from rozibot import delivery, group_handler

api_id = 23549525
api_hash = "0958efc563b9a6710afd7176b736af88"
bot_token = "8032468458:AAHa43tmVZgJvaprKNynTlG63x2-wGztGRQ"
session_string = "1BVtsOMYBu2oZ_VPS08P18nV4fU5n4TBf_vI_HrPj3E4nYuC 26H442WVL7BP1jPraV7_cE3jQnM-b117ixRoCbI3VNnLbp9F 71XxwxeEtolNArId1v8rDEAypicJOrQ01EC5H_IjxgBaf7i2 QSmRiYv7X3tcmQSTsGtnhsaTb53Z_fOiLhrB1aIG9w5ugUs8 Aw74EnCGXSYQW2Hx7mmqh-to7PkwrA9x31D7ziKD49D_10RW DQ_9fa1p4709WgcL8E21cmvZDdT-7zc0pNftbukYQn2QQitD QHFwPfynGEf9_54yddzrfdURJsmKO3bwW4r1bpJpt48mPjaj 7KC_jpfZNiaz_AOI="

app = Client("RoziBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Premium fetch client
premium_client = Client(
    "premium_session",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

async def main():
    await premium_client.start()
    await app.start()
    print("✅ RoziBot is running...")
    await idle()
    await premium_client.stop()
    await app.stop()

from pyrogram.idle import idle

if __name__ == "__main__":
    asyncio.run(main())

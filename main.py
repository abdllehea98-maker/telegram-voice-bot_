import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

api_id = int(os.environ.get("API_ID", "0"))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
call_py = PyTgCalls(app)

@app.on_message(filters.group & filters.new_chat_members)
async def join_group_call(client, message):
    chat_id = message.chat.id
    try:
        await call_py.join_group_call(
            chat_id,
            MediaStream("https://chiayi.radio.stream.public.retro-hits.stream/retro-hits.mp3")
        )
        await message.reply("تم الانضمام للمكالمة بنجاح!")
    except Exception as e:
        print(f"Error: {e}")

call_py.start()
app.run()

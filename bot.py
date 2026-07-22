import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, Message

API_ID = 611335
API_HASH = "d5240214ce14d36f6d53f5d37446e102"
BOT_TOKEN = "8878730932:AAEXLy71E_JiV-qZKwJzY7maydWXyKVWmpw"

app = Client(
    "Themajestic1bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)

BAD_WORDS = ["شتم", "سب", "كلمة_سيئة"]


@app.on_chat_member_updated()
async def welcome_member(client, update: ChatMemberUpdated):
  if update.new_chat_member and not update.old_chat_member:
    user = update.new_chat_member.user
    chat = update.chat
    mention = f"[{user.first_name}](tg://user?id={user.id})"
    await client.send_message(
        chat.id,
        f"أهلاً بك يا {mention} في مجموعة {chat.title}! 🌹\nيسعدنا انضمامك إلينا.",
    )


@app.on_message(filters.text & filters.group)
async def reply_greetings(client, message: Message):
  text = message.text.lower()
  if "السلام عليكم" in text or "سلام عليكم" in text:
    await message.reply("وعليكم السلام ورحمة الله وبركاته 🌸")
  elif "مرحبا" in text or "هلا" in text:
    await message.reply("أهلاً وسهلاً بك! نورت المجموعه ✨")


@app.on_message(filters.text & filters.group)
async def filter_bad_words(client, message: Message):
  text = message.text.lower()
  if any(word in text for word in BAD_WORDS):
    try:
      await message.delete()
      warning = await message.reply(
          f"عذراً [{message.from_user.first_name}](tg://user?id={message.from_user.id})، ممنوع استخدام الألفاظ المسيئة هنا! ⚠️"
      )
      await asyncio.sleep(5)
      await warning.delete()
    except Exception as e:
      print(f"خطأ: {e}")


print("البوت يعمل الآن بنجاح...")
app.run()


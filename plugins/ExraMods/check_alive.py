import time
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import *

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@Client.on_message(filters.command("earn", CMD))
async def help(_, message):
    await message.reply_text("𝟭. 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗛𝗔𝗦 𝟭𝟬𝟬+ 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 !!!\n\n𝟮. 𝗔𝗗𝗗 𝗕𝗢𝗧 𝗧𝗼 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗪𝗜𝗧𝗛 𝗙𝗨𝗟𝗟 𝗔𝗗𝗠𝗜𝗡 𝗥𝗜𝗚𝗛𝗧𝗦\n\n𝟯. 𝗔𝗙𝗧𝗘𝗥 𝗔𝗗𝗗𝗜𝗡𝗚 𝗜𝗡 𝗚𝗥𝗢𝗨𝗣, 𝗖𝗥𝗘𝗔𝗧𝗘 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗡 𝗔𝗡𝗬 𝗨𝗥𝗟 𝗦𝗛𝗢𝗥𝗧𝗡𝗘𝗥 𝗪𝗘𝗕𝗦𝗜𝗧𝗘\n\n𝗠𝗬 𝗦𝗨𝗚𝗚𝗘𝗦𝗧𝗜𝗢𝗡(𝗖𝗣𝗠 𝟳+) : <a href='https://tnshort.net/ref/Bharathraj'>𝗧𝗡𝗦𝗛𝗢𝗥𝗧.𝗡𝗘𝗧</a>\n\n𝟰. 𝗔𝗙𝗧𝗘𝗥 𝗠𝗔𝗞𝗜𝗡𝗚 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗡 𝗦𝗛𝗢𝗥𝗧𝗡𝗘𝗥 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 𝗦𝗘𝗡𝗗 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣\n\n—> /𝗦𝗛𝗢𝗥𝗧𝗟𝗜𝗡𝗞 𝗬𝗢𝗨𝗥_𝗦𝗛𝗢𝗥𝗧𝗘𝗡𝗘𝗥_𝗪𝗘𝗕𝗦𝗜𝗧𝗘_𝗡𝗔𝗠𝗘 (𝗬𝗢𝗨𝗥_𝗦𝗛𝗢𝗥𝗧𝗡𝗘𝗥_𝗔𝗣𝗜)\n\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘:-\n\n/𝗦𝗛𝗢𝗥𝗧𝗟𝗜𝗡𝗞 𝗧𝗡𝗦𝗛𝗢𝗥𝗧.𝗡𝗘𝗧 𝗕𝟲𝗔𝗔𝗖𝗘𝟰𝟲𝗗𝟰𝟬𝗖𝟲𝟬𝟱𝗙𝗙𝗙𝟴𝗘𝗢𝗖𝗔𝗙𝗕𝗖𝗗𝟴𝗙𝗕𝗘𝟰𝟭𝟲𝟴𝟱𝟭𝗙𝟰𝗗\n\n𝟱. 𝗔𝗗𝗗 𝗠𝗢𝗥𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗧𝗼 𝗘𝗔𝗥𝗡 𝗠𝗢𝗡𝗘𝗬")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n⚠️  MOVIES REQUEST TIPS »\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\n❤️Iғ Yᴏᴜ Wᴀɴᴛ A Mᴏᴠɪᴇ Jᴜsᴛ Tʏᴘᴇ Tʜᴇ Nᴀᴍᴇ ❤️\n彡Exᴀᴍᴘʟᴇs\n › Avatar ✔️\n Titanic ✔️\n› Avatar movie ❌\n› #Request Titanic ❌\n› Upload Avatar ❌\n\n❤️Iғ Tʜᴇʀᴇ Aʀᴇ Mᴀɴʏ Mᴏᴠɪᴇs Wɪᴛʜ Tʜᴇ Sᴀᴍᴇ Nᴀᴍᴇ Tʜᴇɴ Tʏᴘᴇ Yᴇᴀʀ ❤️\n彡 Exᴀᴍᴘʟᴇs \n› Avatar 2009 ✔️\n› Titanic 1997 ✔️\n\n❤️Iғ Mᴏᴠɪᴇ Nᴀᴍᴇ Is Lᴏɴɢ Mᴀᴋᴇ Iᴛ Sɪᴍᴘʟᴇ Iɴ Rᴇǫᴜᴇsᴛ ❤️\n彡 Exᴀᴍᴘʟᴇs \n› Last Night in Soho 2021 ❌\n› Soho 2021 ✔️\n› Godzilla vs Kong 2021 ❌\n› Kong 2021 ✔️\n\n❤️Iғ Yᴏᴜ Wᴀɴᴛ Sᴘᴇᴄɪғɪᴄ Lᴀɴɢᴜᴀɢᴇ Tʜᴇɴ Tʏᴘᴇ Lᴀɴɢᴜᴀɢᴇ Wɪᴛʜ Nᴀᴍᴇ❤️\n彡 Exᴀᴍᴘʟᴇs\n › Iron Man Tamil  ✔️\n› Iron Man English ✔️\n› Iron Man Tamil Dubbed  ❌\n› Iron Man In English ❌")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n⚠️ SERIES REQUEST TIPS »\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\n❤️ Iғ Yᴏᴜ Wᴀɴᴛ Aɴʏ Sᴇʀɪᴇs, Jᴜsᴛ Tʏᴘᴇ Tʜᴇ Nᴀᴍᴇ ❤️\n\n彡 Exᴀᴍᴘʟᴇs \n› Stranger Things ✔️\n› Request Stranger Things ❌\n› Stranger Things Series ❌\n\n❤️ Iғ Yᴏᴜ Wᴀɴᴛ A Sᴘᴇᴄɪғɪᴄ Sᴇᴀsᴏɴ Oғ Aɴʏ Sᴇʀɪᴇs , Tʏᴘᴇ Lɪᴋᴇ S01, S02 ᴇᴛᴄ... ❤️\n彡 Exᴀᴍᴘʟᴇs \n› Stranger Things S01 ✔️\n› Stranger Things Season 1 ❌\n\n❤️ Iғ Yᴏᴜ Wᴀɴᴛ A Sᴘᴇᴄɪғɪᴄ Episode Oғ Aɴʏ Sᴇʀɪᴇs , Tʏᴘᴇ Lɪᴋᴇ S01E01, S01E02 ᴇᴛᴄ... ❤️\n彡 Exᴀᴍᴘʟᴇs \n› Stranger Things S01E02 ✔️\n› Stranger Things Season 1  Episode 2 ❌")

#@Client.on_message(filters.command("tutorial", CMD))
#async def tutorial(_, message):
    #await message.reply_text("Tᴜᴛᴏʀɪᴀʟ Vɪᴅᴇᴏ 👉 https://t.me/tnlinkdown/6 \n\nFᴏʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ Tɪᴘs : <code>/ᴍᴏᴠɪᴇs</code>\n\nFᴏʀ Sᴇʀɪᴇs Rᴇǫᴜᴇsᴛ Tɪᴘs : <code>/sᴇʀɪᴇs</code>")

#@Client.on_message(filters.command("tutorial", CMD))
#async def tutorial(_, message):
    #await message.reply_video(
        #video=(TUTORIAL_VIDEO),
        #reply_markup=InlineKeyboardMarkup(
           # [
              #  [InlineKeyboardButton("Close", callback_data='close')]
           # ]
      #  ),

@Client.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    video=(TUTORIAL_VIDEO)

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Close ‼", callback_data='close_data')]
        ]
    )
    await message.reply_video(video=TUTORIAL_VIDEO, reply_markup=keyboard)        

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")

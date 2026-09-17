from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from KartikMusic import app

#--------------------------
MUST_JOIN = ["myanmarbot_music", "myanmar_music_bot2027"]
#------------------------

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return

    for channel in MUST_JOIN:
        try:
            try:
                await app.get_chat_member(channel, msg.from_user.id)
            except UserNotParticipant:
                if channel.isalpha():
                    link = "https://t.me/" + channel
                else:
                    chat_info = await app.get_chat(channel)
                    link = chat_info.invite_link
                try:
                    await msg.reply_video(
                        video="https://graph.org/file/286aa2427c36ca129f609-b2da780c99e73d27a7.mp4",
                        caption=f"๏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ғᴇᴀᴛᴜʀᴇs.\n\nᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ, ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴀɴᴅ ᴛʏᴘᴇ /start ᴀɢᴀɪɴ !!",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("• ᴊᴏɪɴ 1 •", url="https://t.me/+zhdoXlZydqpmZWVl"),
                                    InlineKeyboardButton("• ᴊᴏɪɴ 2 •", url="https://t.me/+VWgbmCbRp5IyNGQ1"),
                                ]
                            ]
                        )
                    )
                    await msg.stop_propagation()
                    return
                except ChatWriteForbidden:
                    pass
        except ChatAdminRequired:
            print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ ๏: {channel} !")

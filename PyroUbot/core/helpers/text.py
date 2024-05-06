from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import LOGS_MAKER_UBOT, OWNER_ID, bot, get_expired_date, ubot


class MSG:
    def DEAK(X):
        return f"""
<b>ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>ɪᴅ:</b> <code>{X.me.id}</code>
<b>ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴛᴇʟᴇɢʀᴀᴍ</b>
"""
            
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>ɪᴅ:</b> <code>{X.me.id}</code>
<b>ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b>
"""

    
    def START(message):
        return f"""
<b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 @{bot.me.username} ᴀᴅᴀʟᴀʜ ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ʙɪsᴀ ᴋᴀʟɪᴀɴ ʙᴜᴀᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ

👉🏻 sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ / ᴍᴇᴍʙᴇʟɪ ᴜsᴇʀʙᴏᴛ</b>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├──• ᴅᴀɴᴀ </b>
 <b>├─• <code>083107520691</code></b>
 <b>└──• <a href=https://link.dana.id/qr/6l85aa18>ᴋʟɪᴋ ᴅɪsɪɴɪ</a></b>

<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
"""

    async def USERBOT(count):
        return f"""
<b>ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
"""

    def POLICY():
        return """
↪️ ᴋᴇʙɪᴊᴀᴋᴀɴ ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ

✅ sᴇᴛᴇʟᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ, ᴊɪᴋᴀ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍᴘᴇʀᴏʟᴇʜ/
ᴍᴇɴᴇʀɪᴍᴀ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ ᴘᴇᴍʙᴇʟɪᴀɴ, 
ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʜᴀᴋ ᴘᴇɴɢɢᴀɴᴛɪᴀɴ ᴅᴀʟᴀᴍ ᴡᴀᴋᴛᴜ 2 ʜᴀʀɪ sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴇʟɪᴀɴ. ɴᴀᴍᴜɴ, ᴊɪᴋᴀ 
ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ/ᴍᴇɴᴇʀɪᴍᴀ sᴀʟᴀʜ sᴀᴛᴜ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ 
ᴘᴇᴍʙᴇʟɪᴀɴ, ᴛᴇʀᴍᴀsᴜᴋ ᴀᴋsᴇs ᴋᴇ ꜰɪᴛᴜʀ ᴘᴇᴍʙᴜᴀᴛᴀɴ ᴜsᴇʀʙᴏᴛ, ᴍᴀᴋᴀ 
ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʟᴀɢɪ ʙᴇʀʜᴀᴋ ᴀᴛᴀs ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ ᴅᴀɴᴀ.

🆘 ᴅᴜᴋᴜɴɢᴀɴ
ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴜᴋᴜɴɢᴀɴ, ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ:
• ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ
• sᴜᴘᴘᴏʀᴛ @mhmdwldnnnn ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ

👉🏻 ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏᴀᴛᴀᴋᴀɴ ʙᴀʜᴡᴀ ᴀɴᴅᴀ ᴛᴇʟᴀʜ 
ᴍᴇᴍʙᴀᴄᴀ ᴅᴀɴ ᴍᴇɴᴇʀɪᴍᴀ ᴋᴇᴛᴇɴᴛᴜᴀɴ ɪɴɪ ᴅᴀɴ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ 
ᴘᴇᴍʙᴇʟɪᴀɴ. ᴊɪᴋᴀ ᴛɪᴅᴀᴋ, ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴛᴀʟᴋᴀɴ.
"""


async def sending_user(user_id):
        await bot.send_message(
            user_id,
            "💬 sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥",
                            callback_data="bahan",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )

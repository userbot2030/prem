from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *

from PyroUbot import *


async def ohaja(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id not in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("⬅️ ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        exp = await get_expired_date(user_id)
        prefix = await get_pref(user_id)
        waktu = exp.strftime("%d-%m-%Y") if exp else "None"
        return await callback_query.edit_message_text(
            f"""
<b>ᴅᴀɴ ᴜꜱᴇʀʙᴏᴛ</b>
 <b>sᴛᴀᴛᴜs :</b> <code>ᴘʀᴇᴍɪᴜᴍ</code>
  <b>ᴘʀᴇғɪxᴇs :</b> <code>{prefix[0]}</code>
  <b>ᴇxᴘɪʀᴇᴅ_ᴏɴ :</b> <code>{waktu}</code>
  <b>ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ :</b> <code>-</code>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        
    else:
        buttons = [
            [InlineKeyboardButton("ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ", callback_data=f"bahan")],
            [InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<b>‼️ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍɪʟɪᴋɪ ᴜsᴇʀʙᴏᴛ ɪɴɪ</b>
<b>✅ sɪʟᴀʜᴋᴀɴ ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ ɴʏᴀ</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
    )

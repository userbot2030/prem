from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} ʙᴜʟᴀɴ",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏꜰɪʟ 👤", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "❌ ᴛᴏʟᴀᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ❌", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        button = [
            [InlineKeyboardButton("ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ", callback_data="bahan")],
            [
                InlineKeyboardButton(
                    "sᴛᴀᴛᴜs ᴀᴋᴜɴ", callback_data="pler"
                ),
                InlineKeyboardButton(
                    "ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ", callback_data="memek"
                ),
            ],
            #[InlineKeyboardButton("🤩 ᴜsᴇʀʙᴏᴛ ɢʀᴀᴛɪs 🤩", callback_data="grts")],
            [
                InlineKeyboardButton(
                    "ᴄʜᴀɴɴᴇʟꜱ sᴜᴘᴘᴏʀᴛ", url="https://t.me/Disney_storeDan"
                ),
                InlineKeyboardButton(
                    "ᴘᴇʀᴛᴀɴʏᴀᴀɴ", url="https://t.me/mhmdwldnnnn"
                ),
            ],
        ]
        return button

    def plus_minus(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ ✅", callback_data="confirm")],
            [InlineKeyboardButton("⬅️ ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return button

    
    def ambil_akun(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "📁 ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ 📁",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "📲 ᴄᴇᴋ ɴᴏᴍᴏʀ 📲",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "⏳ ᴄᴇᴋ ᴋᴀᴅᴀʟᴜᴀʀꜱᴀ ⏳",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔑 ᴄᴇᴋ ᴏᴛᴘ 🔑",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔐 ᴄᴇᴋ ᴠᴇʀɪꜰɪᴋᴀꜱɪ 2ʟ 🔐",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "☠ ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ ☠", callback_data=f"ub_deak {int(count)}",
                )
            ],
            [
                InlineKeyboardButton("⬅️", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"next_ub {int(count)}"),
            ],  
        ]
        return button

    def deak(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "⬅️ ᴋᴇᴍʙᴀʟɪ",
                    callback_data=f"prev_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "sᴇᴛᴜJᴜɪ ✅", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button

class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴏʀᴅᴇʀ @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"sɪʟᴀʜᴋᴀɴ ᴏʀᴅᴇʀ ᴅɪ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ɪɴʟɪɴᴇ ɪɴɪ"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"ᴍᴀᴋᴀɴʏᴀ ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper


async def gcast_create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = m.text.split("~>", 1)
    for X in split_text[1].split():
        button_data = X.split(":", 1)
        button_label = button_data[0].replace("_", " ")
        button_url = button_data[1]
        keyboard.append(InlineKeyboardButton(button_label, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0].split(None, 1)[1]
    return buttons, text_button


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("~>", 1)
    for X in split_text[1].split():
        split_X = X.split(":", 1)
        button_text = split_X[0].replace("_", " ")
        button_url = split_X[1]
        keyboard.append(InlineKeyboardButton(button_text, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0]
    return buttons, text_button

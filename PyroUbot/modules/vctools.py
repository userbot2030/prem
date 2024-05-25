from asyncio import sleep
from random import randint
from typing import Optional

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "vctools"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟs 』</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>startvc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> uɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ 

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>stopvc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>joinvc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>leavevc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ
"""


@PY.UBOT("startvc")
async def _(client, message):
    await opengc(client, message)


@PY.UBOT("stopvc")
async def _(client, message):
    await end_vc_(client, message)

@PY.UBOT("joinvc")
async def _(client, message):
    await joinvc(client, message)

@PY.UBOT("leavevc")
async def _(client, message):
    await leavevc(client, message)



async def get_group_call(client: Client, message: Message, err_msg: str = "") -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await client.send(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"**No group call Found** {err_msg}")
    return False

@PY.UBOT("joinvc")
@ubot.on_message(filters.user(DEVS) & filters.command("cjoinvc", ".") & ~filters.me)
async def joinvc(client, message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113891550788324241"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6111585093220830556"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        await client.group_call.start(chat_id, join_as=client.me.id)
    except Exception as e:
        return await msg.edit(f"<emoji id={gagal}>❌</emoji>ERROR: {e}")
    await msg.edit(f"<b><emoji id={sukses}>✅</emoji>ʙᴇʀʜᴀsɪʟ ɴᴀɪᴋ ᴋᴇ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>")
    await sleep(1)
    await client.group_call.set_is_mute(True)

@PY.UBOT("leavevc")
@ubot.on_message(filters.user(DEVS) & filters.command("cleavevc", ".") & ~filters.me)
async def leavevc(client: Client, message: Message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113891550788324241"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6111585093220830556"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    try:
        await client.group_call.stop()
    except Exception as e:
        return await msg.edit(f"<emoji id={gagal}>❌</emoji>ERROR: {e}")
    return await msg.edit(f"<b><emoji id={sukses}>✅</emoji>ʙᴇʀʜᴀsɪʟ ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>")


async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6246660083808210143"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    ky = await message.reply(message, "`Processing....`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<b><emoji id={sukses}>✅</emoji> ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ</b>\n <emoji id={alasan}>⚠️</emoji> <b>ɢʀᴏᴜᴘ ᴄʜᴀᴛ</b> : {message.chat.title}"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


async def end_vc_(client: Client, message: Message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6247033234861853924"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    ky = await message.reply(message, "`Processing....`")
    message.chat.id
    if not (group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await ky.edit(f"<emoji id={gagal}>❎</emoji> <b>ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴍᴀᴛɪᴋᴀɴ</b>\n <emoji id={alasan}>⚠️</emoji><b>Chat</b> : {message.chat.title}")

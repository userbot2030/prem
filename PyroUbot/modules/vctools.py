from PyroUbot import *


__MODULE__ = "vctools"
__HELP__ =f"""
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

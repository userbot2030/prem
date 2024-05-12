from PyroUbot import *


__MODULE__ = "vctools"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}startvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}stopvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴅɪᴀᴋʜɪʀɪ.
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}joinvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʙᴇʀʜᴀꜱɪʟ ᴊᴏɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leavevc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.
"""


@PY.UBOT("startvc")
async def _(client, message):
    await start_vctools(client, message)


@PY.UBOT("stopvc")
async def _(client, message):
    await stopvc_vctools(client, message)


@PY.UBOT("joinvc")
async def _(client, message):
    await joinvc_vctools(client, message)


@PY.UBOT("leavevc")
async def _(client, message):
    await leavevc_vctools(clien, message)

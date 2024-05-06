from PyroUbot import *

__MODULE__ = "control"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴛʀᴏʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setprefix</code> [sɪᴍʙᴏʟ ᴘʀᴇғɪx]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴘʀᴇғɪx/ʜᴀɴᴅʟᴇʀ ᴄᴏᴍᴍᴀɴᴅ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setemoji</code> [ǫᴜᴇʀʏ] [ᴠᴀʟᴇᴜ]
  <b>• ǫᴜᴇʀʏ: </b>
       <b>•> PONG </b>
       <b>•> MENTION </b>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴘᴀᴅᴀ ᴘɪɴɢ</b>

"""



@PY.UBOT("setprefix")
async def _(client, message):
    await setprefix(client, message)

@PY.UBOT("setemoji")
async def _(client, message):
    await change_emot(client, message)


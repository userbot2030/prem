from .. import *


@PY.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)


@PY.BOT("stats")
async def _(client, message):
    await stats_ubot(client, message)


@PY.CALLBACK("kontol")
async def _(client, callback_query):
    await cb_stats(client, callback_query)

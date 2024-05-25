from PyroUbot import *

class EMO:
    async def PING1(client):
        emot_1 = await get_vars(client.me.id, "EMOJI_PING1")
        ping1 = emot_1 if emot_1 else "5219943216781995020"
        if client.me.is_premium:
            _pong1 = f"<emoji id={ping1}>🏓</emoji>"
        else:
            _pong1 = ""
        return _pong1


    async def PING2(client):
        emot_2 = await get_vars(client.me.id, "EMOJI_PING2")
        ping2 = emot_2 if emot_2 else "5301096984617166561"
        if client.me.is_premium:
            _pong2 = f"<emoji id={ping2}>🤖</emoji>"
        else:
            _pong2 = ""
        return _pong2


    async def PING3(client):
        emot_3 = await get_vars(client.me.id, "EMOJI_PING3")
        ping3 = emot_3 if emot_3 else "5289940334619406906"
        if client.me.is_premium:
            _pong3 = f"<emoji id={ping3}>👑</emoji>"
        else:
            _pong3 = ""
        return _pong3
        
    async def SUKSES(client):
        emot_4 = await get_vars(client.me.id, "EMOJI_SUKSES")
        sukses = emot_4 if emot_4 else "5206607081334906820"
        if client.me.is_premium:
            _berhasil = f"<emoji id={sukses}>✅</emoji>"
        else:
            _berhasil = ""
        return _berhasil

    async def GAGAL(client):
        emot_5 = await get_vars(client.me.id, "EMOJI_GAGAL")
        gagal = emot_5 if emot_5 else "5210952531676504517"
        if client.me.is_premium:
            _ggl = f"<emoji id={gagal}>❌</emoji>"
        else:
            _ggl = ""
        return _ggl

    async def PROSES(client):
        emot_6 = await get_vars(client.me.id, "EMOJI_PROSES")
        proses = emot_6 if emot_6 else "5814367691275767776"
        if client.me.is_premium:
            _proses = f"<emoji id={proses}>⏳</emoji>"
        else:
            _proses = ""
        return _proses

    async def WARNING(client):
        emot_7 = await get_vars(client.me.id, "EMOJI_WARNING")
        warning = emot_7 if emot_7 else "6172475875368373616"
        if client.me.is_premium:
            _warn = f"<emoji id={warning}>⚠️</emoji>"
        else:
            _warn = ""
        return _warn

    async def ALASAN(client):
        emot_8 = await get_vars(client.me.id, "EMOJI_ALASAN")
        alasan = emot_8 if emot_8 else "6208270338971669367"
        if client.me.is_premium:
            _alsn = f"<emoji id={alasan}>💬</emoji>"
        else:
            _alsn = ""
        return _alsn

    async def USER(client):
        emot_9 = await get_vars(client.me.id, "EMOJI_USER")
        user = emot_9 if emot_9 else "5316767533573884148"
        if client.me.is_premium:
            _usr = f"<emoji id={user}>👤</emoji>"
        else:
            _usr = ""
        return _usr

    async def ADMIN(client):
        emot_10 = await get_vars(client.me.id, "EMOJI_USER")
        admin = emot_10 if emot_10 else "6264622255515371358"
        if client.me.is_premium:
            _adm = f"<emoji id={admin}>👮🏻</emoji>"
        else:
            _adm = ""
        return _adm

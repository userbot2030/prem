import os

DEVS = [
    5779185981,
]

API_ID = int(os.getenv("API_ID", "26477680"))

API_HASH = os.getenv("API_HASH", "b0d8504752cc1ecf52009ece2bdef0b8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7000576366:AAFldbmglUra7jmWiisvrbQzdBjK-3oG9JY")

OWNER_ID = int(os.getenv("OWNER_ID", "5779185981"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002032983910"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002127258037").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "sk-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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://dantesbot:wildan18@cluster0.fol5tml.mongodb.net/?retryWrites=true&w=majority",
)



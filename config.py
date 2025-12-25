# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature (FIXED BOOL HANDLING)
LOGIN_SYSTEM = os.environ.get("LOGIN_SYSTEM", "True").lower() == "true"

if LOGIN_SYSTEM is False:
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23631217"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get(
    "API_HASH",
    "567c6df308dc6901790309499f729d12"
)

# Your Owner / Admin Id For Broadcast
ADMINS = int(os.environ.get("ADMINS", "7501925066"))

# Upload channel (leave empty "" if not needed)
CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1002434689255")

# MongoDB
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mohammadmuzaffarimambaturbari:sHXNxpKZ9PDjyYQr@cluster0.dqjjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "mohammadmuzaffarimambaturbari")

# ⏩ SPEED CONTROL (MAIN CHANGE)
# 10 sec ❌ | 2 sec ✅ | 1 sec ⚠️ risky
WAITING_TIME = int(os.environ.get("WAITING_TIME", "2"))

# Error message toggle (FIXED BOOL)
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"

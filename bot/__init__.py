import os
import logging
import time

from logging.handlers import RotatingFileHandler

from Script import script

# Change Accordingly While Deploying To A VPS
API_ID = int(os.environ.get("API_ID"))

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DATABASE_URI = os.environ.get("DATABASE_URI")

USER_SESSION = os.environ.get("USER_SESSION")

DATABASE_NAME=os.environ.get("DATABASE_NAME")

COLLECTION_NAME=os.environ.get("COLLECTION_NAME")

LOG_CHANNEL=os.environ.get("LOG_CHANNEL")

CUSTOM_FILE_CAPTION=os.environ.get("CUSTOM_FILE_CAPTION")

ADMINS=os.environ.get("ADMINS")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

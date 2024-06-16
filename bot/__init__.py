from os import environ
import logging
import time

from logging.handlers import RotatingFileHandler

from Script import script

# Change Accordingly While Deploying To A VPS
API_ID = int(environ['API_ID'])

API_HASH = environ['API_HASH']

BOT_TOKEN = environ['BOT_TOKEN']

DATABASE_URI = environ.get("DATABASE_URI")

USER_SESSION = environ.get("USER_SESSION")

DATABASE_NAME= environ.get("DATABASE_NAME")

COLLECTION_NAME= environ.get("COLLECTION_NAME")

LOG_CHANNEL= environ.get("LOG_CHANNEL")

CUSTOM_FILE_CAPTION= environ.get("CUSTOM_FILE_CAPTION")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

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

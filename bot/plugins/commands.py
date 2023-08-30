from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from Script import script
import asyncio
from bot import __init__ #import for Log channel
from bot.database import Media #class
db = Database()

FORCE_SUB = "wudixh13"

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
#FORCE SUB FN()    
    if FORCE_SUB:
        try:
            user = await bot.get_chat_member(FORCE_SUB, update.from_user.id)
            if user.status == "kicked out":
                await update.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await update.reply_text(
                text="🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭.\n\nDᴏ Yᴏᴜ Wᴀɴᴛ Mᴏᴠɪᴇs? Tʜᴇɴ Jᴏɪɴ Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ Aɴᴅ Wᴀᴛᴄʜ ɪᴛ.😂\n Tʜᴇɴ ɢᴏ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴍᴏᴠɪᴇ ᴀɢᴀɪɴ ᴀɴᴅ ɢɪᴠᴇ ɪᴛ ᴀ sᴛᴀʀᴛ...!😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭", url=f"t.me/{FORCE_SUB}")
                 ]]
                 )
            )
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type, file_size = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
  #FILE SIZE COMPRESSING>>>>>      
        if file_size < 1024:
            file_size = f"[{file_size} B]"
        elif file_size < (1024**2):
            file_size = f"[{str(round(file_size/1024, 2))} KB]"
        elif file_size < (1024**3):
            file_size = f"[{str(round(file_size/(1024**2), 2))} MB]"
        elif file_size < (1024**4):
            file_size = f"[{str(round(file_size/(1024**3), 2))} GB]"
#CUSTOM FILE CAPTION       
        caption = f""" 📂 <em>File Name</em>: <code>Kᴜᴛᴛᴜ Bot | {file_name} </code> \n\n🖇 <em>File Size</em>: <code> {file_size} </code>"""
        
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton('💕Movie Group❤️', url="https://t.me/wudixh")
                        ], [
                            InlineKeyboardButton('Dᴇᴠᴇʟᴏᴘᴇʀ ✔', url="https://t.me/wudixh13/4")
                        ]]
                ))
            
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(name).error(e)
        return

#pmstart
    buttonscom = [[
                    InlineKeyboardButton('Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ💕', url=f"http://t.me/im_kuttu2_bot?startgroup=true")
                ],[
                    InlineKeyboardButton('Mᴏᴠɪᴇ ɢʀᴏᴜᴘ🎥', url='https://t.me/wudixh')
                ],[
                    InlineKeyboardButton('Hᴇʟᴘ🔧', callback_data="help"),
                    InlineKeyboardButton('Aʙᴏᴜᴛ🖥', callback_data="about")
           ]]
    
    if not await db.is_user_exist(update.from_user.id): #db add use and exist checking
        await db.add_user(update.from_user.id, message.from_first.name)
        await message.send_message(LOG_CHANNEL, script.LOGTXT_P.format(update.from_user_id, update.from_user.mention))
#SEND MSG TO LOGCHANNEL
    reply_markup = InlineKeyboardMarkup(buttonscom)
    s=await update.reply_sticker("CAACAgUAAxkBAAEKKFpk7Z_2zmfPq4vX_GROmZqanhB4JAACqAADyJRkFJWi9VCRb0zWMAQ") #sticker id
    await asyncio.sleep(2) #sleep for 2s 
    await s.delete() #sticker delete after 2s
    
    await update.reply_text(
        text=script.START_TEXT.format(update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )
    return
    
@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
            InlineKeyboardButton('Stats💹', callback_data='stats')

        ],[
            InlineKeyboardButton('🏡Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('🔐Cʟᴏsᴇ', callback_data='close')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_text(
        text=script.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
            InlineKeyboardButton('Oᴡɴᴇʀ👤', url='https://t.me/wudixh13/4')
        ], [
            InlineKeyboardButton('🏡Hᴏᴍᴇ', callback_data='start')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_text(
        text=script.ABOUT_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )
@Client.on_message(filters.command(["stats"]) & filters.private, group=1)
async def help(bot, update):
    okda = await update.reply('Fetching stats..')
    total = await Media.count_documents
    users = await db.total_users_count()
    monsize = await db.get_db_size()
    free = 536870912 - monsize
    monsize = get_size(monsize)
    free = get_size(free)
    await okda.edit_text(
        text=script.STATUS_TXT.format(total, users, monsize, free),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

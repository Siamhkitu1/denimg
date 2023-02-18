import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/905149e85560cf7794797.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
Alo kka ada yg bsa saya banting
jika kalian kepo kek dora gabung dibawah ...
┏━━━━━━━━━━━━━━━━━
┣➸ ini tele aku kak : [deniMG](https://t.me/deniMG)
┣➸ ini ch aku muehehe : [TiredEXE](https://t.me/TiredEXE)
┣➸ kalo ini grup : [Excellent](https://t.me/+QEC_TALjMABiZjhl)
┣➸ kalo ini apa hayo › : [Kepo ya](https://www-xnxx-com.translate.goog/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id&_x_tr_pto=wapp)
┗━━━━━━━━━━━━━━━━━

chat aku dong kka
Pc pc aja [ini deniMG](https://t.me/deniMG) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ kmu tuh cantik mau g di eue sama aku ❱ ➕", url=f"https://t.me/TiredEXE")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/mulai", "/alive", "deniMG"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/905149e85560cf7794797.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Kepo kek dora", url=f"https://www-xnxx-com.translate.goog/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id&_x_tr_pto=wapp")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/905149e85560cf7794797.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Kepo kek kntl", url=f"https://t.me/TiredEXE")
                ]
            ]
        ),
    )

# (©)Codexbotz
# Recode by @mrismanaziz

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • Owner: @{OWNER}\n • Group I: @{CHANNEL}\n • Group II: @{GROUP}\n • PP MURAH: <a href='https://t.me/tontonvid'>Paid Promote</a>\n • VVIP MURAH: <a href='https://t.me/vvipmurahmeriah'>Join VVIP Murah</a>\n • Source Code: <a href='https://t.me/tontonvid'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass

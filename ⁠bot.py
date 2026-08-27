import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text('سڵاو! بۆتەکەت کاردەکات.')

app = ApplicationBuilder().token('8992391913:AAF_E4XIGGlVP0nqZfT15BVv78jZ6kF7Aa4').build()
app.add_handler(CommandHandler('start', start))
app.run_polling()

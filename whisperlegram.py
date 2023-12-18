import os
from dotenv import load_dotenv
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CallbackContext, ContextTypes, CommandHandler, filters

load_dotenv(dotenv_path="vars.env")

TOKEN = os.getenv("tg_key")

print(TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def get_voice(update: Update, context: CallbackContext) -> None:
    new_file = await context.bot.get_file(update.message.voice.file_id)
    print(update.message.voice.file_id)
    await new_file.download_to_drive("voice_note.ogg")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Voice message saved, transcribing...")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    
    echo_handler = MessageHandler(filters.VOICE, get_voice)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7567550205:AAGzh9JZkEFSjNWhbsZAWWqLMUL8KswI4Ck"
CHANNEL_LINK = "https://t.me/eaexperts"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with channel button"""
    keyboard = [[InlineKeyboardButton("Join Our Forex Channel", url=CHANNEL_LINK)]]
    
    await update.message.reply_text(
        "Welcome to Forex Experts!\n\n"
        "Click below to join our premium channel:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    await update.message.reply_text(
        "Simply click the button in /start to join our Forex channel!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle any messages"""
    await update.message.reply_text(
        "Please use /start to join our Forex channel."
    )

def main():
    """Run the bot"""
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.run_polling()

if __name__ == '__main__':
    main()

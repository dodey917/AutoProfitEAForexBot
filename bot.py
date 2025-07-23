import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token
TOKEN = "7567550205:AAGzh9JZkEFSjNWhbsZAWWqLMUL8KswI4Ck"

# Your channel and group links
CHANNEL_LINK = "https://t.me/eaexperts"
GROUP_LINK = "https://t.me/Z5293362763"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"Hello {user.first_name}! 👋\n\n"
        "Welcome to Forex Experts!\n\n"
        f"Join our channel: {CHANNEL_LINK}\n"
        f"Join our group: {GROUP_LINK}\n\n"
        "Well done, you are on the way to becoming a trading expert!"
    )
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "This bot helps you connect with our Forex community.\n\n"
        "Available commands:\n"
        "/start - Get welcome message and links\n"
        "/help - Show this help message\n\n"
        f"Channel: {CHANNEL_LINK}\n"
        f"Group: {GROUP_LINK}"
    )
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle any other messages."""
    await update.message.reply_text(
        "Thanks for your message! Use /start to get our links or /help for assistance."
    )

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command messages - reply with default message
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

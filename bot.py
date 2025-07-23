import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token
TOKEN = "7567550205:AAGzh9JZkEFSjNWhbsZAWWqLMUL8KswI4Ck"

# Your channel info
CHANNEL_LINK = "https://t.me/eaexperts"
CHANNEL_USERNAME = "eaexperts"  # Without the '@'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with channel button when the command /start is issued."""
    user = update.effective_user
    
    # Create inline keyboard with single button
    keyboard = [
        [
            InlineKeyboardButton("Join Our Channel", url=CHANNEL_LINK),
            InlineKeyboardButton("I've Joined ✅", callback_data="joined")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = (
        f"Hello {user.first_name}! 👋\n\n"
        "Welcome to Forex Experts!\n\n"
        "Click the button below to join our exclusive channel for expert signals:\n\n"
        "After joining, click 'I've Joined' below!"
    )
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == "joined":
        await query.edit_message_text(
            text="🎉 Well done! You are on your way to becoming a trading expert!\n\n"
                 "You now have access to our premium Forex signals and analysis.",
            reply_markup=None
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    help_text = (
        "🤖 Forex Experts Bot Help\n\n"
        "This bot provides access to our premium Forex channel.\n\n"
        "Available commands:\n"
        "/start - Get welcome message with channel link\n"
        "/help - Show this help message\n\n"
        "Click below to join our channel:"
    )
    await update.message.reply_text(
        help_text,
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle any other messages."""
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "To get started, please join our channel using the button below:",
        reply_markup=reply_markup
    )

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Add callback handler for buttons
    application.add_handler(CallbackQueryHandler(button_callback))

    # Handle all other messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler
)

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Constants
BOT_TOKEN = "7567550205:AAGzh9JZkEFSjNWhbsZAWWqLMUL8KswI4Ck"
CHANNEL_LINK = "https://t.me/eaexperts"
CHANNEL_NAME = "Forex Experts Pro"

class ForexExpertsBot:
    def __init__(self):
        self.app = Application.builder().token(BOT_TOKEN).build()
        self._register_handlers()

    def _register_handlers(self):
        """Register all command and message handlers"""
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CallbackQueryHandler(self.button_handler))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /start command with professional welcome message"""
        user = update.effective_user
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                text=f"✨ Join {CHANNEL_NAME}",
                url=CHANNEL_LINK
            )],
            [InlineKeyboardButton(
                text="✅ Joined Successfully",
                callback_data="joined"
            )]
        ])

        welcome_message = (
            f"🌟 *Welcome {user.first_name} to {CHANNEL_NAME}!*\n\n"
            "Discover *exclusive* Forex signals, market analysis, and trading strategies "
            "from our team of professional traders.\n\n"
            "To get started:\n"
            "1. Tap 'Join Channel' below\n"
            "2. Confirm with 'Joined Successfully'\n\n"
            "*Limited spots available!*"
        )

        await update.message.reply_text(
            welcome_message,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle button callbacks"""
        query = update.callback_query
        await query.answer()

        if query.data == "joined":
            success_message = (
                "🎉 *Welcome Aboard!*\n\n"
                "You've successfully joined our premium Forex community.\n\n"
                "🔹 Daily market analysis\n"
                "🔹 Real-time trade signals\n"
                "🔹 Expert trading insights\n\n"
                "We're excited to help you achieve your trading goals!"
            )
            await query.edit_message_text(
                text=success_message,
                parse_mode="Markdown"
            )

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /help command"""
        help_message = (
            "💼 *Forex Experts Pro - Assistance*\n\n"
            "Here's how to use this bot:\n\n"
            "*/start* - Begin and join our premium channel\n"
            "*/help* - Show this help message\n\n"
            "For any issues, please contact our support team."
        )
        await update.message.reply_text(
            help_message,
            parse_mode="Markdown"
        )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle any other text messages"""
        await update.message.reply_text(
            "To access our premium Forex content, please use /start to begin.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(
                    text="🚀 Get Started",
                    callback_data="start"
                )]
            ])
        )

    def run(self):
        """Run the bot indefinitely"""
        self.app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    bot = ForexExpertsBot()
    logger.info("Forex Experts Pro Bot is now running...")
    bot.run()

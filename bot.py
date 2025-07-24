import os
import sys
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configuration - Exit if token not found
BOT_TOKEN = os.getenv('8448863022:AAG1u9aCnHoKlDam4Go_N_IBbcFv4KHLG8c')
if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN environment variable not set!")
    sys.exit(1)

CHANNEL_LINK = "https://t.me/eaexperts"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_message = (
        f"👋 Hello {user.username or 'trader'}!\n\n"
        "🌟 Welcome to Forex Experts – your gateway to automated trading solutions!\n\n"
        "📈 Access our Copy Trade service featuring advanced EAs and trading robots "
        "designed for efficient market participation.\n\n"
        "👉 Join our channel for real-time updates:"
    )

    keyboard = [
        [InlineKeyboardButton("✨ Join Official Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ I've Joined", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

async def handle_joined(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    success_message = (
        "🚀 Well done! You're all set.\n\n"
        "Next steps:\n"
        "1. Check our channel for daily insights\n"
        "2. Review pinned messages for resources\n"
        "3. Contact @ForexSupport for assistance\n\n"
        "*Note: Trading involves risk. Past performance ≠ future results.*"
    )
    
    await query.edit_message_text(
        success_message,
        reply_markup=None,
        parse_mode="Markdown"
    )

def main():
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        print("Bot initialized successfully!")
        
        # Add Handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_joined, pattern="joined"))
        
        # Start Bot
        print("Bot is running...")
        application.run_polling()
        
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

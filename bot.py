import os
import sys
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enhanced token retrieval with detailed error reporting
def get_bot_token():
    token = os.getenv('8448863022:AAG1u9aCnHoKlDam4Go_N_IBbcFv4KHLG8c')
    
    if not token:
        print("❌ CRITICAL ERROR: BOT_TOKEN environment variable is not set!")
        print("Please set the BOT_TOKEN environment variable in Render.com")
        print("Go to your service -> Environment -> Add environment variable")
        print("Key: BOT_TOKEN")
        print("Value: [YOUR_BOT_TOKEN_FROM_BOTFATHER]")
        sys.exit(1)
    
    # Basic token format validation
    if ':' not in token:
        print("❌ INVALID TOKEN FORMAT: Token should be in format '1234567890:ABCdefGHIjklMNoPQRsTUVwxyZ'")
        print(f"Your token: '{token}'")
        sys.exit(1)
        
    return token

BOT_TOKEN = get_bot_token()
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
        print("⏳ Initializing bot...")
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add Handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_joined, pattern="joined"))
        
        print("🤖 Bot initialized successfully!")
        print("🚀 Starting bot polling...")
        application.run_polling()
        
    except Exception as e:
        print(f"🔥 CRITICAL ERROR: {str(e)}")
        print("Possible solutions:")
        print("1. Check BOT_TOKEN format (should be 'numbers:letters')")
        print("2. Verify internet connection")
        print("3. Ensure bot has proper permissions")
        sys.exit(1)

if __name__ == "__main__":
    print("🔍 Checking environment...")
    main()

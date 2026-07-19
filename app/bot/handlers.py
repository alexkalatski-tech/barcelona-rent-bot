from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Barcelona Rent Bot\n\nI'm alive! 🚀"
    )

def register_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))

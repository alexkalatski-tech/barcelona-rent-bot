from telegram.ext import Application
from handlers import register_handlers

class RentBot:
    def __init__(self, token: str):
        self.app = Application.builder().token(token).build()
        register_handlers(self.app)

    def run(self):
        self.app.run_polling()

from config.settings import settings
from utils.logger import logger
from bot.bot import RentBot

def main():
    logger.info("Starting Barcelona Rent Bot...")
    if not settings.TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN is not configured.")
        return
    RentBot(settings.TELEGRAM_BOT_TOKEN).run()

if __name__ == "__main__":
    main()

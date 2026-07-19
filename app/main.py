from config.settings import settings
from utils.logger import logger

def main():
    logger.info("Barcelona Rent Bot is starting...")
    logger.info(f"Check interval: {settings.CHECK_INTERVAL} seconds")
    logger.info("Project initialized successfully.")

if __name__ == "__main__":
    main()

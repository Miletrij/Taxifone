import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,  # filters вместо Filters!
    ContextTypes,  # CallbackContext заменён на ContextTypes
)

# Настройка логов
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "Your telegram token"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я бот для такси. Отправьте мне адрес.")

# Обработчик текстовых сообщений
async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    address = update.message.text
    await update.message.reply_text(f"Адрес принят: {address}. Такси скоро приедет!")

def main() -> None:
    # Создаём Application (раньше был Updater)
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address))  # filters.TEXT вместо Filters.text

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()

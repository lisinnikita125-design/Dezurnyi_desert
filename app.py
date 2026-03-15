import os
import logging
from flask import Flask, request
from bot import create_application
from telegram import Update

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Создаём экземпляр бота
application = create_application()

BASE_URL = os.environ.get("RENDER_EXTERNAL_URL")  # автоматически задаётся Render'ом

@app.route('/')
def index():
    return "Bot is running!", 200

@app.route('/health')
def health():
    return "OK", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    """Принимает обновления от Telegram и передаёт их боту."""
    if request.method == 'POST':
        update_data = request.get_json()
        if update_data:
            update = Update.de_json(update_data, application.bot)
            application.update_queue.put_nowait(update)
            return "OK", 200
        else:
            return "Bad Request", 400
    return "Method Not Allowed", 405

@app.before_request
def setup_webhook():
    """Устанавливает вебхук при первом запросе (один раз)."""
    if not hasattr(app, 'webhook_set'):
        logger.info("Устанавливаем вебхук на %s/webhook", BASE_URL)
        application.bot.set_webhook(url=f"{BASE_URL}/webhook")
        app.webhook_set = True
        logger.info("Вебхук установлен")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Запуск Flask на порту {port}")
    app.run(host='0.0.0.0', port=port)
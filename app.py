import os
import threading
import logging
from flask import Flask
from bot import main as bot_main

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!", 200

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"🚀 Запуск Flask на порту {port}")
    app.run(host='0.0.0.0', port=port)

# Запускаем Flask в фоновом потоке
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# Теперь запускаем бота в главном потоке
if __name__ == '__main__':
    try:
        logger.info("🔥 Запуск бота в главном потоке...")
        bot_main()
    except Exception as e:
        logger.exception("❌ Ошибка в боте: %s", e)

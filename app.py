import os
import threading
import logging
from flask import Flask
from bot import main as bot_main

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!", 200

@app.route('/health')
def health():
    return "OK", 200

def run_bot():
    try:
        logger.info("Запуск бота в фоновом потоке...")
        bot_main()
    except Exception as e:
        logger.exception("Ошибка в боте: %s", e)

thread = threading.Thread(target=run_bot)
thread.daemon = True
thread.start()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

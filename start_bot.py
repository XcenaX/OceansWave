from main.modules.NewsBot import Bot
from oceanswave.settings import TELEGRAM_BOT_TOKEN

bot = Bot(TELEGRAM_BOT_TOKEN)
bot.polling(none_stop=True, interval=0)
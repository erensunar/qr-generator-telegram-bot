import sys
import telebot
from qr_generator import generate_qr
sys.path.insert(0, "..") 
import config

TOKEN = config.BOT_TOKEN


bot = telebot.TeleBot(TOKEN)


start_message = config.BOT_START_MESSAGE


# Bot başladığında çalışacak fonksiyon
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, start_message)

@bot.message_handler(func=lambda message: True)
def create_qr_from_text(message):
    # Eğer mesaj metin değilse, "Please send a text message." mesajı gönder
    if message.content_type != 'text':
        bot.reply_to(message, "Please send a text message.")
        return

    # QR kodu oluştur
    qr_img =generate_qr(message.text)

    # QR kodunu gönder
    bot.send_photo(message.chat.id, photo=qr_img)

# Botu başlat
bot.polling()

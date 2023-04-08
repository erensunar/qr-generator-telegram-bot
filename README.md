# Telegram QR Code Bot

This is a Telegram bot that converts user text messages to QR codes and sends them back to the user.
Bu, kullanıcı metin mesajlarını QR kodlarına dönüştüren ve kullanıcıya geri gönderen bir Telegram botudur.

## Requirements

- qrcode==7.4.2
- pyTelegramBotAPI==4.10.0
- pillow==9.5.0

## Usage

1. Clone the repository:
```bash
    git clone https://github.com/erensunar/qr-generator-telegram-bot.git
```
2. Install the required packages:
```bash
    pip install -r requirements.txt
```
3. Create a new Telegram bot and get the bot token. You can find instructions [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).

4. Add your bot token to the config file.

5. Run the bot:
```bash
    python telegram_bot.py
```
6. Send a text message to the bot and receive a QR code in response!

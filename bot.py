import telebot
import subprocess
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle(message):
    url = message.text.strip()
    bot.reply_to(message, "⏳ جارِ تحميل الفيديو...")

    try:
        subprocess.run(
            ["yt-dlp", "-f", "mp4", "-o", "video.mp4", url],
            check=True
        )
        with open("video.mp4", "rb") as video:
            bot.send_video(message.chat.id, video)
        os.remove("video.mp4")
    except:
        bot.reply_to(message, "❌ رابط غير صالح")

bot.infinity_polling()

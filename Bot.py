import telebot
import pyqrcode
import time

token="Paste your Bot token here"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'வணக்கம், \n I am here to create your own QR code... \n\n<b> Send /qr & then send me a text or Link to Generate your QR code... 🔥 \n\n <b> ⚡️ GOD : KiruthiVarma</b>')
    
@bot.message_handler(commands=['qr'])
def qr_code_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_message(message.chat.id, "⬆️ Send Text or Url")
    bot.register_next_step_handler(sent, qrcode)

def qrcode(message):
    url=pyqrcode.create(message.text)
    url.png('QR Code.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open('QR Code.png','rb' ))

while True:
	try:
		bot.polling(True)
	except Exception:
		time.sleep(1)

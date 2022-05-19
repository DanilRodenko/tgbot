import requests as rq
from datetime import datetime as dt
import telebot
from telebot import types
from auth_data import token



def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, f"Hello {message.chat.first_name}.")
        choose_coin(message)

    def choose_coin(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_btc = types.KeyboardButton('BTCUSD')
        key_eth = types.KeyboardButton('ETHUSD')
        key_doge = types.KeyboardButton('DOGEUSD')
        keyboard.add(key_btc,key_eth,key_doge)
        bot.send_message(message.from_user.id, 'Choose Your Coin', reply_markup=keyboard)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == 'BTCUSD':
             try:
                 req = rq.get("https://yobit.net/api/3/ticker/btc_usd")
                 response = req.json()
                 sell_price = response["btc_usd"]['sell']
                 bot.send_message(
                     message.chat.id,
                     f"{dt.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                 )

             except Exception as ex:
                 print(ex)
                 bot.send_message(
                     message.chat.id,
                     'Damn...Something was wrong'
                 )
        elif message.text == 'ETHUSD':
            try:
                req = rq.get("https://yobit.net/api/3/ticker/eth_usd")
                response = req.json()
                sell_price = response["eth_usd"]['sell']
                bot.send_message(
                    message.chat.id,
                    f"{dt.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price: {sell_price}"
                )

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Damn...Something was wrong'
                )

        elif message.text == 'DOGEUSD':
            try:
                req = rq.get("https://yobit.net/api/3/ticker/doge_usd")
                response = req.json()
                sell_price = response["doge_usd"]['sell']
                bot.send_message(
                    message.chat.id,
                    f"{dt.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_price}"
                )

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Damn...Something was wrong'
                )
        else:
            bot.send_message(message.chat.id, 'Check command')
    bot.polling()

# if __name__ == '__main__':
#     telegram_bot(token)
#
telegram_bot(token)
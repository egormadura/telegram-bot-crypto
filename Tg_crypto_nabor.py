from telebot import TeleBot, types
import random

bot = TeleBot(token='6882251487:AAExMhiNsI7lWItFE8BZnEWyl50QI6k87gc', parse_mode='html')  # Замените 'YOUR_BOT_TOKEN' на фактический токен вашего бота

# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Новости 🗞")
    btn2 = types.KeyboardButton("Чарты 🔝")
    btn3 = types.KeyboardButton("Графики 📈")
    btn4 = types.KeyboardButton("Ончейн анализ 📊")
    btn5 = types.KeyboardButton("Индикаторы 🆘")
    btn6 = types.KeyboardButton("Биржи 💱")
    btn7 = types.KeyboardButton("Эскпрореры 🔎")
    btn8 = types.KeyboardButton("Ютуб-каналы 🎥")
    btn9 = types.KeyboardButton("Телеграм-каналы 📧")
    btn10 = types.KeyboardButton("NFT 🖼")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Погрузтимся в криптовалютный мир 🙃? Выберите категорию!".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://media.giphy.com/media/l49JMVDvP8D38LHwI/giphy.gif', None, 'Text')

    # Обработчик инлайн-кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
    user_data = bot.get_chat_member(call.message.chat.id, user_id).user
    current_section = user_data.id  # Используем ID пользователя в качестве ключа для отслеживания текущего раздела

    if call.data == "other_section":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Новости 🗞")
        btn2 = types.KeyboardButton("Чарты 🔝")
        btn3 = types.KeyboardButton("Графики 📈")
        btn4 = types.KeyboardButton("Ончейн анализ 📊")
        btn5 = types.KeyboardButton("Индикаторы 🆘")
        btn6 = types.KeyboardButton("Биржи 💱")
        btn7 = types.KeyboardButton("Эскпрореры 🔎")
        btn8 = types.KeyboardButton("Ютуб-каналы 🎥")
        btn9 = types.KeyboardButton("Телеграм-каналы 📧")
        btn10 = types.KeyboardButton("NFT 🖼")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(call.message.chat.id, text="Выберите раздел", reply_markup=markup)
    elif call.data == "back":
        # Вернуть пользователя в предыдущий раздел
        # Здесь вы можете добавить логику для определения предыдущего раздела и настройки клавиатуры соответственно
        bot.send_message(call.message.chat.id, text="Вы вернулись в предыдущий раздел")
    else:
        # Обработка других инлайн-кнопок
        pass

# Обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Новости 🗞":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Bitcoin 24", url="https://www.block-chain24.com/")
        btn2 = types.InlineKeyboardButton("Forklog", url="https://forklog.com/")
        btn3 = types.InlineKeyboardButton("Crunchbase", url="https://www.crunchbase.com/")
        btn4 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3,btn4)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)
    elif message.text == "Чарты 🔝":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Coin Market Cap", url="https://coinmarketcap.com/ru/")
        btn2 = types.InlineKeyboardButton("Drops Tab", url="https://dropstab.com/")
        btn3 = types.InlineKeyboardButton("CoinGecko", url="https://www.coingecko.com/ru")
        btn4 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3,btn4)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)        
    elif message.text == "Графики 📈":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Trading View", url="https://ru.tradingview.com/")
        btn2 = types.InlineKeyboardButton("Messari", url="https://messari.io")
        btn3 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)
    elif message.text == "Ончейн анализ 📊":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Glassnode", url="https://studio.glassnode.com/")
        btn2 = types.InlineKeyboardButton("Santiment", url="https://app.santiment.net/")
        btn3 = types.InlineKeyboardButton("Cryptoed", url="https://cryptoyed.com/ru/")
        btn4 = types.InlineKeyboardButton("Token Terminal", url="https://tokenterminal.com/")
        btn5 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3,btn4,btn5)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)
    elif message.text == "Индикаторы 🆘":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Страха и жадности", url="https://alternative.me/crypto/fear-and-greed-index/")
        btn2 = types.InlineKeyboardButton("Bitcoin Rainbow Chart", url="https://www.blockchaincenter.net/en/bitcoin-rainbow-chart/")
        btn3 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)
    elif message.text == "Биржи 💱":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Coin Market Cap", url="https://coinmarketcap.com/exchanges/")
        btn2 = types.InlineKeyboardButton("Другие биржи", url="https://example.com/exchanges/")
        btn3 = types.InlineKeyboardButton("Выбрать другой раздел", callback_data="other_section")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)       
    elif message.text == "Эскпрореры 🔎":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Ethereum", url="https://etherscan.io/")
        btn2 = types.InlineKeyboardButton("BSC", url="https://bscscan.com/")
        btn3 = types.InlineKeyboardButton("Tron", url="https://tronscan.org")
        btn4 = types.InlineKeyboardButton("Polkadot", url="https://acala.subscan.io/")
        btn5 = types.InlineKeyboardButton("Atom", url="https://hub.mintscan.io/")
        btn6 = types.InlineKeyboardButton("Solana", url="https://explorer.solana.com/")
        btn7 = types.InlineKeyboardButton("Polygon", url="https://polygonscan.com/")
        btn8 = types.InlineKeyboardButton("Chia", url="https://www.chiaexplorer.com/blockchain/search")
        btn9 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8,btn9)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)       
    elif message.text == "Ютуб-каналы 🎥":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Слезы Сатоши", url="https://www.youtube.com/@SATOSHIFRIENDS")
        btn2 = types.InlineKeyboardButton("Юра Франциско", url="https://www.youtube.com/@Cryptofriends")
        btn3 = types.InlineKeyboardButton("Геннадий М", url="https://www.youtube.com/@GennadyM")
        btn4 = types.InlineKeyboardButton("Ридван", url="https://www.youtube.com/@GenesisRidvan")
        btn5 = types.InlineKeyboardButton("Трэйдер 80/20", url="https://www.youtube.com/@Trader8020")
        btn6 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)       
    elif message.text == "Телеграм-каналы 📧":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Рафаэль 'Слезы Сатоши'", url="https://t.me/slezisatoshi")
        btn2 = types.InlineKeyboardButton("Юра Франциско 'Crypto Family'", url="https://t.me/CryptoFamilyPublic")
        btn3 = types.InlineKeyboardButton("Ридван 'Crypto Family'", url="https://t.me/genesis_daily_news")
        btn4 = types.InlineKeyboardButton("Геннадий М ", url="https://t.me/gen_m")
        btn5 = types.InlineKeyboardButton("Трэйдер 80/20 ", url="https://t.me/tradertrend")
        btn6 = types.InlineKeyboardButton("Crypto Headlines", url="https://t.me/crypto_hd")
        btn7 = types.InlineKeyboardButton("Нарнийская центрифуга", url="https://t.me/narnian_cfg")
        btn8 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)       
    elif message.text == "NFT 🖼":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("OpenSea", url="https://opensea.io")
        btn2 = types.InlineKeyboardButton("X2Y2", url="https://x2y2.io/#")
        btn2 = types.InlineKeyboardButton("Dappradar", url="https://dappradar.com/")
        btn3 = types.InlineKeyboardButton("Выбрать другой раздел ◀", callback_data="other_section")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите сервис", reply_markup=markup)       
                                       
    # Добавьте обработчики для других разделов

    elif message.text == "Выбрать другой раздел ◀":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Новости 🗞")
        btn2 = types.KeyboardButton("Чарты 🔝")
        btn3 = types.KeyboardButton("Графики 📈")
        btn4 = types.KeyboardButton("Ончейн анализ 📊")
        btn5 = types.KeyboardButton("Индикаторы 🆘")
        btn6 = types.KeyboardButton("Биржи 💱")
        btn7 = types.KeyboardButton("Эскпрореры 🔎")
        btn8 = types.KeyboardButton("Ютуб-каналы 🎥")
        btn9 = types.KeyboardButton("Телеграм-каналы 📧")
        btn10 = types.KeyboardButton("NFT 🖼")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню 👈", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Не понимаю тебя 😟")

# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()

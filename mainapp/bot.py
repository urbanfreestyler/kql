def send_application(name, phone, email):
    import telebot
    bot = telebot.TeleBot("TOKEN")

    chat_id = "-1001662935535"

    bot.send_message(chat_id=chat_id, text="Новая заявка:\n"
                                                "Имя: " + name + "\n"
                                                 "Номер: " + phone + "\n"
                                                 "E-mail: " + email)

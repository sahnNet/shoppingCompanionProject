import telebot
import classifierFind as cff
import database as db

# Build a telegram robot with a registered token
bot = telebot.TeleBot(token="5328326614:AAEKpInGPpIB4JAp9LPQA5QrxzS5Ho8LMv4")
orders = []


# Check the type and request of the user
def check_command(command: str, user_chat_id: int):
    result = None
    if command == "/start":
        result = '''سلام
من همراه خرید شما هستم😎
چی نیاز داری؟ بهم بگو🧐'''

    else:
        intent = cff.get_classification([command])[0]
        if intent == "دونه ای" or intent == "کیلویی":
            orders.append(command)
        if len(orders) == 2:
            pass
        else:
            result = cff.get_answer_intent(intent)

    return result


# Executive function in response to the user's message
@bot.message_handler(content_types=['text'])
def main(user):
    if not user.from_user.is_bot:
        result = check_command(user.text, user.chat.id)
        if result is not None:
            bot.send_message(user.chat.id, result)


# Specify the execution cycle for each user
# Always running
bot.polling(none_stop=True)

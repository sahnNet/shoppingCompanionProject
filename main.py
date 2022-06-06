import telebot
import classifierFind as cff
import database as db

# Build a telegram robot with a registered token
bot = telebot.TeleBot(token="5328326614:AAEKpInGPpIB4JAp9LPQA5QrxzS5Ho8LMv4")
orders = []
flag = False


# Check the type and request of the user
def check_command(command: str, user_chat_id: int):
    global flag
    result = None
    if command == "/start":
        result = '''سلام
من همراه خرید شما هستم😎
چی نیاز داری؟ بهم بگو🧐'''

    else:
        intent = cff.get_classification([command])

        if (intent == "دونه ای" or intent == "کیلویی") or (intent == "عدد" and len(orders) == 1):
            orders.append(command)

        elif (intent == "بله" or command == "بله") and flag:
            user_id = db.add_user(user_chat_id)
            bill_id = db.add_bill(user_id)
            db.close_bill(bill_id)
            result = f'''فاکتور ثبت شد
            کد فاکتور : {bill_id}'''
            flag = False

            return result

        elif flag:
            result = f"فاکتور نهایی نشد"
            flag = False

            return result

        if len(orders) == 2:
            user_id = db.add_user(user_chat_id)
            bill_id = db.add_bill(user_id)
            order_id = db.add_order(bill_id, orders[0], orders[1])
            orders.clear()

            result = f'''سفارش ثبت شد
            کد سفارش : {order_id}'''

        elif intent == "لیست خرید" or command == "لیست خرید" or command == "فاکتور":
            result = ''
            flag = True
            user_id = db.add_user(user_chat_id)
            bill_id = db.add_bill(user_id)

            for o in db.get_orders_by_bill_id(bill_id):
                result += f"{o[0]} : {o[1]}\n"

            result += "فاکتور را تایید می کنید؟"
            result += "\n"
            result += "بله/خیر"

        elif intent == "تاریخچه لیست های خرید":
            result = ''
            user_id = db.add_user(user_chat_id)
            bills_id = db.get_close_bills_id(user_id)

            for bill_id in bills_id:
                result += f"کد فاکتور = {bill_id[0]}\n"
                for o in db.get_orders_by_bill_id(bill_id[0]):
                    result += f"{o[0]} : {o[1]}\n"
                result += "\n"

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

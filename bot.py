import constants as keys
import responses as r
from telegram import Update
from telegram.ext import *

print("Bot is waking up.")

def start_command(update, context):
    update.message.reply_text('Type something to get started')

def help_command(update, context):
    update.message.reply_text('I will do my best!')

def handle_command(update, context):
    print(f"update: {update.message.reply_text}")
    input_message = str(update.message.text).lower()
    response = r.sample_responses(input_message)

    update.message.reply_text(response)

def echo(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def error(update, context):
    print(f"Update {update} caused an error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_command))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
# if __name__ == '__main__':
#     application = ApplicationBuilder().token(keys.API_KEY).build()
#
#     application.add_handler(CommandHandler("start", start_command))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(MessageHandler(Filters.text, handle_command))
#     application.add_error_handler(error)
#
#     application.run_polling()

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import bot_commands



app = ApplicationBuilder().token("5668929474:AAFqbzsH1tq42necRpTPS9tmV_A9rxFn16c").build()


app.add_handler(CommandHandler("hello", bot_commands.hello))
app.add_handler(CommandHandler("calc", bot_commands.calculate_command))
app.add_handler(MessageHandler(filters.TEXT, bot_commands.calculate))



print('Сервер запустился')
app.run_polling()
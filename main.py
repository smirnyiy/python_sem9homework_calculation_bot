from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from controller import *

app = ApplicationBuilder().token("YOUR TOKEN").build()
app.add_handler(CommandHandler("start", hi_commands))
app.add_handler(CommandHandler("menu", menu_commands))
app.add_handler(CommandHandler("sum", sum_commands))
app.add_handler(CommandHandler("mult", mult_commands))
app.add_handler(CommandHandler("dif", dif_commands))
app.add_handler(CommandHandler("div", div_commands))
print('start server')
app.run_polling()
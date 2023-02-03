from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *

async def hi_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}, выбери /menu')

async def menu_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Напиши действие и 2 числа через пробел:\n/sum - сложение\n/mult - умножение\n/dif - разница\n/div - деление\n Например /sum 2 2 или /mult 5 3')
    
async def sum_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')

async def mult_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}*{y}={x*y}')

async def div_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}/{y}={x/y}')

async def dif_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}-{y}={x-y}')
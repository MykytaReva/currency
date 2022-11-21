import httpx
from telegram import ForceReply, Update, \
    InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler,\
    ContextTypes, MessageHandler, filters, CallbackQueryHandler

from config import settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
            InlineKeyboardButton("Option 3", callback_data="3"),
        ],
        [InlineKeyboardButton("Option 4", callback_data="4")],
        [InlineKeyboardButton("Option 5", callback_data="5")],
        [
            InlineKeyboardButton("Option 6", callback_data="6"),
            InlineKeyboardButton("Option 7", callback_data="7"),
            InlineKeyboardButton("Option 8", callback_data="8"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Please choose the option:', reply_markup=reply_markup)

async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    print(user)
    await update.message.reply_text(
        f'''Your id -->>{user.id}.
Your username -->> {user.username}.'''
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


async def get_rate_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = settings.rates_url
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        rates_list = response.json()
        await update.message.reply_text(str(rates_list))

async def last_rate_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = settings.rates_url
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        rates_list = response.json()
        await update.message.reply_text(rates_list['results'][-1])

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option -->> {query.data}")

def main() -> None:

    TOKEN = settings.telegram_token
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("user_id", user_id))
    application.add_handler(CommandHandler("rates", get_rate_list))
    application.add_handler(CommandHandler("last_rate", last_rate_list))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


if __name__ == "__main__":
    main()
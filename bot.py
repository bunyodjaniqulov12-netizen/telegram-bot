from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8652061733:AAHTvr7o5nQEN77SKi6v-i16Rq4ShkLUxg0"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! 🤖 Menga xabar yoz!")


async def javob(update: Update, context: ContextTypes.DEFAULT_TYPE):
    matn = update.message.text

    if matn.lower() == "salom":
        await update.message.reply_text("Salom! 😊 Qalaysan?")
    elif matn.lower() == "qalaysan":
        await update.message.reply_text("Yaxshi, rahmat! 🤖")
    else:
        await update.message.reply_text("Sening xabaring: " + matn)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, javob))

print("BOT ISHLADI!")

app.run_polling()
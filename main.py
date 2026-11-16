import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلا بيك في رَدّك 👋\n"
        "ابعتلي رسالة عميلك، وأنا اقترح عليك 3 ردود.\n"
        "جرب /help عشان تشوف الأوامر."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - البداية\n"
        "/analyze - حلل رسالة\n"
        "/templates - قوالب جاهزة\n"
        "/lang - اللغة\n"
        "/help - المساعدة\n\n"
        "ابعت أي رسالة على طول وأنا هحللها."
    )

async def templates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "قوالب جاهزة:\n\n"
        "1- محترم: شكرا لرسالتك، هرد عليك بأسرع وقت 🙏\n"
        "2- قوي: الكلام ده مش مقبول، خلينا نتكلم باحترام.\n"
        "3- ساخر: واضح إنك فاضي، بس أنا مشغول 😅"
    )

async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اللغة الحالية: عربي مصري 🇪🇬")

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(
        f"حللت رسالتك: {text}\n\n"
        "1- رد محترم: فهمت وجهة نظرك، خلينا نوصل لحل يرضينا.\n"
        "2- رد قوي: مش هقبل بالطريقة دي، لو سمحت اتكلم باحترام.\n"
        "3- رد ساخر: حلو الكلام ده، بس جرب تاني بطريقة أحسن 😅\n\n"
        "لو عايز تعدل الأسلوب، قولي."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("templates", templates))
    app.add_handler(CommandHandler("lang", lang))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze))
    print("Bot started...")
    app.run_polling()

if name == "main":
    main()

import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Inserisci il tuo token qui
TOKEN = "8495927717:AAHYljBoR1WTYLPyePb2I_ezbggALpIwl2s"

# Frasi personalizzate
messaggi = {
    "💙 Frasi per quando sei triste": [
        "Amo la pace che c’è quando siamo soli io e te",
        "Dei lampioni che ho incontrato sei l’unico che mi ha indicato la strada",
        "Non è noia non fare nulla insieme a te",
        "Per due come noi…<3",
        "Il mio vuoto sta prendendo la tua forma"
    ],
    "🎵 Frasi di canzoni in cui ti penso": [
        "Ora che so cos’è l’amore ho paura, che tu vada via",
        "Bella così che se non ti conoscessi penserei alla madre dei figli miei",
        "Notte e giorno non c’è sonno quando sei qui con me",
        "Che palle fare after con i fantasmi tu mi mandi, mi mancano i tuoi occhi e mi mancano i tuoi sguardi",
        "Ho bisogno di sentire più amore e meno stress",
        "Anche se quando c’eri tu sembrava bello stare fermi a non fare niente"
    ],
    "🌅 Momenti felici che abbiamo passato": [
        "Ti ricordi del pranzo che abbiamo fatto in Toscana e immaginavamo la nostra vita insieme in quel casale?",
        "Per tutte le volte che ho sognato di viaggiare in Giappone insieme",
        "Quante volte ci sentiamo critici culinari girando per più ristoranti",
        "Amo parlare della prossima ricetta che possiamo cucinare a casa mia",
        "Ma quanto eravamo belli a Perugia, mentre cantavamo insieme 'sto bene'?"
    ]
}

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tastiera = ReplyKeyboardMarkup(
        [["💙 Frasi per quando sei triste"],
         ["🎵 Frasi di canzoni in cui ti penso"],
         ["🌅 Momenti felici che abbiamo passato"]],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    await update.message.reply_text(
        "Ciao amore ❤️\nScegli cosa vuoi leggere oggi:",
        reply_markup=tastiera
    )

# Gestione dei messaggi (risposta ai bottoni)
async def rispondi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    testo = update.message.text
    if testo in messaggi:
        frase = random.choice(messaggi[testo])
        await update.message.reply_text(frase)
    else:
        await update.message.reply_text("Tocca uno dei pulsanti per ricevere un messaggio 💌")

# Avvio del bot
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, rispondi))
    app.run_polling()

if __name__ == "__main__":
    main()

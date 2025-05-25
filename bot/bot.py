from sqlalchemy.future import select
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from database.database import SessionLocal
from database.models import User

first_lesson = "📚 *Cours 1 : Bonjour* → 'Bonjour' = *مرحبا* (marḥaban)"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        user = result.scalar()
        if not user:
            session.add(User(user_id=user_id, lesson_id=0))
            await session.commit()
        await update.message.reply_text(first_lesson, parse_mode="Markdown")

def setup_bot(token: str):
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    return app

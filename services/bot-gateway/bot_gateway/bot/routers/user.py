import logging

from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def procces_start_command(message: Message, i18n: TranslatorRunner):
    # Добавил заглушку на user, так как если вызывавется в канале, то from_user отсутствует Optional[str]
    username = html.quote(message.from_user.full_name) if message.from_user else "John Doe"
    await message.answer(text=i18n.user.greeting(username=username))

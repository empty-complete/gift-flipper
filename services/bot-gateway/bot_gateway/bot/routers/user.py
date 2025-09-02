import logging

from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def procces_start_command(message: Message, i18n: TranslatorRunner):
    username = html.quote(message.from_user.full_name)
    await message.answer(text=i18n.user.greeting(username=username))

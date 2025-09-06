import logging

from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from bot_gateway.bot.keyboards import menu

logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def procces_start_command(message: Message, i18n: TranslatorRunner):
    # Добавил заглушку на user, так как если вызывавется в канале, то from_user отсутствует Optional[str]
    username = html.quote(message.from_user.full_name) if message.from_user else "John Doe"
    await message.answer_photo(
        photo="https://i.ibb.co/gChf9ng/photo-2025-08-18-10-30-00.jpg",
        caption=i18n.user.greeting(username=username),
        show_caption_above_media=True,
        reply_markup=menu.get_keyboard(
            i18n=i18n, search_status=True
        ),  # TODO: Нужно добавить search_status
    )

from datetime import datetime

import pytest
from aiogram import html
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.enums import ChatType
from aiogram.methods import SendPhoto
from aiogram.methods.base import TelegramType
from aiogram.types import Chat, Message, Update, User


@pytest.mark.asyncio
@pytest.mark.parametrize("locale", ["ru", "en"])
async def test_cmd_start(dp, bot, translator_hub, locale):
    bot.add_result_for(
        method=SendPhoto,
        ok=True,
    )
    chat = Chat(id=1234567, type=ChatType.PRIVATE)
    user = User(id=1234567, is_bot=False, first_name="User", language_code=locale)
    message = Message(message_id=1, chat=chat, from_user=user, text="/start", date=datetime.now())
    result = await dp.feed_update(
        bot,
        Update(message=message, update_id=1),
        _translator_hub=translator_hub,
    )
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()  # type: ignore # [6]

    assert isinstance(outgoing_message, SendPhoto)
    i18n = translator_hub.get_translator_by_locale(locale)
    # Здесь просто проверяем текст сообщения, которое отправил бот
    assert outgoing_message.caption == i18n.user.greeting(
        username=html.quote(user.first_name or "")
    )

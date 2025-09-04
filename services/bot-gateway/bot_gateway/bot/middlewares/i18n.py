import logging
from collections.abc import Awaitable, Callable
from typing import Any, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub

logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        user: User = cast(User, data.get("event_from_user"))

        hub: TranslatorHub = cast(TranslatorHub, data.get("_translator_hub"))
        locale = user.language_code or getattr(hub, "default_locale", None) or "ru"
        data["i18n"] = hub.get_translator_by_locale(locale=locale)

        return await handler(event, data)

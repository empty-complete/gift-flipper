from __future__ import annotations

import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot_gateway.config.settings import Settings

# TODO: from bot_gateway.bot.middleware.request_id import RequestidMiddleware

logger = logging.getLogger(__name__)

# TODO: from bot_gateway.bot.routers import commands_router, start_dialog, settings_dialog

# TODO: nats servers connection


def build_bot(settings: Settings) -> Bot:
    token: str = settings.telegram.token.get_secret_value()
    parse_mode: str = settings.telegram.parse_mode

    bot = Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=ParseMode(parse_mode), link_preview_is_disabled=True
        ),
    )
    return bot


def build_dispatcher(settings: Settings) -> Dispatcher:
    # TODO: nats servers connection
    dp = Dispatcher(storage=None)  # TODO: nats storage
    return dp


def build_app(settings: Settings) -> tuple[Bot, Dispatcher]:
    return build_bot(settings=settings), build_dispatcher(settings=settings)

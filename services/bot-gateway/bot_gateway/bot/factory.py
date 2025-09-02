from __future__ import annotations

import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# TODO: from bot_gateway.bot.middleware.request_id import RequestidMiddleware
from dynaconf import LazySettings

logger = logging.getLogger(__name__)

# TODO: from bot_gateway.bot.routers import commands_router, start_dialog, settings_dialog

# TODO: nats servers connection


def build_bot(settings: LazySettings) -> Bot:
    try:
        token: str = settings.token
    except AttributeError:
        token = "7374156483:BBHwikKjwllXjfzzgWV12i8g8E3udHNJGYW"
        logger.warning("settings.token not found, using fake token: %s", token)

    parse_mode: str = settings.bot.parse_mode

    bot = Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=ParseMode(parse_mode), link_preview_is_disabled=True
        ),
    )
    return bot


def build_dispatcher(settings: LazySettings) -> Dispatcher:
    # TODO: nats servers connection
    dp = Dispatcher(storage=None)  # TODO: nats storage
    return dp


def build_app(settings: LazySettings) -> tuple[Bot, Dispatcher]:
    return build_bot(settings=settings), build_dispatcher(settings=settings)

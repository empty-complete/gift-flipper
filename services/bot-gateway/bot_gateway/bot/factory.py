from __future__ import annotations

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# import logging
# TODO: from bot_gateway.bot.middleware.request_id import RequestidMiddleware
from dynaconf import LazySettings

# logger = logging.getLogger(__name__)

# TODO: from bot_gateway.bot.routers import commands_router, start_dialog, settings_dialog

# TODO: nats servers connection


# TODO: check config.py
def build_bot(settings: LazySettings) -> Bot:
    bot = Bot(
        token=str(settings.token),
        default=DefaultBotProperties(parse_mode=ParseMode(str(settings.bot.parse_mode))),
    )
    return bot


def build_dispatcher(settings: LazySettings) -> Dispatcher:
    # TODO: nats servers connection
    dp = Dispatcher(storage=None)  # TODO: nats storage
    return dp

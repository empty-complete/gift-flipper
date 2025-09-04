import asyncio
import logging

from fluentogram import TranslatorHub

from bot_gateway.bot.factory import build_app
from bot_gateway.bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot_gateway.bot.routers import get_routers
from bot_gateway.config.settings import get_settings
from bot_gateway.utils.i18n import create_translator_hub


async def main() -> None:
    """Placeholder entrypoint"""
    settings = get_settings()
    logging.basicConfig(
        format=settings.logs.format_,
        level=settings.logs.level_name,
    )

    bot, dp = build_app(settings=settings)

    # Создаем объект типа TranslatorHub
    translator_hub: TranslatorHub = create_translator_hub()

    # Skip collected updates
    await bot.delete_webhook(drop_pending_updates=True)

    # Include routers and middlewares
    dp.include_routers(*get_routers())
    dp.update.middleware(TranslatorRunnerMiddleware())

    # Run polling
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == "__main__":
    asyncio.run(main())

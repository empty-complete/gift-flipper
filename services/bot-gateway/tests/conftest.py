import pytest
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot_gateway.bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot_gateway.bot.routers import get_routers
from bot_gateway.utils.i18n import create_translator_hub
from fluentogram import TranslatorHub
from mocked_aiogram import MockedBot, MockedSession


@pytest.fixture(scope="session")
def dp() -> Dispatcher:
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_routers(*get_routers())
    dispatcher.update.middleware(TranslatorRunnerMiddleware())
    return dispatcher


@pytest.fixture(scope="session")
def bot() -> MockedBot:
    bot = MockedBot()
    bot.session = MockedSession()
    return bot


@pytest.fixture(scope="session")
def translator_hub() -> TranslatorHub:
    return create_translator_hub()

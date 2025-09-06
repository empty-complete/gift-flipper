import logging

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fluentogram import TranslatorRunner

logger = logging.getLogger(__name__)


def get_keyboard(i18n: TranslatorRunner, search_status: bool):
    search_button: list[str] = [
        i18n.menu.start() if not search_status else i18n.menu.stop(),
    ]

    static_buttons: list[str] = [
        i18n.menu.profile(),
        i18n.menu.filters(),
    ]

    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*map(lambda x: KeyboardButton(text=x), search_button))
    kb_builder.row(*map(lambda x: KeyboardButton(text=x), static_buttons))

    return kb_builder.as_markup(resize_keyboard=True)

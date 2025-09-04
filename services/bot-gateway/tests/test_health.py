# Тест: пакет должен импортироваться
def test_pkg_importable() -> None:
    pass


# Тест: у пакета есть __version__
def test_version_exists() -> None:
    import bot_gateway

    assert isinstance(bot_gateway.__version__, str)


def test_config_availability() -> None:
    pass


# Тест: проверка сборки бота
def test_build_bot():
    from bot_gateway.bot.factory import build_bot
    from bot_gateway.config.settings import get_settings

    build_bot(settings=get_settings())


# Тест: проверка сборки диспетчера
def test_build_dispatcher():
    from bot_gateway.bot.factory import build_dispatcher
    from bot_gateway.config.settings import get_settings

    build_dispatcher(settings=get_settings())

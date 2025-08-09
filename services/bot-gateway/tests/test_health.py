# Тест: пакет должен импортироваться
def test_pkg_importable() -> None:
    import bot_gateway  # noqa: F401  # Импорт и игнор "неиспользуемая переменная"


# Тест: у пакета есть __version__
def test_version_exists() -> None:
    import bot_gateway

    assert isinstance(bot_gateway.__version__, str)  # Должна быть строка

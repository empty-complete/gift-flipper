from pathlib import Path

from dynaconf import Dynaconf

BASE_DIR = Path(__file__).resolve().parent.parent

# TODO: add settings schema: https://github.com/dynaconf/dynaconf/issues/651#issuecomment-912410244

settings = Dynaconf(
    envvar_prefix="BOT_GATEWAY",
    settings_files=[
        BASE_DIR / "config" / "settings.toml",
        BASE_DIR / "config" / ".secrets.toml",
    ],
    environments=True,
    load_dotenv=True,
)

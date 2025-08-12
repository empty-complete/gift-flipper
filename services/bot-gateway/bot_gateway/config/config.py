from pathlib import Path

from dynaconf import Dynaconf

BASE_DIR = Path(__file__).resolve().parent.parent
settings = Dynaconf(
    envvar_prefix="BOT_GATEWAY",
    settings_files=[
        BASE_DIR / "config" / "settings.toml",
        BASE_DIR / "config" / ".secrets.toml",
    ],
    environments=True,
    load_dotenv=True,
)

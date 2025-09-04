from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class Logs(BaseModel):
    level_name: str = "DEBUG"
    format_: str = "[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s"


class Telegram(BaseModel):
    token: SecretStr = SecretStr("7374156483:BBHwikKjwllXjfzzgWV12i8g8E3udHNJGYW")
    parse_mode: Literal["HTML", "Markdown", "MarkdownV2"] = "HTML"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )

    telegram: Telegram = Telegram()
    logs: Logs = Logs()


@lru_cache
def get_settings() -> Settings:
    return Settings()

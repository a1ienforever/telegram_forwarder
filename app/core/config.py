from dataclasses import dataclass, field
from typing import Optional

from dotenv import load_dotenv
from icecream import install
from pydantic_settings import BaseSettings, SettingsConfigDict

install()
ic.configureOutput(includeContext=True)

class CustomBaseSettings(BaseSettings):
    """Базовый класс для всех конфигураций."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DatabaseConfig(CustomBaseSettings):

    host: str = "localhost"
    password: str = "<PASSWORD>"
    user: str = "root"
    name: str = "root"
    port: int = 5432

    def dsn(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class TelegramConfig(CustomBaseSettings):

    token: str = "Token"
    admin_ids: list[int] = []
    use_redis: bool = False
    bot_name: str = "bot_name"


class RedisConfig(CustomBaseSettings):

    password: Optional[str] = None
    port: int = 6379
    host: str = "localhost"

    def dsn(self) -> str:
        if self.redis_pass:
            return f"redis://:{self.redis_pass}@{self.redis_host}:{self.redis_port}/0"
        return f"redis://{self.redis_host}:{self.redis_port}/0"


class UserBotConfig(CustomBaseSettings):

    api_id: Optional[int] = None
    api_hash: Optional[str] = None
    phone: Optional[str] = None
    login: Optional[str] = None


class Settings(CustomBaseSettings):
    telegram: TelegramConfig = TelegramConfig()
    database: DatabaseConfig = DatabaseConfig()
    redis: RedisConfig = RedisConfig()
    user_bot: UserBotConfig = UserBotConfig()


settings = Settings()

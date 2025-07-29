
from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    """Базовый класс для настроек с поддержкой переопределения префикса для переменных окружения."""
    ...

class DatabaseConfig(CustomBaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="DATABASE_")

    host: str = None
    password: str = None
    user: str = None
    database: str = None
    port: int = 5432

    def dsn(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"



class TelegramConfig(CustomBaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="TELEGRAM_")
    token: str = None
    admin_ids: list[int] = []
    use_redis: bool = None
    bot_name: str = None


class RedisConfig(CustomBaseSettings):
    """
    Redis configuration class.

    Attributes
    ----------
    redis_pass : Optional(str)
        The password used to authenticate with Redis.
    redis_port : Optional(int)
        The port where Redis server is listening.
    redis_host : Optional(str)
        The host where Redis server is located.
    """
    model_config = SettingsConfigDict(env_file=".env", env_prefix="REDIS_")

    redis_pass: str = None
    redis_port: int = None
    redis_host: str = None

    def dsn(self) -> str:
        """
        Constructs and returns a Redis DSN (Data Source Name) for this database configuration.
        """
        if self.redis_pass:
            return f"redis://:{self.redis_pass}@{self.redis_host}:{self.redis_port}/0"
        else:
            return f"redis://{self.redis_host}:{self.redis_port}/0"


class Settings:
    telegram: TelegramConfig = TelegramConfig()
    redis: RedisConfig = RedisConfig()
    database: DatabaseConfig = DatabaseConfig()


settings = Settings()

import logging

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage

from app.core.config import Settings


def get_storage(config: Settings) -> RedisStorage | MemoryStorage:
    if config.telegram.use_redis:
        logging.info("Redis successful connect")
        redis = RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
        return redis

    else:
        return MemoryStorage()
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core import settings

engine = create_async_engine(settings.database.dsn(), echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session



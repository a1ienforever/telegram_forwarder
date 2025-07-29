from sqlalchemy import select

from app.core.dependencies import SessionDep
from app.domain.interfaces.repositories.base_repo import BaseRepositories, T


class BaseRepo(BaseRepositories):
    model = None
    mapper = None

    @classmethod
    async def get_all(cls, session: SessionDep) -> list[T]:
        query = select(cls.model)
        result = await session.execute(query).scalars().all()
        return cls.mapper.to_entity_list(result)

    @classmethod
    async def get_by_id(cls, session: SessionDep, id: int) -> T | None:
        query = select(cls.model).filter_by(id=id)
        result = await session.execute(query).scalar_one_or_none()
        return cls.mapper.to_entity(result)

    @classmethod
    async def create(cls, session: SessionDep, entity: T) -> T:
        instance = cls.model(**entity)
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        return cls.mapper.to_entity(instance)

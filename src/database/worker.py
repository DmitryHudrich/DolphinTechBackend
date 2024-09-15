from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine,
)
from src.settings import Settings
from src.database.mainbase import MainBase
from typing import Final, Type


class DBWorker:
    _ENGINE_DB: Final[AsyncEngine] = create_async_engine(
        url=Settings.db_url, echo=Settings.echo
    )
    _ASYNC_SESSION: Final[AsyncSession] = async_sessionmaker(_ENGINE_DB)

    @classmethod
    @property
    def engine(cls) -> AsyncEngine:
        return cls._ENGINE_DB

    @classmethod
    async def create_tables(cls) -> None:
        async with cls._ENGINE_DB.begin() as session:
            await session.run_sync(MainBase.metadata.create_all)

    @classmethod
    async def get_session(cls) -> AsyncSession:
        async with cls._ASYNC_SESSION() as session:
            return session

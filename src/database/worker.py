from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession, AsyncEngine
from src.settings import Settings
from src.database.mainbase import MainBase
from typing import Final, Type


class DBWorker:

    _ENGINE_DB: Final[Type[AsyncEngine]] = create_async_engine(url=Settings.db_url, echo=Settings.echo)
    _ASYNC_SESSION: Final[Type[AsyncSession]] = async_sessionmaker(self.engine_db)

    async def create_tables(self) -> None:
        async with self._ENGINE_DB.begin() as session:
            await session.run_sync(MainBase.metadata.create_all)
    
    async def get_session(self) -> AsyncSession:
        
        async with self._ASYNC_SESSION() as session:
            return session
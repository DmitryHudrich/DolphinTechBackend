from src.database.repository.user_repository import UserRepository
from src.database.repository.note_repository import NoteRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.worker import DBWorker
from typing import Type
from abc import ABC, abstractclassmethod

class IEngineRepository:

    user_rep: Type[UserRepository]
    note_rep: Type[NoteRepository]

    @abstractclassmethod
    def __init__(self): pass

    @abstractclassmethod
    async def __aenter__(self):pass

    @abstractclassmethod
    async def __aexit__(self, *args): pass


class EngineRepository(IEngineRepository):
    
    def __init__(self) -> None:
        self.session: AsyncSession

    async def __aenter__(self, *args, **kwargs) -> None:
        self.session = await DBWorker.get_session()

        self.user_rep = UserRepository()
        self.note_rep = NoteRepository()

    async def __aexit__(self, *args) -> None:
        self.session.close()

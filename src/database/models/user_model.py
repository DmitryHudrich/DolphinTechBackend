from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, BigInteger, ForeignKey
from src.database.mainbase import MainBase
from typing import List, Union, Dict


class UserTable(MainBase):

    username: Mapped[str] = mapped_column(type_=String(120), default="anonim", nullable=True, index=False, name="username", unique=False)
    tg_id: Mapped[int] = mapped_column(type_=BigInteger, nullable=True, index=False, name="tg_id", default=0)

    notes: Mapped[List["NoteTable"]] = relationship("NoteTable", back_populates="user", uselist=True)

    def read_model(self) -> Dict[str, Union[str, int]]:
        return {
            k: v
            for k, v in self.__dict__.items()
            if k != "_sa_instance_state"
        }

    def __str__(self) -> str:
        return str(self.read_model())

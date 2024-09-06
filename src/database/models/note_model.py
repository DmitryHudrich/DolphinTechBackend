from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, String, ForeignKey
from typing import Union, Dict
from src.database.mainbase import MainBase


class NoteTable(MainBase):

    theme: Mapped[str] = mapped_column(type_=String(100), name="theme_note", unique=False, index=True, nullable=False)
    main_text: Mapped[str] = mapped_column(type_=Text, name="main_txt", unique=False, index=False, nullable=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("UserTable.id"), type_=Integer, name="id_user")
    
    user: Mapped["UserTable"] = relationship("UserTable", back_populates="notes", uselist=False)

    def read_model(self) -> Dict[str, Union[str, int]]:
        return {
            k: v
            for k, v in self.__dict__.items()
            if k != "_sa_instance_state"
        }
    
    def __str__(self) -> str: return str(self.read_model())
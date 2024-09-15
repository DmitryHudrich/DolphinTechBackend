from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import Integer


class MainBase(DeclarativeBase):
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        return str(cls.__name__)

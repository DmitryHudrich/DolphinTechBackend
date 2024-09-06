from typing import Any, Final

class SettingsMeta(type):

    def __setattr__(cls, name: str, value: Any) -> None:
        if name in ("db_url", "echo", f"_Settings__DB_URL", f"_Settings__ECHO"):
            raise AttributeError("Данный атрибута нельзя изменять")

class Settings(metaclass=SettingsMeta):

    __DB_URL: Final[str] = "sqlite+aiosqlite:///./dolphine.db"
    __ECHO: Final[bool] = True

    @classmethod
    @property
    def db_url(cls) -> str:
        return cls.__DB_URL
    
    @classmethod
    @property
    def echo(cls) -> bool:
        return cls.__ECHO
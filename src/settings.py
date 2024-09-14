from typing import Any, Final
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class SettingsMeta(type):

    def __setattr__(cls, name: str, value: Any) -> None:
        if name in ("db_url", "echo", f"_Settings__DB_URL", f"_Settings__ECHO"):
            raise AttributeError("Данный атрибута нельзя изменять")

class Settings(metaclass=SettingsMeta):

    __DB_URL: Final[str] = "sqlite+aiosqlite:///./dolphine.db"
    __ECHO: Final[bool] = True

    #URLS
    __IUBIP_GROUP_URL: Final[str] = getenv("IUBIP_GROUPS_URL")
    __MOBILE_SCHEDULE_RKSI_URL: Final[str] = getenv("MOBILE_SCHEDULE_RKSI_URL")
    __SCHEDULE_RKSI_URL: Final[str] = getenv("SCHEDULE_RKSI_URL")
    __RGUPS_URL: Final[str] = getenv("RGUPS_URL")

    @classmethod
    @property
    def db_url(cls) -> str:
        return cls.__DB_URL
    
    @classmethod
    @property
    def echo(cls) -> bool:
        return cls.__ECHO

    @classmethod
    @property
    def mobile_schedule_rksi(cls) -> str: return cls.__MOBILE_SCHEDULE_RKSI_URL

    @classmethod
    @property
    def schedule_rksi(cls) -> str: return cls.__SCHEDULE_RKSI_URL

    @classmethod
    @property
    def iubip_group(cls) -> str: return cls.__IUBIP_GROUP_URL

    @classmethod
    @property
    def rgups_url(cls) -> str: return cls.__RGUPS_URL
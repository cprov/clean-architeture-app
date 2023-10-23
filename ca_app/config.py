import sys
import typing

from pydantic import (
    ConfigDict,
    ValidationError,
    field_validator,
)
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file = ".env")


    database_uri: typing.Optional[str]

    @field_validator("database_uri")
    def fill_database_uri(cls, v, values) -> str:
        if not v:
            return "sqlite:///./ca_app.db"
        return v


try:
    settings = Settings()
except ValidationError as e:
    print(e)
    sys.exit(1)

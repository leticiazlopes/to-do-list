from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

    # Defina um valor padrão, para que o campo não seja "required"
    DATABASE_URL: str = Field(default="sqlite:///./database.db")
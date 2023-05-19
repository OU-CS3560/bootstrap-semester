from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str

    class Config:
        env_prefix = ""
        case_sensitive = False


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    secret_key: str
    access_token_expire_minutes: int = 30

    class Config:
        env_prefix = ""
        case_sensitive = False


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "PAY2UHackathon"
    description: str = "PAY2UHackathon"
    secret: str = "SECRET"
    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
    )

    class Config:
        env_file = ".env"


settings = Settings()

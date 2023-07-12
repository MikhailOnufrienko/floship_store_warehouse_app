from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    STORE_DJANGO_SECRET_KEY: str
    STORE_ALLOWED_HOSTS: str = '127.0.0.1,localhost'
    STORE_DB_HOST: str = '127.0.0.1'
    STORE_DB_PORT: int = 5432
    STORE_DB_USER: str
    STORE_DB_PASSWORD: str
    STORE_DB_NAME: str = 'store_db'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


project_settings = Settings()

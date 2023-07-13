from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    WAREHOUSE_DJANGO_SECRET_KEY: str
    WAREHOUSE_ALLOWED_HOSTS: str = '127.0.0.1,localhost'
    WAREHOUSE_DB_HOST: str = '127.0.0.1'
    WAREHOUSE_DB_PORT: int = 5433
    WAREHOUSE_DB_USER: str
    WAREHOUSE_DB_PASSWORD: str
    WAREHOUSE_DB_NAME: str = 'warehouse_db'
    STORE_USERNAME: str
    STORE_PASSWORD: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


project_settings = Settings()

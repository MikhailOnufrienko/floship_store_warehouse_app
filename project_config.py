from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    STORE_DJANGO_SECRET_KEY: str
    STORE_ALLOWED_HOSTS: str = '127.0.0.1,localhost'
    STORE_DB_HOST: str = '127.0.0.1'
    STORE_DB_PORT: int = 5432
    STORE_DB_USER: str
    STORE_DB_PASSWORD: str
    STORE_DB_NAME: str = 'store_db'
    STORE_ADMIN_USERNAME: str  # used when we request
    STORE_ADMIN_PASSWORD: str  # store app via API from warehouse
    STORE_APP_PORT: str = '8001'
    STORE_APP_NAME: str = 'store'
    WAREHOUSE_DJANGO_SECRET_KEY: str
    WAREHOUSE_ALLOWED_HOSTS: str = '127.0.0.1,localhost'
    WAREHOUSE_DB_HOST: str = '127.0.0.1'
    WAREHOUSE_DB_PORT: int = 5433
    WAREHOUSE_DB_USER: str
    WAREHOUSE_DB_PASSWORD: str
    WAREHOUSE_DB_NAME: str = 'warehouse_db'
    WAREHOUSE_ADMIN_USERNAME: str  # used when we request
    WAREHOUSE_ADMIN_PASSWORD: str  # warehouse app via API from store
    WAREHOUSE_APP_PORT: str = '8002'
    WAREHOUSE_APP_NAME: str = 'warehouse'

    class Config:
        env_file='.env'
        env_file_encoding='utf-8'


project_settings = Settings()

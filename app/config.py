from pydantic_settings import BaseSettings
import os 

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.dev')

settings = Settings()
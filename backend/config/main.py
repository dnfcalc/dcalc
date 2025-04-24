from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG_MODE: bool = True
    WORKERS: int = 1
    PORT:int = 27173
    REDIS_URL: str = 'redis://localhost:6379/1'

    class Config:
        env_file = ('config/.env', 'config/.env.dev', 'config/.env.prod')


config = Config()

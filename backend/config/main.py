import os
import sys

from pydantic_settings import BaseSettings, SettingsConfigDict

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass

class Config(BaseSettings):
    DEBUG_MODE: bool = True
    WORKERS: int = 1
    PORT:int = 27173
    MCPPORT: int = 27174
    REDIS_URL: str = 'redis://localhost:6379/1'
    COLG_TOKEN: str = ''
    HELPER_TOKEN: str = ''
    HELPER_ID: str = ''

    model_config = SettingsConfigDict(
        env_file=('config/.env', 'config/.env.dev', 'config/.env.prod')
    )


config = Config()

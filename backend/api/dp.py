from typing import Annotated
from redis import Redis
from sqlalchemy.orm import Session
from fastapi import Depends

from database.connect import get_db,get_redis

SessionDep = Annotated[Session, Depends(get_db)]
RedisDep = Annotated[Redis, Depends(get_redis)]

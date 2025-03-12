from typing import Annotated, Optional
from redis import Redis
from sqlalchemy.orm import Session
from fastapi import Depends, Header

from api.core.exception import ResponseException
from database.connect import get_db,get_redis
from api.core.Auth import AlterState, deleteToken, readToken

SessionDep = Annotated[Session, Depends(get_db)]
RedisDep = Annotated[Redis, Depends(get_redis)]


def authorize(redis:RedisDep, access_token: Optional[str] = Header(None)):
    if access_token is not None:
        info = readToken(access_token, redis)
        return info
    else:
        raise ResponseException('登录过期或无效Token，请刷新后重试')


def unauthorize(redis:RedisDep, access_token: Optional[str] = Header(None)):
    if access_token is not None:
        return deleteToken(access_token, redis)

AltersDep = Annotated[AlterState, Depends(authorize)]
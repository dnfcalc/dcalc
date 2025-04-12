import time
from typing import Annotated, Optional
from redis import Redis
from sqlalchemy.orm import Session
from fastapi import Depends, Header

from api.core.exception import ResponseException
from core.character.adventure import get_adv_info
from database.connect import get_db, get_redis
from api.core.Auth import AlterState
import base64
import json
from api.core.Redis import get_redis_info

SessionDep = Annotated[Session, Depends(get_db)]
RedisDep = Annotated[Redis, Depends(get_redis)]


def alterToken(redis:RedisDep,alter_token: Optional[str] = Header(None)):
    if alter_token is not None:
        try:
            decoded_bytes = base64.b64decode(alter_token)
            decoded_str = decoded_bytes.decode('utf-8')
            alter = json.loads(decoded_str)
            # 6小时过期
            if (int(time.time() * 1000) - alter['time']) / (60 * 60 * 1000) > 6:
                raise ResponseException('登录过期或无效Token，请刷新后重试')
            alterData = get_redis_info(redis, f'dcalc:adventure:{alter['alter']}', lambda : get_adv_info(alter['alter']))
            return AlterState(alterData["class"], alter_token, {}, alter['equVersion'], alter['time'])
        except (base64.binascii.Error, json.JSONDecodeError):
            raise ResponseException('登录过期或无效Token，请刷新后重试')
    else:
        raise ResponseException('登录过期或无效Token，请刷新后重试')
    pass


AltersDep = Annotated[AlterState, Depends(alterToken)]

# def authorize(redis:RedisDep, access_token: Optional[str] = Header(None)):
#     if access_token is not None:
#         info = readToken(access_token, redis)
#         return info
#     else:
#         raise ResponseException('登录过期或无效Token，请刷新后重试')


# def unauthorize(redis:RedisDep, access_token: Optional[str] = Header(None)):
#     if access_token is not None:
#         return deleteToken(access_token, redis)

# TokenDep = Annotated[AlterState, Depends(authorize)]

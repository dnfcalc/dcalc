import base64
import hmac
import json
import time
from typing import Optional
from core.basic.character import Character
from fastapi import  Header, Request
from api.core.exception import ResponseException


class AlterState:
    def __init__(self, alter: str, token: str, charcater: Character, equVersion: str):
        self.alter = alter
        self.token = token
        self.origin = alter.split('.')[-1]
        self.character = charcater
        self.equVersion = equVersion

    def to_dict(self):
        return self.__dict__


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict2obj(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    d = Dict()
    for k, v in dictObj.items():
        d[k] = dict2obj(v)
    return d


async def createToken(alter: str, equVersion: str, expire=86400 / 24 * 2, redis=None, env=''):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode('utf-8')
    sha1_tshex_str = hmac.new(alter.encode('utf-8'), ts_byte, 'sha1').hexdigest()
    token = sha1_tshex_str
    token = base64.urlsafe_b64encode(token.encode('utf-8')).decode('utf-8')
    # character = createCharacter(alter)
    character = {}
    await redis.set(f'token:{token}', json.dumps(AlterState(alter, token, character, equVersion).to_dict()), int(expire))
    return token


async def readToken(token: str, redis, env) -> AlterState:
    info = None
    try:
        info = dict2obj(json.loads(await redis.get(f'token:{token}')))
    except Exception:
        ResponseException('登录过期或无效Token，请刷新后重试')
    if info is None:
        raise ResponseException('登录过期或无效Token，请刷新后重试')
    return info


def deleteToken(token, redis, env):
    redis.expire(token, 0)
    return token


async def authorize(request: Request, access_token: Optional[str] = Header(None)):
    if access_token is not None:
        info = await readToken(access_token, request.app.state.redis, request.app.state.env)
        return info
    else:
        raise ResponseException('登录过期或无效Token，请刷新后重试')


def unauthorize(request: Request, access_token: Optional[str] = Header(None)):
    if access_token is not None:
        return deleteToken(access_token, request.app.state.redis, request.app.state.env)


async def uid(request: Request, access_uid: Optional[str] = Header(None)):
    try:
        return int(access_uid)
    except Exception:
        return -1


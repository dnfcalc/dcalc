import base64
import hmac
import json
import time
from typing import Optional
from core.character.adventure import get_adv_info
from core.basic.character import Character
from fastapi import  Header, Request
from api.core.exception import ResponseException


class AlterState:
    def __init__(self, value: str, token: str, charcater: Character, equVersion: str,time: int):
        self.value = value
        try:
            self.alter = get_adv_info(value)["class"]
        except Exception:
            raise ResponseException(f'无效的职业{value}')
        self.token = token
        self.origin = self.alter.split('.')[-1]
        self.character = charcater
        self.equVersion = equVersion
        self.time = time

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


def createToken(value: str, equVersion: str, redis = None, expire=86400 / 24 * 2)->str:
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode('utf-8')
    sha1_tshex_str = hmac.new(value.encode('utf-8'), ts_byte, 'sha1').hexdigest()
    token = sha1_tshex_str
    token = base64.urlsafe_b64encode(token.encode('utf-8')).decode('utf-8')
    # character = createCharacter(alter)
    character = {}
    redis.set(f'token:{token}', json.dumps(AlterState(value, token, character, equVersion).to_dict()), int(expire))
    return token


def readToken(token: str, redis) -> AlterState:
    info = None
    try:
        info = dict2obj(json.loads(redis.get(f'token:{token}')))
    except Exception as ex:
        print(ex)
        ResponseException('登录过期或无效Token，请刷新后重试')
    if info is None:
        raise ResponseException('登录过期或无效Token，请刷新后重试')
    return info


def deleteToken(token, redis, env):
    redis.expire(token, 0)
    return token


def uid(access_uid: Optional[str] = Header(None)):
    try:
        return int(access_uid)
    except Exception:
        return -1


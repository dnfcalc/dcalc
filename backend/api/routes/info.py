from api.core.Auth import createToken
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter,Request
from api.core.Response import Return, response
from api.core.Redis import get_redis_info
from api.dp import RedisDep,AltersDep
from core.basic.character import createCharacter

router = APIRouter()

register_gzip_request(router)


@router.get('/adventure')
async def get_adventure_info(request: Request,redis:RedisDep):
    def get_adventure():
        with open('./dataFiles/adventure-info.json', encoding='utf-8') as fp:
            return json.load(fp)
    adventure_info = get_redis_info(redis, 'dcalc:adventure', get_adventure)

    return response(data=adventure_info)

@router.get("/token/get/{alter}")
async def getToken(redis:RedisDep,
    alter: str, request: Request, version: str = None, equVersion: str = "0"
):
    token = createToken(alter, equVersion, redis)
    return response(data=token)

@router.get("/character")
async def get_character_info(
    request: Request, state: AltersDep ,redis:RedisDep
):
    character = createCharacter(state.alter, state.equVersion)
    def get_character():
        return character.getInfo()
    info = get_redis_info(redis, f"dcalc:character:{state.alter}", get_character)
    return response(data=info)


from api.core.Auth import createToken
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter,Request
from api.core.Response import Return, response
from api.core.Redis import get_redis_info
from api.dp import RedisDep

router = APIRouter()

register_gzip_request(router)


@router.get('/adventure')
async def get_adventure_info(request: Request,redis:RedisDep):
    def get_adventure():
        with open('./dataFiles/adventure-info.json', encoding='utf-8') as fp:
            return json.load(fp)
    adventure_info = get_redis_info(redis, 'dcalc:adventure', get_adventure)

    return response(data=adventure_info)

@router.get('/equipment/list')
async def get_equipment_list(request: Request,redis:RedisDep):
    def get_equipment_list():
        with open('./dataFiles/equipment-list.json', encoding='utf-8') as fp:
            return json.load(fp)
    equipment_list = get_redis_info(redis, 'dcalc:equipment', get_equipment_list)

    return response(data=equipment_list)

@router.get("/token/get/{alter}", response_model=Return[str])
async def getToken(
    alter: str, request: Request, version: str = None, equVersion: str = ""
):
    if version is not None and version != "default" and version != "":
        alter = version + "." + alter
    token = createToken(
        alter, equVersion, redis=request.app.state.redis, env=request.app.state.env
    )
    return response(data=token)

from api.core.Auth import createToken
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter, Body,Request
from api.core.Response import Return, response
from api.core.Redis import get_redis_info
from api.dp import RedisDep,AltersDep
from core.basic.character import createCharacter

router = APIRouter()

register_gzip_request(router)

@router.post('/calc')
async def calc(request: Request,state:AltersDep,config=Body(None)):
  character = createCharacter(state.alter, state.equVersion)
  return response(data=character.calc(config))

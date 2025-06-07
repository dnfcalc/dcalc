from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter,Request
from api.core.Response import  response
from api.core.Redis import get_redis_info
from api.dp import RedisDep

router = APIRouter()

register_gzip_request(router)

@router.get('/{job}/{jobGrow}/{skill}')
async def get_cn_skll_info(redis:RedisDep,job:str, jobGrow:str, skill:str, request: Request):
    """
    Get the OpenAPI information for a specific job and skill.
    """
    key = f"openapi:{job}:{jobGrow}:{skill}"

    def get_skill_info():
        # This function should retrieve the skill info based on job and jobGrow
        # For now, we return a placeholder dictionary
        with open(f"./openapi/{job}/{jobGrow}/cn/skillDetail/{skill}.json", encoding="utf-8") as f:
            skill_data = json.load(f)
        return skill_data

    skill_info = get_redis_info(redis, key, get_skill_info)

    return response(data=skill_info)

import re
from api.core.Auth import createToken
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter,Request
from api.core.Response import Return, response
from api.core.Redis import get_redis_info
from api.dp import RedisDep,AltersDep
from core.character.adventure import get_adv_list
from core.basic.character import createCharacter

router = APIRouter()

register_gzip_request(router)

def replace_placeholders(template):
    # 匹配 <int>、<float>、<float1>、<float2> 等
    pattern = re.compile(r'<(int|float\d*)>')
    idx = 0

    def repl(match):
        nonlocal idx
        idx += 1
        return f'{{value{idx}}}'

    return pattern.sub(repl, template)



@router.get('/adventure')
async def get_adventure_info(request: Request,redis:RedisDep):
    adventure_info = get_redis_info(redis, 'dcalc:adventure', get_adv_list)

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
    info = get_redis_info(redis, f"dcalc:character:{state.alter}:{state.equVersion}", get_character)
    # info = character.getInfo()
    return response(data=info)

@router.get("/skill/{skillId}/{level}")
async def get_skill_info(
    state: AltersDep, skillId: str, level: int, redis: RedisDep
):
    """
    获取技能信息
    """
    alter = state.alter
    jobId = alter.split(".")[1]
    jobGrowId = alter.split(".")[2]
    skill_info = {}
    key = f'openapi:{jobId}:{jobGrowId}:{skillId}'
    try:
        def get_skill_info():
            # This function should retrieve the skill info based on job and jobGrow
            # For now, we return a placeholder dictionary
            with open(f'./openapi/data/{jobId}/{jobGrowId}/cn/skillDetail/{skillId}.json', encoding='utf-8') as f:
                skill_data = json.load(f)
            if 'levelInfo' in skill_data and 'optionDesc' in skill_data['levelInfo'] and skill_data['levelInfo']['optionDesc'] is not None:
                skill_data['levelInfo']['optionDesc'] = replace_placeholders(skill_data['levelInfo']['optionDesc'])
            return skill_data

        skill_info = get_redis_info(redis, key, get_skill_info)
        if level is not None:
            level = max(0, min(level, skill_info.get('maxLevel', 0)))
            if 'levelInfo' in skill_info and 'rows' in skill_info['levelInfo']:
                detail = list(filter(lambda x: x['level'] == level, skill_info['levelInfo']['rows']))
                if detail and len(detail) > 0:
                    skill_info['levelInfo'].update(detail[0])
                    skill_info['levelInfo']['detail'] = skill_info['levelInfo'].get('optionDesc', '')
                    for key in skill_info['levelInfo']['optionValue'].keys():
                        skill_info['levelInfo']['detail'] = skill_info['levelInfo']['detail'].replace(f'{{{key}}}', str(skill_info['levelInfo']['optionValue'][key]))
                    del skill_info['levelInfo']['rows']
                    skill_info['attribute'] = {}
                    skill_info['attribute'].update(skill_info['levelInfo'])
                    del skill_info['levelInfo']
    except FileNotFoundError:
        return response(code=404, message=f'技能信息未找到: {jobId} {jobGrowId} {skillId}', data=None)
    return response(data=skill_info)

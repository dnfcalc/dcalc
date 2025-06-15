from fastapi.params import Param
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter, Path
from api.core.Response import response
from api.core.Redis import get_redis_info
from api.dp import RedisDep
import re
from typing import Annotated

from api.types.open import SkillDetailResponse, SkillsListResponse

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


@router.get('/skills/', operation_id='skillsList')
async def get_skills_list(redis: RedisDep, skillName: Annotated[str, Param(..., description='技能名称，支持模糊查询')])->SkillsListResponse:
    """
    根据技能名称，获取对应的技能列表信息
    """
    key = 'openapi:skills'

    def get_skills():
        # This function should retrieve the skills list from the data source
        # For now, we return a placeholder list
        with open('./openapi/data/skills.json', encoding='utf-8') as f:
            skills_data = json.load(f)
        return skills_data

    skills_list = get_redis_info(redis, key, get_skills)
    data = list(filter(lambda x: re.sub(r'\s+', '', skillName) in re.sub(r'\s+', '', x['skillName']), skills_list)) if skillName else skills_list
    return response(data=data)


@router.get('/{jobId}/{jobGrowId}/skills/', operation_id='skillsByJob')
async def get_cn_skills_by_job(redis: RedisDep, jobId: Annotated[str, Path(..., description='职业')], jobGrowId: Annotated[str, Path(..., description='转职')]) -> SkillsListResponse:
    """
    获取职业技能列表
    """
    key = f'openapi:{jobId}:{jobGrowId}:skills'

    def get_skills_by_job():
        # This function should retrieve the skills by job and jobGrow
        # For now, we return a placeholder list
        with open(f'./openapi/data/{jobId}/{jobGrowId}/cn/skill_tree.json', encoding='utf-8') as f:
            skills_data = json.load(f)
        return skills_data

    skills_list = get_redis_info(redis, key, get_skills_by_job)
    return response(data=skills_list)

@router.get('/{jobId}/{jobGrowId}/{skillId}/', operation_id='skillDetail')
async def get_cn_skill_info(redis: RedisDep, jobId: Annotated[str, Path(..., description='职业')], jobGrowId: Annotated[str, Path(..., description='转职')], skillId: Annotated[str, Path(..., description='技能')], level: Annotated[int, Param(..., description='技能等级')] = None) -> SkillDetailResponse:
    """
    获取技能详细信息
    """
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

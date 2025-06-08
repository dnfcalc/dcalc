from fastapi.params import Param
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter, Path
from api.core.Response import response,Return
from api.core.Redis import get_redis_info
from api.dp import RedisDep
import re
from typing import TYPE_CHECKING, Annotated

from api.types.open import SkillInfo,SkillDetail
if TYPE_CHECKING:
    from api.core.Response import Return

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


@router.get('/skills/')
async def get_skills_list(redis: RedisDep,skillName: str) -> Return[list[SkillInfo]]:
    """
    根据技能名称，获取对应的技能列表信息
    """
    key = 'openapi:skills'
    def get_skills():
        # This function should retrieve the skills list from the data source
        # For now, we return a placeholder list
        with open('./openapi/skills.json', encoding='utf-8') as f:
            skills_data = json.load(f)
        return skills_data
    skills_list = get_redis_info(redis, key, get_skills)
    data = list(
        filter(
            lambda x: re.sub(r'\s+', '', skillName) == re.sub(r'\s+', '', x["skillName"]),
            skills_list
        )
    ) if skillName else skills_list
    return response(data=data)


@router.get('/{job}/{jobGrow}/{skillId}/')
async def get_cn_skll_info(redis: RedisDep,
                           job: Annotated[str,Path(..., title='职业')],
                           jobGrow: Annotated[str,Path(..., title='转职')],
                           skillId: Annotated[str,Path(..., title='技能')],
                           level: Annotated[int,Param(..., title="技能等级")]
                           ) -> Return[SkillDetail]:
    """
    获取技能详细信息
    """
    skill_info = {}
    key = f'openapi:{job}:{jobGrow}:{skillId}'
    try:
        def get_skill_info():
            # This function should retrieve the skill info based on job and jobGrow
            # For now, we return a placeholder dictionary
            with open(f'./openapi/{job}/{jobGrow}/cn/skillDetail/{skillId}.json', encoding='utf-8') as f:
                skill_data = json.load(f)
            if "levelInfo" in skill_data and "optionDesc" in skill_data["levelInfo"] and skill_data["levelInfo"]["optionDesc"] is not None:
                skill_data["levelInfo"]["optionDesc"] = replace_placeholders(skill_data["levelInfo"]["optionDesc"])
            return skill_data

        skill_info = get_redis_info(redis, key, get_skill_info)
        if level is not None:
            level = max(0,min(level,skill_info.get("maxLevel",0)))
            if "levelInfo" in skill_info and "rows" in skill_info["levelInfo"]:
                detail = list(filter(lambda x: x["level"] == level, skill_info["levelInfo"]["rows"]))
                if detail and len(detail) > 0:
                    skill_info["levelInfo"].update(detail[0])
                    skill_info["levelInfo"]["detail"] = skill_info["levelInfo"].get("optionDesc", "")
                    for key in skill_info["levelInfo"]["optionValue"].keys():
                        skill_info["levelInfo"]["detail"] = skill_info["levelInfo"]["detail"].replace(f"{{{key}}}",str(skill_info["levelInfo"]["optionValue"][key]))
                    del skill_info["levelInfo"]["rows"]
                    skill_info["attribute"] = {}
                    skill_info["attribute"].update(skill_info["levelInfo"])
                    del skill_info["levelInfo"]
    except FileNotFoundError:
        return response(code=404, message=f"技能信息未找到: {job} {jobGrow} {skillId}", data=None)
    return response(data=skill_info)

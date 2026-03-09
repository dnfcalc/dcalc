from fastapi.params import Param
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter, Path, Query, Depends
from api.core.Response import response
from api.core.Redis import get_redis_info
from api.dp import RedisDep
import re
from typing import Annotated

from api.types.open import (
    JobInfoResponse,
    SkillDataSummaryResponse,
    SkillDetailResponse,
    SkillsListResponse,
    SearchSkillResponse,
)
import os

from core.character.adventure import get_adv_list

router = APIRouter()

register_gzip_request(router)


def replace_placeholders(template):
    # 匹配 <int>、<float>、<float1>、<float2> 等
    pattern = re.compile(r"<(int|float\d*)>")
    idx = 0

    def repl(match):
        nonlocal idx
        idx += 1
        return f"{{value{idx}}}"

    return pattern.sub(repl, template)


@router.get("/skills/", operation_id="skillsList", response_model=SearchSkillResponse)
async def get_skills_list(
    redis: RedisDep,
    skillName: Annotated[str, Param(..., description="技能名称，支持模糊查询")] = None,
) -> SearchSkillResponse:
    """
    根据技能名称，获取对应的技能列表信息
    """
    key = "openapi:skills"

    def get_skills():
        # This function should retrieve the skills list from the data source
        # For now, we return a placeholder list
        with open("./openapi/data/skills.json", encoding="utf-8") as f:
            skills_data = json.load(f)
        return skills_data

    skills_list = get_redis_info(redis, key, get_skills)
    data = (
        list(
            filter(
                lambda x: re.sub(r"\s+", "", skillName)
                in re.sub(r"\s+", "", x["skillName"]),
                skills_list,
            )
        )
        if skillName
        else skills_list
    )
    return response(data=data)


@router.get("/jobInfo/", operation_id="jobsInfo", response_model=JobInfoResponse)
async def get_jobs_info(
    redis: RedisDep,
    jobName: Annotated[str, Query(..., description="职业名称，支持模糊查询")]  = None,
) -> JobInfoResponse:
    """
    根据职业名称，获取对应的职业转职信息
    """
    adventure_info = get_redis_info(redis, "dcalc:adventure", get_adv_list)
    result = []
    for adv in adventure_info:
        matched_children = [
            child
            for child in adv.get("children", [])
            if jobName in child.get("title", "") or jobName in child.get("name", "")
        ]
        if matched_children:
            parent = {k: v for k, v in adv.items() if k != "children"}
            for child in matched_children:
                entry = parent.copy()
                entry["child"] = child
                result.append(
                    {
                        "jobId": entry.get("name", ""),
                        "jobName": entry.get("title", ""),
                        "jobGrowId": child.get("name", ""),
                        "jobGrowName": child.get("title", ""),
                    }
                )
    return response(data=result)


@router.get("/{jobId}/{jobGrowId}/skills/", operation_id="skillsByJob",response_model=SkillsListResponse)
async def get_cn_skills_by_job(
    redis: RedisDep,
    jobId: Annotated[str, Path(..., description="职业")],
    jobGrowId: Annotated[str, Path(..., description="转职")],
) -> SkillsListResponse:
    """
    获取职业技能列表
    """
    key = f"openapi:{jobId}:{jobGrowId}:skills"

    def get_skills_by_job():
        # This function should retrieve the skills by job and jobGrow
        # For now, we return a placeholder list
        with open(
            f"./openapi/data/{jobId}/{jobGrowId}/cn/skill_tree.json", encoding="utf-8"
        ) as f:
            skills_data = json.load(f)
        return skills_data

    skills_list = get_redis_info(redis, key, get_skills_by_job)
    return response(data=skills_list)


@router.get("/{jobId}/{jobGrowId}/{skillId}/", operation_id="skillDetail", response_model=SkillDetailResponse)
async def get_cn_skill_info(
    redis: RedisDep,
    jobId: Annotated[str, Path(..., description="职业")],
    jobGrowId: Annotated[str, Path(..., description="转职")],
    skillId: Annotated[str, Path(..., description="技能")],
    level: Annotated[int, Param(..., description="技能等级")] = None,
) -> SkillDetailResponse:
    """
    获取技能详细信息
    """
    skill_info = {}
    key = f"openapi:{jobId}:{jobGrowId}:{skillId}"
    try:

        def get_skill_info():
            # This function should retrieve the skill info based on job and jobGrow
            # For now, we return a placeholder dictionary
            with open(
                f"./openapi/data/{jobId}/{jobGrowId}/cn/skillDetail/{skillId}.json",
                encoding="utf-8",
            ) as f:
                skill_data = json.load(f)
            if (
                "levelInfo" in skill_data
                and "optionDesc" in skill_data["levelInfo"]
                and skill_data["levelInfo"]["optionDesc"] is not None
            ):
                skill_data["levelInfo"]["optionDesc"] = replace_placeholders(
                    skill_data["levelInfo"]["optionDesc"]
                )
            return skill_data

        skill_info = get_redis_info(redis, key, get_skill_info)
        if level is not None:
            level = max(0, min(level, skill_info.get("maxLevel", 0)))
            if "levelInfo" in skill_info and "rows" in skill_info["levelInfo"]:
                detail = list(
                    filter(
                        lambda x: x["level"] == level, skill_info["levelInfo"]["rows"]
                    )
                )
                if detail and len(detail) > 0:
                    skill_info["levelInfo"].update(detail[0])
                    skill_info["levelInfo"]["detail"] = skill_info["levelInfo"].get(
                        "optionDesc", ""
                    )
                    for key in skill_info["levelInfo"]["optionValue"].keys():
                        skill_info["levelInfo"]["detail"] = skill_info["levelInfo"][
                            "detail"
                        ].replace(
                            f"{{{key}}}",
                            str(skill_info["levelInfo"]["optionValue"][key]),
                        )
                    del skill_info["levelInfo"]["rows"]
                    skill_info["attribute"] = {}
                    skill_info["attribute"].update(skill_info["levelInfo"])
                    del skill_info["levelInfo"]
    except FileNotFoundError:
        return response(
            code=404,
            message=f"技能信息未找到: {jobId} {jobGrowId} {skillId}",
            data=None,
        )
    return response(data=skill_info)


@router.get("/skillData/summary/", operation_id="skillDataSummary",response_model=SkillDataSummaryResponse)
async def get_skill_data_summary(
    redis: RedisDep,
    job: Annotated[str, Param(..., description="职业")],
    skills: Annotated[
        str,
        Param(
            ...,
            description="技能列表字符串,逗号拼接技能名称,不传递或者传递为空时,查询所有",
        ),
    ] = "",
    weapons: Annotated[
        str,
        Param(
            ...,
            description="武器类型列表字符串,逗号拼接武器类型名称,不传递或者传递为空时,查询所有",
        ),
    ] = "",
) -> SkillDataSummaryResponse:
    """
    获取技能数据汇总信息
    """
    key = f"openapi:skillData:summary:{job}"
    data = []
    skills = skills.split(",") if skills else []
    weapons = weapons.split(",") if weapons else []
    try:
        def get_skill_data_summary():
            # This function should retrieve the skill data summary based on job
            # For now, we return a placeholder dictionary
            summary_dir = "./openapi/summary/"
            json_files = [f for f in os.listdir(summary_dir) if f.endswith(".json")]
            res = []
            for i in json_files:
                if job in i:
                    with open(os.path.join(summary_dir, i), encoding="utf-8") as f:
                        skill_data = json.load(f)
                    weapon = i.split("_")[-1].replace(".json", "")
                    res.append(
                        {"weapon": weapon if weapon else "通用", "skills": skill_data}
                    )
            return res

        job_summary = get_redis_info(redis, key, get_skill_data_summary)
        for item in job_summary:
            if len(weapons) == 0 or item["weapon"] in weapons:
                items = list(filter(lambda x: x["技能名称"] in skills, item["skills"])) if len(skills) > 0 else item["skills"]
                for skill in items:
                    skill["武器类型"] = item["weapon"]
                data.extend(items or [])
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return response(data=[])
    return response(data=data)

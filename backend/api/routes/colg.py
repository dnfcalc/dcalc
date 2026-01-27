from api.types.colg import HistoryGold, RealTimeGold
from fastapi.params import Param
from api.core.Gzip import register_gzip_request
import json
from fastapi import APIRouter, Path, Query
from api.core.Response import response
from api.core.Redis import get_redis_info
from api.dp import RedisDep
from typing import Annotated
import requests
from config.main import config
from datetime import datetime, timezone, timedelta
from api.core.Response import Return as Response

router = APIRouter()

register_gzip_request(router)

regionMap = {
    '跨1': 1,
    '跨2': 2,
    '跨3A': 3,
    '跨3B': 4,
    '跨4': 5,
    '跨5': 6,
    '跨6': 7,
    '跨7': 8,
}

url = 'https://poservice.colg.cn/api/v1/trend/getCoinTrendDataKol'

payload = {'token': config.COLG_TOKEN, 'area': 0, 'time_type': 'other', 'start_time': '2026-01-06', 'end_time': '2026-01-06'}


def get_date_str(timestamp: int) -> str:
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    beijing_time = utc_time + timedelta(hours=8)
    return beijing_time.strftime('%Y-%m-%d %H:%M:%S')


@router.get('/gold/realtime/', operation_id='realTimeGold')
async def get_real_time_gold(redis: RedisDep) -> Response[list[RealTimeGold]]:
    """
    返回所有跨区的实时金价信息
    """
    key = 'openapi:colg:real_time_gold'
    try:

        def get_gold_data():
            res = []
            for region_name, region_id in regionMap.items():
                payload['area'] = region_id
                payload['start_time'] = datetime.now().strftime('%Y-%m-%d')
                payload['end_time'] = datetime.now().strftime('%Y-%m-%d')
                response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
                response.raise_for_status()
                resp = response.json().get('data', {})
                res.append({'updataTime': get_date_str(resp['x'][-1]), 'region': region_name, 'goldPrice': resp['y'][-1]})
            return res
    except Exception as e:
        # print(f"File not found: {e}")
        return response(data=[])
    # 设置半小时过期一次
    data = get_redis_info(redis, key, get_gold_data, 30 * 60)
    return response(data=data)


@router.get('/gold/history/', operation_id='historyGold')
async def get_history_gold(region: Annotated[int, Query(..., description='跨区id')], timeRange: Annotated[int, Query(..., description='时间跨度天数')] = 7) -> Response[HistoryGold] | Response[None]:
    """
    获取历史金价数据

    Args:
        region (int): 跨区id，必填参数，跨区id对应的映射如下
            {
                '跨1': 1,
                '跨2': 2,
                '跨3A': 3,
                '跨3B': 4,
                '跨4': 5,
                '跨5': 6,
                '跨6': 7,
                '跨7': 8,
            }
        timeRange (int, optional): 时间跨度天数，默认为7天

    Returns:
        Response[HistoryGold]: 返回历史金价数据的响应对象

    Raises:
        无显式异常，但会在跨区ID无效时返回404错误码

    Note:
        - region参数必须在regionMap的值范围内
        - timeRange参数是可选的，使用默认值7表示最近7天的数据
    """
    print(region, timeRange)
    if region not in regionMap.values():
        return response(
            code=404,
            message='跨区ID无效',
            data=None,
        )
    region_name = [k for k, v in regionMap.items() if v == region][0]
    end_date = datetime.now()
    start_date = end_date - timedelta(days=timeRange - 1)
    payload['area'] = region
    payload['start_time'] = start_date.strftime('%Y-%m-%d')
    payload['end_time'] = end_date.strftime('%Y-%m-%d')
    data = []
    echartsData = {}
    try:
        req = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
        req.raise_for_status()
        resp = req.json().get('data', {})
        for i in range(len(resp['x'])):
            data.append(
                {
                    'date': get_date_str(resp['x'][i]).split(' ')[0],
                    'avg': resp['y'][i],
                    'zero': resp['y1'][i],
                }
            )
    except Exception as e:
        return response(data=None)
    echartsData = {
        'title': {'text': f'DNF{region_name}近{timeRange}天金币价格趋势分析', 'left': 'center'},
        'toolbox': {'feature': {'saveAsImage': {}, 'dataView': {'readOnly': True}, 'magicType': {'type': ['line', 'bar']}}},
        'tooltip': {'trigger': 'axis', 'axisPointer': {'type': 'cross', 'label': {'backgroundColor': '#6a7985'}}},
        'legend': {'data': ['平均金价', '12时金价'], 'bottom': 0},
        'xAxis': {'type': 'category', 'name': '日期', 'boundaryGap': False, 'data': [item['date'] for item in data]},
        'yAxis': {'type': 'value', 'name': '价格 (万金币/1人民币)', 'min': (min([item['avg'] for item in data] + [item['zero'] for item in data]) // 5 ) * 5, 'max': (max([item['avg'] for item in data] + [item['zero'] for item in data]) // 5 ) * 5 + 5, 'axisLabel': {'formatter': '{value} 万金币'}},
        'series': [
            {'name': '平均金价', 'type': 'line', 'smooth': True, 'data': [item['avg'] for item in data], 'markPoint': {'data': [{'type': 'max', 'name': '最大值'}, {'type': 'min', 'name': '最小值'}]}},
            {'name': '12时金价', 'type': 'line', 'smooth': True, 'data': [item['zero'] for item in data], 'markLine': {'data': [{'type': 'average', 'name': '平均值'}]}},
        ],
    }
    return response(data={'region': region_name, 'data': data, 'echartsData': echartsData})

# Google Analytics 4 上报脚本
import platform
import uuid
import requests

# from log import logger


def get_cid():
    return "{}-{}".format(platform.node(), uuid.getnode())


# note: 查看数据地址 https://analytics.google.com/analytics/web/#/
# note: 当发现上报失败时，可以将打印的post body复制到 https://ga-dev-tools.web.app/ga4/event-builder/ 进行校验，看是否缺了参数，或者有参数不符合格式
# note: 参数文档 https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=gtag#payload_query_parameters
GA_API_BASE_URL = "https://www.google-analytics.com/mp/collect"
# GA_API_BASE_URL = "https://www.google-analytics.com/debug/mp/collect"
GA_API_SECRET = "XMAI1cjPQbqz9zoONwudOA"
GA_MEASUREMENT_ID = "G-Y0WSE6LW2Z"

GA_API_URL = f"{GA_API_BASE_URL}?measurement_id={GA_MEASUREMENT_ID}&api_secret={GA_API_SECRET}"

headers = {
    "user-agent": "dcalc",
}


def track_event(category: str, event_name: str):
    try:
        event_name = event_name.replace("/", "_")
        json_data = {
            "client_id": get_cid(),
            "user_id": get_cid(),
            "events": [
                {
                    "name": category,
                    "params": {
                        "engagement_time_msec": "1000",
                        "session_id": get_cid(),
                        "event_name": event_name,
                    },
                }
            ],
        }
        res = requests.post(GA_API_URL, json=json_data,
                            headers=headers, timeout=10)

    # 打印日志，方便调试
    # debug_msg = f"request info: body = {res.request.body!r}"
    # logFunc = logger.debug
    # if "debug" in GA_API_BASE_URL:
    #     debug_msg += f" res = {res.text}"
    #     logFunc = logger.warning
    # logFunc(debug_msg)
    except Exception as ex:
        print(ex)
        pass


if __name__ == "__main__":
    track_event("test_category", "test_event/name_1")
    track_event("test_category", "test_event_name_2")

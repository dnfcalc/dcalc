from __future__ import annotations
# Google Analytics 上报脚本
from urllib.parse import quote_plus
import requests
import platform
import uuid
from core.store import store

# note: 查看数据地址 https://analytics.google.com/analytics/web/#/
# note: 当发现上报失败时，可以将打印的post body复制到 https://ga-dev-tools.web.app/hit-builder/ 进行校验，看是否缺了参数，或者有参数不符合格式
# note: 参数文档 https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters
GA_API_URL = "https://www.google-analytics.com/collect"
GA_TRACKING_ID = "UA-212229431-2"

headers = {
    "user-agent": "dcalc",
}

def is_windows() -> bool:
    return platform.system() == "Windows"


def get_cid():
    return "{}-{}".format(platform.node(), uuid.getnode())


common_data = {
    "v": "1",  # API Version.
    "tid": GA_TRACKING_ID,  # Tracking ID / Property ID.
    "cid": get_cid(),  # Anonymous Client Identifier. Ideally, this should be a UUID that is associated with particular user, device, or browser instance.
    "ua": "djc_helper",
    "an": "dcalc",
    "av": store.get("version"),
    "ds": "dcalc",
    "sr": "1920x1080",
}

GA_REPORT_TYPE_EVENT = "event"
GA_REPORT_TYPE_PAGE_VIEW = "page_view"


def track_event(category: str, action: str, label=None, value=0, ga_misc_params: dict | None = None):
    try:
        if ga_misc_params  is None:
            ga_misc_params = {}

        data = {
            **common_data,
            "t": "event",  # Event hit type.
            "ec": category,  # Event category.
            "ea": action,  # Event action.
            "el": label,  # Event label.
            "ev": value,  # Event value, must be an integer
            **ga_misc_params,  # 透传的一些额外参数
        }

        res = requests.post(GA_API_URL, data=data, headers=headers, timeout=10)
    except Exception:
        pass


def track_page(page: str, ga_misc_params: dict | None = None):
    try:
        if ga_misc_params  is None:
            ga_misc_params = {}

        page = quote_plus(page)
        data = {
            **common_data,
            "t": "pageview",  # Event hit type.
            "dh": "djc-helper.com",  # Document hostname.
            "dp": page,  # Page.
            "dt": "",  # Title.
            **ga_misc_params,  # 透传的一些额外参数
        }

        res = requests.post(GA_API_URL, data=data, timeout=10)
    except Exception:
        pass


if __name__ == "__main__":
    # track_event("example", "test")
    track_page("/example/test_quote")

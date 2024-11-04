import os
import sys
import threading
from typing import Any

import utils.analysis.ga4 as ga4
import utils.analysis.ga as ga

def async_call(cb, *args, **params):
    threading.Thread(target=cb, args=args, kwargs=params, daemon=True).start()

def increase_counter(
    name: Any = "",
    report_to_google_analytics=True,
    ga_type=ga.GA_REPORT_TYPE_EVENT,
    ga_category="",
    ga_misc_params=None,
):

    name = str(name)

    if name == "":
        raise AssertionError("increase_counter name not set")

    def _cb():
        if report_to_google_analytics:
            increase_counter_sync_google_analytics(name, ga_type, ga_category, ga_misc_params)

    async_call(_cb)

def increase_counter_sync_google_analytics(name: str, ga_type: str, ga_category: str, ga_misc_params: dict):
    try:
    #  上报谷歌分析（v3和v4同时上报）
        if ga_type == ga.GA_REPORT_TYPE_EVENT:
            if ga_category == "":
                # 如果ga_category为空，则尝试从name中解析，假设name中以/分隔的第一个部分作为ga_category
                parts = name.split("/", 1)
                if len(parts) == 2:
                    ga_category, name = parts
                else:
                    ga_category = "counter"
            ga.track_event(ga_category, name, ga_misc_params)
            ga4.track_event(ga_category, name)
        elif ga_type == ga.GA_REPORT_TYPE_PAGE_VIEW:
            ga.track_page(name, ga_misc_params)
            ga4.track_event("page_view", name)
        else:
            pass
    except Exception as ex:
        print(ex)

def test():
    os.system("PAUSE")

if __name__ == "__main__":
    test()

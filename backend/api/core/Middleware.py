from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        # allow_origins = ["http://127.0.0.1:25252"],
        # allow_origin_regex='https?://(127.0.0.1|localhost|.*.skycity.top|.*.dnftools.com):?.*',  # 改成用正则就行了
        # 改成用正则就行了
        allow_origin_regex='https?://(127.0.0.1|localhost|.*.dnftools.com|.*.dcalc.cn|.*.seicing.com):?.*',
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

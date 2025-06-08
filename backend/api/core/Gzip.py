import gzip
from fastapi import Request, APIRouter, FastAPI
from fastapi.responses import Response
from collections.abc import Callable
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.routing import APIRoute


class GzipRequest(Request):
    async def body(self) -> bytes:
        if not hasattr(self, '_body'):
            body = await super().body()
            if 'gzip' in self.headers.getlist('Content-Encoding'):
                body = gzip.decompress(body)
                if 'application/json;charset=UTF-8' in self.headers.getlist('Content-Type'):
                    body = body.decode()
                    pass
            self._body = body
        return self._body


class GzipRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request = GzipRequest(request.scope, request.receive)
            return await original_route_handler(request)

        return custom_route_handler


def register_gzip_request(router: APIRouter):
    router.route_class = GzipRoute
    pass


def register_gzip_response(app: FastAPI):
    app.add_middleware(GZipMiddleware)
    pass

def gzip_zip(content):
    bytes_com = gzip.compress(str(content).encode('utf-8'))
    # base64_data = base64.b64encode(bytes_com)
    # back = base64_data.decode()
    return bytes_com


def gzip_unzip(content):
    if content:
        # base64_data = base64.b64decode(content)
        bytes_decom = gzip.decompress(content)
        str_unzip = bytes_decom.decode()
        return str_unzip
    else:
        return None

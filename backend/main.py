from config.main import config
from api.main import api_router
from fastapi import FastAPI
from multiprocessing import freeze_support
from api.core import Exceptions,Middleware,Gzip
from fastapi_mcp import FastApiMCP
import uvicorn

application = FastAPI(docs_url='/doc', redoc_url=None)
application.add_exception_handler(Exception, Exceptions.all_exception_handler)
Middleware.register_cors(application)
Gzip.register_gzip_response(application)
application.include_router(api_router)

mcp = FastApiMCP(application,name="dcalc-mcp",description="Dcalc MCP Service",include_operations=["skillsList", "skillDetail"])
mcp.mount()

if __name__ == '__main__':
    freeze_support()

    def on_startup():
        return print("Application starting...")

    uvicorn.run(app = "main:application", host='127.0.0.1', port=config.PORT, workers=config.WORKERS,reload=False)



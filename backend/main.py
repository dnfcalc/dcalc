from config.main import config
from api.main import api_router
from fastapi import FastAPI
from multiprocessing import freeze_support
from api.core import Exceptions,Middleware,Gzip
import uvicorn

application = FastAPI(docs_url='/doc', redoc_url=None)
application.add_exception_handler(Exception, Exceptions.all_exception_handler)
Middleware.register_cors(application)
Gzip.register_gzip_response(application)
application.include_router(api_router)


if __name__ == '__main__':
    freeze_support()

    def on_startup():
        return print("Application starting...")

    uvicorn.run(app = "main:application", host='0.0.0.0', port=config.PORT, workers=config.WORKERS,reload=False)



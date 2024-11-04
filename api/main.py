# encoding:utf-8
# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/
import uvicorn
from multiprocessing import freeze_support
from routers.config import config

if __name__ == '__main__':

    freeze_support()

    uvicorn.run(
        **config
    )
    # print(os.getppid())

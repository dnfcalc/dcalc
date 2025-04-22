from datetime import datetime
import logging
import traceback
from fastapi import Request, status
from fastapi.responses import JSONResponse
# from fastapi import Request, status

from api.core.exception import ResponseException

logFormatter = logging.Formatter(
    """
[start]
%(asctime)s
<%(name)s>
%(message)s
[end]
"""
)


async def all_exception_handler(request: Request, ex: Exception):
    # api = str(request.url).split("api/")[1]
    info = ''
    if not isinstance(ex, ResponseException):
        info = traceback.format_exc(limit=-1).strip().split('\n')[1:]
        info[0] = info[0].split('\\')[-1].replace('"', ':').replace(',', '')
        info = '\r'.join(info)
        if request.client.host != '127.0.0.1':
            from fastapi.logger import logger
            logger.setLevel(logging.ERROR)
            logger.name = 'dcalc'
            log_directory = 'logs'
            import os

            if not os.path.exists('./logs'):
                os.makedirs('./logs')
            time_str = datetime.now().strftime('%Y_%m_%d')
            fileHandler = logging.FileHandler(f'{log_directory}/{logger.name,}_{time_str}.log', encoding='utf-8')
            fileHandler.setFormatter(logFormatter)
            fileHandler.setLevel(logging.ERROR)
            logger.addHandler(fileHandler)
            try:
                import pathlib
                pathlib.Path(log_directory).mkdir(parents=True, exist_ok=True)
            except PermissionError:
                print('创建日志目录logs失败，请确认是否限制了基础的运行权限')
            logFunc = logger.error
            logFunc(info)
            info = '服务器内部错误'
            fileHandler.close()
    else:
        info = ex.args[0]
    # traceback.print_last(sys.exc_info())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        # 一定要加
        headers={'Access-Control-Allow-Origin': '*'},
        content={
            'code': 500,
            'message': info,
            # f"api:{api} \n \r{info}",
            'data': [],
        },
    )

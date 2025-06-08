import base64
import json
from typing import Generic, TypeVar
from pydantic import Field
from pydantic.generics import GenericModel
import gzip  # 导入 gzip 模块
from io import BytesIO  # 从 io 模块导入 BytesIO 类

T = TypeVar('T')

class Return(GenericModel, Generic[T]):
    code: int = Field(..., description='响应状态码')
    """响应状态码"""
    message: str = Field(..., description='响应消息')
    """响应消息"""
    data: T = Field(..., description='响应数据')
    """响应数据"""

# 定义一个函数，将字符串压缩为 gzip 格式，并进行 base64 编码后返回结果
def gzip_str(to_gzip: str) -> str:
    out = BytesIO()  # 创建一个 BytesIO 对象
    with gzip.GzipFile(fileobj=out, mode='w') as f:  # 使用 gzip 对象进行数据压缩
        f.write(to_gzip.encode())  # 将待压缩的字符串写入 gzip 对象中
    return base64.b64encode(out.getvalue()).decode()  # 对压缩后的数据使用 base64 编码并返回结果


def response(*, code=200, data: list | dict | str, message='Success', zip=False)-> Return:
    if zip:
        import gzip
        data = base64.b64encode(gzip.compress(json.dumps(data).encode()))
    return Return(code=code, message=message, data=data)


def success(data=None, msg=''):
    """成功返回格式"""
    return response(200, msg, data)


def fail(code=-1, msg='', data=None):
    """失败返回格式"""
    return response(code, msg, data)

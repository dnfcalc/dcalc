from numbers import Number


def is_number(num_str):
    """
    判断数据是否为一个数字

    :param num_str: 字符串对象
    :return:
    """
    """
    判断数据是否为一个数字

    :param num_str: 字符串对象
    :return: 布尔值   True 是一个数字   False  不是一个数字   None  本就是数值类型
    """
    # 防止非字段类型类型输入报错
    if isinstance(num_str, Number):
        return None
    elif not isinstance(num_str, str):
        return False

    if num_str.isdigit():
        return True
    # 对Float类型的数字进行判断
    if num_str.count('.') == 1:
        num_str_list = num_str.split('.')
        left = num_str_list[0]
        right = num_str_list[1]
        if left.startswith('-') and left.count('-') == 1 and right.isdigit():
            _left = left.split('-')[1]
            if _left.isdigit():
                return True
        elif left.isdigit() and right.isdigit():
            return True
    # 负数判断
    elif num_str.startswith('-'):
        _left = num_str.split('-')[1]
        if _left.isdigit():
            return True
    return False


def str_to_num(value, default=0, num_type=float):
    """
    将字符串类型转化为数据类型

    :param value: 需要转化的值，不一定需要是字符串类型
    :param default: 设置转换失败返回数值，默认原值
    :param num_type: 设置转换成的数据类型
    :return:
    """
    num_flag = is_number(value)
    if num_flag:
        return num_type(value)
    elif num_flag is None:
        return num_type(value)
    return value if default is None else default

registry = {}

def register(func):
    registry[func.__name__] = func
    return func

def execture(name):
    if name in registry:
        return registry[name]
    else:
        print(f"Function {name} not found in registry.")
        return None

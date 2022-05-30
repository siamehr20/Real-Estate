def check_access(func):
    def wrapper(obj, *args, **kwargs):
        if obj.has_access():
            # print('Has Access ')
            return func(obj)
        raise Exception('Agent has No Access...! ')

    return wrapper

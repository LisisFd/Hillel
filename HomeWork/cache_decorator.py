def do_cache(func):
    """
    :return: Update cache
    """
    cache = dict()

    def wrapper(*args):
        """
            Wrapper checks for the presence of values ​​in the cache,
            and adds a new one if there is none.
            Maxsize cache - 3.
        :return: function execution result
        """
        if args in cache.keys():
            return cache.get(args)
        elif len(cache.keys()) == 3:
          cache.pop(list(cache.keys())[0])
        cache[args] = func(*args)
        return func(*args)
    return wrapper


@do_cache
def get_value(a, b):
    """
    :param a: Int num
    :param b: Int num
    :return: a to the power b
    """
    return a ** b


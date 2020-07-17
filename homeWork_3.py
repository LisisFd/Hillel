import os


def get_log(func):
    def wrapper(dir):
        result = func(dir)
        for elem in result:
            if '.log' in elem:
                with open(f'{dir}/{elem}', 'r') as f:
                    print(f.read())
        return result

    return wrapper


@get_log
def get_file(dir):
    files = os.listdir(dir)
    return files


print(get_file('my_dir'))

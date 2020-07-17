

def decorator_file(func):
    def wrapper(file):
        list_words = func(file).split()
        print(f'File name : {file}\nWord count: {len(list_words)}')
        func(file)
        # Ничего не возвращает, так-как, сказано что функция должена печатать 
    return wrapper


@decorator_file
def file_read(file):
    with open(file, 'r') as copy_file:
        reader = copy_file.read()  # шоб красиво было :3
        print(reader)  # print - потому что четко написано что функция должна "печатать"
        return reader


file_read('file.txt')
def three_biggest_int(input_list):
    biggest_ints = list()
    input_list = list(set(input_list))
    for num in input_list:
        biggest_ints.append(max(input_list))
        input_list.remove(max(input_list))
        if len(biggest_ints) == 3: break
    return biggest_ints


def lowest_int_index(input_list):
    biggest_ints = list()
    input_list = list(set(input_list))
    lowest_int_index = input_list.index(min(input_list))
    print(lowest_int_index) # print Потому что, в условии задачи, четко написано: "Вывести".
    return lowest_int_index


def reversed_list(input_list):
    input_list.reverse()
    print(input_list)


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    common_keys = list()
    for keys1 in dict1:
        for keys2 in dict2:
            if keys1 == keys2:
                common_keys.append(keys1)
    return common_keys


def sort_by_age(student_list):
    result_dict = {'Kiev': list(), 'Dnepr': list(), 'Lviv': list()}
    for elem in student_list:
        for key in result_dict:
            if elem['city'] == key:
                result_dict[key].append(elem)
        elem.pop('city')
    return result_dict
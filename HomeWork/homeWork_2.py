def sort_by_age(student_list=None):
    """
        Groups students by key value City, and sorted by key value Age
    :param student_list:  list of dicts with where are each of them has info about student
    :return: sorted dict
    """
    if not student_list:
        student_list = [{'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
                        {'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
                        {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
                        {'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
                        {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
                        {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}]

    result_dict = {student.get('city'): list() for student in student_list}
    for city in result_dict.keys():
        for student in student_list:
            if city == student.get('city'):
                student.pop('city')
                result_dict[city].append(student)
        result_dict[city] = sorted(result_dict.get(city),
                                   key=lambda student_elem: student_elem['age'])
    return result_dict


def three_biggest_int(input_list):
    """
    :param input_list: list int numbers
    :return: list with three max elem in input list
    """
    input_list = list(set(input_list))
    input_list.sort(reverse=True)
    biggest_ints = input_list[:3]
    return biggest_ints


def lowest_int_index(input_list):
    """
        Print minimal element index
    :param input_list: list int numbers
    :return: None
    """
    input_list = list(set(input_list))
    lowest_index = input_list.index(min(input_list))
    print(lowest_index)


def find_common_keys(dict1, dict2):
    """
    :param dict1: some dict
    :param dict2: another dict
    :return: list of keys that are in each dictionary
    """
    common_keys = list(
        set(dict1.keys()).intersection(set(dict2.keys())))
    return common_keys

def catalog_finder(url_list):
    """
    :return: list with url who have catalog page
    """
    result_list = []
    for url in url_list:
        if '/catalog/' in url:
            result_list.append(url)
    return result_list


def get_str_center(input_str):
    """

    :param input_str: some string
    :return: 2 or 3 characters in the center of the line
    """
    start_slide = int(len(input_str) / 2)
    if len(input_str) % 2 == 0:
        output_str = input_str[start_slide - 1:start_slide+1]
    else:
        output_str = input_str[round(start_slide)-1:start_slide+2]
    return output_str



def count_symbols(input_str):
    """

    :param input_str: some string
    :return: dict where key are lettters and value their number in string
    """

    output_dict = dict()
    for letter in input_str:
        output_dict.update({letter: output_dict.get(letter, 0) + 1})
    return output_dict


def mix_strings(str1, str2):
    """
    :param str1: some string
    :param str2: another string
    :return: string where str2 in str1
    """

    middle_str = round(len(str1)/2) if len(str1) % 2 else int(len(str1)/2)
    result_str = f"{str1[:middle_str]}{str2}{str1[middle_str:]}"
    return result_str


def even_int_generator():
    """
    :return: list with evem numbers
    """
    even_int_list = [num for num in range(1,101) if not num % 2]
    return even_int_list


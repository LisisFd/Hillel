def catalog_finder(url_list):
    result_list = []
    for url in url_list:
        if '/catalog/' in url:
            result_list.append(url)
        else:
            continue
    return result_list


def get_str_center(input_str):
    start_slide = int(len(input_str) / 2)
    if len(input_str)%2 == 0:
        output_str = input_str[start_slide - 1:start_slide+1]
    else:
        output_str = input_str[round(start_slide)-1:start_slide+2]
    return output_str



def count_symbols(input_str):
    output_dict = dict()
    for letter in input_str:
        if letter in output_dict: continue
        else:
            output_dict.update({letter: input_str.count(letter)})
    return output_dict


def mix_strings(str1, str2):
    middle_str = int(len(str1)/2) if len(str1) % 2 == 0 else round(len(str1)/2)
    result_str = str1[:middle_str] + str2 + str1[middle_str:]
    return result_str


def even_int_generator():
    even_int_list = []
    for num in range(1, 101):
        if num % 2 == 0:
            even_int_list.append(num)
        else:
            continue
    return even_int_list
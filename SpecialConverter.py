import Changer       #Файл с предыдущими функция перевода числе из разных систем счисления
from textwrap import wrap

eight_four_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                           '7': '0111', '8': '1000', '9': '1001', '10': '1010', '11': '1011', '12': '1100', '13': ''}

four_two_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '1000', '5': '1001', '6': '1010',
                         '7': '1011', '8': '1110', '9': '1111'}

five_four_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '1000', '6': '1001',
                          '7': '1010', '8': '1011', '9': '1100'}


def bin_to_gray_code_changer(bin: str):
    bin_arr = [x for x in bin]
    buff_arr = ['0']
    for iter in range(len(bin_arr) - 1):
        buff_arr.append(bin_arr[iter])




def dec_to_gray_code_changer(dec: int):
    pass


def dec_to_xs3__changer(dec: int):
    dec_str = str(dec)
    added_element = ''

    for iter in range(len(dec_str)):
        added_element += '3'
    dec_int = int(dec_str) + int(added_element)

    xs3_result = ''
    for item in str(dec_int):
        xs3_result += eight_four_two_one_dict[item]

    return xs3_result


def dec_to_five_four_two_one_bcd_changer(dec: int):
    dec_num = str(dec)

    five_four_two_one_result = ''
    for iter in dec_num:
        five_four_two_one_result += five_four_two_one_dict[iter]

    return five_four_two_one_result


def dec_to_four_two_two_one_bcd_changer(dec: int):
    dec_num = str(dec)

    four_two_two_one_result = ''
    for iter in dec_num:
        four_two_two_one_result += four_two_two_one_dict[iter]

    return four_two_two_one_result


def dec_to_eight_four_two_one_bcd_changer(dec: int):
    dec_num = str(dec)

    eight_four_two_one_result = ''
    for iter in dec_num:
        eight_four_two_one_result += eight_four_two_one_dict[iter]

    return eight_four_two_one_result


def special_converter_core_func(input_type: str, output_type: str, input_data: str):
    pass


print(dec_to_eight_four_two_one_bcd_changer(357))
print(dec_to_four_two_two_one_bcd_changer(357))
print(dec_to_xs3__changer(357))

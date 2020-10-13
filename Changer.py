from datetime import datetime
import time
import math
from textwrap import wrap

hexadecimal_bin_dictionary = {'0000': '0', '0001': '1', '0010': '2', '0011' : '3', '0100': '4', '0101': '5',
                              '0110': '6', '0111':'7', '1000':'8', '1001': '9', '1010': 'A', '1011': 'B',
                              '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

hexadecimal_decimal_dictionary = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                                  '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def positive_dec_to_bin_convert(decimal_number: float):
    integer_part = math.trunc(decimal_number)
    non_integer_part = decimal_number - integer_part

    integer_binary_part = ''
    while integer_part > 0:
        integer_binary_part = str(integer_part % 2) + integer_binary_part
        integer_part = integer_part // 2

    non_integer_binary_part = ''
    while non_integer_part > 0:
        non_integer_part = non_integer_part * 2
        buff = math.trunc(non_integer_part)
        if (buff > 0):
            non_integer_binary_part += str(1)
            non_integer_part -= 1
        else:
            non_integer_binary_part += str(0)
    binary_number = integer_binary_part + '.' + non_integer_binary_part
    return binary_number


def bin_to_hex_convert(binary_number: str):
    integer_binary_part = binary_number.split('.')[0]
    non_integer_binary_part = binary_number.split('.')[1]

    while len(integer_binary_part) % 4 != 0:
        integer_binary_part = '0' + integer_binary_part
    integer_part_split = wrap(integer_binary_part, 4)

    while len(non_integer_binary_part) % 4 != 0:
        non_integer_binary_part += '0'
    non_integer_part_split = wrap(non_integer_binary_part, 4)

    hexadecimal_num = ''
    for iter in integer_part_split:
        for bin_iter in hexadecimal_bin_dictionary:
            if iter == bin_iter:
                hexadecimal_num += hexadecimal_bin_dictionary[bin_iter]
    hexadecimal_num += '.'
    for iter in non_integer_part_split:
        for bin_iter in hexadecimal_bin_dictionary:
            if iter == bin_iter:
                hexadecimal_num += hexadecimal_bin_dictionary[bin_iter]
    return hexadecimal_num


def negative_hex_to_dec_convert(hexadecimal_num: str):
    return float('-' + positive_hex_to_dec_convert(hexadecimal_num))


def positive_hex_to_dec_convert(hexadecimal_num: str):
    hexadecimal_int = hexadecimal_num.split('.')[0]
    hexadecimal_non_int = hexadecimal_num.split('.')[1]

    int_part_exponent_index = len(hexadecimal_int) - 1
    # print(int_part_exponent_index)
    int_decimal_part = 0
    for iter in hexadecimal_int:
        for hex_iter in hexadecimal_decimal_dictionary:
            if iter == hex_iter:
                int_decimal_part += (16 ** int_part_exponent_index) * hexadecimal_decimal_dictionary[hex_iter]
                int_part_exponent_index -= 1

    none_int_part_exponent_index = len(hexadecimal_non_int)
    # print(none_int_part_exponent_index)
    # print('--------------------------------------')
    none_int_decimal_part = 0
    for iter in hexadecimal_non_int:
        for non_int_hex_iter in hexadecimal_decimal_dictionary:
            if iter == non_int_hex_iter:
                none_int_decimal_part += ((1 / (16 ** none_int_part_exponent_index))) * \
                                         hexadecimal_decimal_dictionary[non_int_hex_iter]
                # print(none_int_decimal_part)
                none_int_part_exponent_index -= 1

    decimal_number_result = int_decimal_part + none_int_decimal_part
    return str(decimal_number_result)


def negative_dec_to_bin(decimal_number):
    decimal_number = str(decimal_number)[1:]
    decimal_number = float(decimal_number)

    return positive_dec_to_bin_convert(decimal_number)


if __name__ == '__main__':
    start_time = datetime.now()
    data_file = open('dataTest.txt', 'r')
    data = data_file.read()
    data_list = data.split('\n')
    print(data_list)
    data_sum_coverted = 0
    data_sum = 0
    data_list = [x for x in data_list if x != '']
    for iter in data_list:
        if iter[0] == '-':
            data_sum_coverted += float(negative_hex_to_dec_convert((bin_to_hex_convert(negative_dec_to_bin(iter)))))
        else:
            data_sum_coverted += float(positive_hex_to_dec_convert(
                bin_to_hex_convert(positive_dec_to_bin_convert(float(iter)))))
    finish_time = datetime.now() - start_time
    for iter in data_list:
        data_sum += float(iter)

#print(data_sum)
    print(str(data_sum_coverted), str(positive_dec_to_bin_convert(data_sum_coverted)),
            str(bin_to_hex_convert(positive_dec_to_bin_convert(data_sum_coverted))),
            str(positive_hex_to_dec_convert(bin_to_hex_convert(positive_dec_to_bin_convert(data_sum_coverted)))))
    print(finish_time)


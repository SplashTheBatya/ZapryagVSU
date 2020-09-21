from datetime import datetime
import time
import math
from textwrap import wrap
import bitstring
from bitstring import Bits

hexadecimal_bin_dictionary = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
                              '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D',
                              '1110': 'E', '1111': 'F'}

hexadecimal_decimal_dictionary = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                                  '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def positive_dec_to_bin_convert(decimal_number: float):
    integer_part = math.trunc(decimal_number)
    non_integer_part = decimal_number - integer_part

    integer_binary_part = ''
    while integer_part > 0:
        integer_binary_part = str(integer_part % 2) + integer_binary_part
        integer_part = integer_part // 2
    while len(integer_binary_part) < 8:
        integer_binary_part = '0' + integer_binary_part

    non_integer_binary_part = ''
    while non_integer_part > 0:
        non_integer_part = non_integer_part * 2
        buff = math.trunc(non_integer_part)
        if buff > 0:
            non_integer_binary_part += str(1)
            non_integer_part -= 1
        else:
            non_integer_binary_part += str(0)
    binary_number = integer_binary_part + '.' + non_integer_binary_part
    return binary_number


def negative_dec_to_bin_convert(decimal_number: float):
    decimal_number = str(decimal_number)[1:]
    decimal_number = float(decimal_number)
    integer_part = math.trunc(decimal_number)
    non_integer_part = decimal_number - integer_part

    integer_binary_part = ''
    while integer_part > 0:
        integer_binary_part = str(integer_part % 2) + integer_binary_part
        integer_part = integer_part // 2
    while len(integer_binary_part) < 7:
        integer_binary_part = '0' + integer_binary_part

    integer_binary_part = integer_binary_part.replace('1', '2')
    integer_binary_part = integer_binary_part.replace('0', '1')
    integer_binary_part = integer_binary_part.replace('2', '0')

    integer_binary_part = [x for x in integer_binary_part]
    #print(integer_binary_part)
    integer_binary_part.reverse()
    #print(integer_binary_part)
    buff = 1
    for bin_array_iter in range(len(integer_binary_part)):
        if int(integer_binary_part[bin_array_iter]) + buff == 2:
            integer_binary_part[bin_array_iter] = '0'
            buff = 1
        else:
            integer_binary_part[bin_array_iter] = str(int(integer_binary_part[bin_array_iter]) + buff)
            buff = 0
    integer_binary_part.reverse()
    #print(integer_binary_part)
    string_buffer = ''
    for str_iter in range(len(integer_binary_part)):
        string_buffer += integer_binary_part[str_iter]

    integer_binary_part = string_buffer
    integer_binary_part = '1' + str(integer_binary_part)

    non_integer_binary_part = ''
    while non_integer_part > 0:
        non_integer_part = non_integer_part * 2
        buff = math.trunc(non_integer_part)
        if buff > 0:
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


def neg_hex_to_decimal_convert(hexadecimal_num: str):
    hexadecimal_int = hexadecimal_num.split('.')[0]
    hexadecimal_non_int = hexadecimal_num.split('.')[1]

    binary_2s_int_part = ''
    for iter_str in hexadecimal_int:
        for key_dict, data_dict in hexadecimal_bin_dictionary.items():
            if iter_str == data_dict:
                binary_2s_int_part += str(key_dict)

    binary_2s_non_int_part = ''
    for iter_str in hexadecimal_non_int:
        for key_dict, data_dict in hexadecimal_bin_dictionary.items():
            if iter_str == data_dict:
                binary_2s_non_int_part += str(key_dict)
    while binary_2s_non_int_part[-1] == '0':
        binary_2s_non_int_part = binary_2s_non_int_part[:-1]

    print(binary_2s_int_part + '.' + binary_2s_non_int_part)

    binary_2s_int_part = [x for x in binary_2s_int_part]
    binary_2s_int_part.reverse()

    buff = 1
    for bin_array_iter in range(len(binary_2s_int_part)-1):
        if int(binary_2s_int_part[bin_array_iter]) - buff < 0:
            binary_2s_int_part[bin_array_iter] = '1'
            buff = 1
        else:
            binary_2s_int_part[bin_array_iter] = str(int(binary_2s_int_part[bin_array_iter]) - buff)
            buff = 0
    binary_2s_int_part.reverse()
    #print(binary_2s_int_part)
    binary_int_part = ''
    for str_iter in range(len(binary_2s_int_part)):
        binary_int_part += binary_2s_int_part[str_iter]

    sign_indicator = binary_int_part[0:1]
    binary_int_part = binary_int_part[1:]
    binary_int_part = binary_int_part.replace('1', '2')
    binary_int_part = binary_int_part.replace('0', '1')
    binary_int_part = binary_int_part.replace('2', '0')
    binary_int_part = sign_indicator + binary_int_part

    binary_int_part = binary_int_part[1:]
    binary_int_part = [x for x in binary_int_part]
    binary_int_part.reverse()
    decimal_int_part = 0

    exponent = 0
    for dec_int_iter in binary_int_part:
        decimal_int_part += int(dec_int_iter) * (2**exponent)
        exponent += 1

    decimal_non_int_part = 0
    exponent = 1
    for dec_non_int_iter in binary_2s_non_int_part:
        decimal_non_int_part += float(dec_non_int_iter) * (1/2**exponent)
        exponent += 1

    decimal_number = decimal_int_part + decimal_non_int_part
    if sign_indicator == '1':
        decimal_number = float('-' + str(decimal_number))
    if sign_indicator == '0':
        pass
    return decimal_number


# def positive_bin_to_hex_convert(binary_number: str):
#     integer_binary_part = binary_number.split('.')[0]
#     non_integer_binary_part = binary_number.split('.')[1]
#
#     while len(integer_binary_part) % 4 != 0:
#         integer_binary_part = '0' + integer_binary_part
#     integer_part_split = wrap(integer_binary_part, 4)
#
#     while len(non_integer_binary_part) % 4 != 0:
#         non_integer_binary_part += '0'
#     non_integer_part_split = wrap(non_integer_binary_part, 4)
#
#     hexadecimal_num = ''
#     for iter in integer_part_split:
#         for bin_iter in hexadecimal_bin_dictionary:
#             if iter == bin_iter:
#                 hexadecimal_num += hexadecimal_bin_dictionary[bin_iter]
#     hexadecimal_num += '.'
#     for iter in non_integer_part_split:
#         for bin_iter in hexadecimal_bin_dictionary:
#             if iter == bin_iter:
#                 hexadecimal_num += hexadecimal_bin_dictionary[bin_iter]
#     return hexadecimal_num


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
                none_int_decimal_part += (1 / (16 ** none_int_part_exponent_index)) * \
                                         hexadecimal_decimal_dictionary[non_int_hex_iter]
                # print(none_int_decimal_part)
                none_int_part_exponent_index -= 1

    decimal_number_result = int_decimal_part + none_int_decimal_part
    return str(decimal_number_result)



# number_to_convert_pos = float(input('Input some + '))
number_to_convert_neg = float(input('Input some - '))
number_to_convert_pos = float(input('Input some + '))

# print(positive_dec_to_bin_convert(number_to_convert_pos))
print(negative_dec_to_bin_convert(number_to_convert_neg))
print(bin_to_hex_convert(negative_dec_to_bin_convert(number_to_convert_neg)))
print(neg_hex_to_decimal_convert(bin_to_hex_convert(negative_dec_to_bin_convert(number_to_convert_neg))))
print('----------------------------------')
print(positive_dec_to_bin_convert(number_to_convert_pos))
print(bin_to_hex_convert(positive_dec_to_bin_convert(number_to_convert_pos)))
print(positive_hex_to_dec_convert(bin_to_hex_convert(positive_dec_to_bin_convert(number_to_convert_pos))))


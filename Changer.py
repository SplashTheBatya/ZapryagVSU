from datetime import datetime
import time
import math
from textwrap import wrap

start_time = datetime.now()

print('Input decimal number: ')
decimal_number = float(input())
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
    if(buff > 0):
        non_integer_binary_part += str(1)
        non_integer_part -= 1
    else:
        non_integer_binary_part += str(0)
binary_number = integer_binary_part + '.' + non_integer_binary_part
print('Decimal number ',str(decimal_number),' is equals ',binary_number,' in binary')



hexadecimal_bin_dictionary = {'0000': '0', '0001': '1', '0010': '2', '0011' : '3', '0100': '4', '0101': '5', '0110': '6',
                          '0111':'7', '1000':'8', '1001': '9', '1010': 'A', '1011': 'B', '1100' : 'C', '1101': 'D',
                          '1110': 'E', '1111': 'F'}

hexadecimal_decimal_dictionary = {'0' : 0, '1' : 1, '2' : 2, '3': 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7,
                                  '8' : 8,'9': 9,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E' : 14, 'F': 15}

while len(integer_binary_part) % 4 != 0:
    integer_binary_part = '0' + integer_binary_part
integer_part_split = wrap(integer_binary_part, 4)

while len(non_integer_binary_part) % 4 != 0:
    non_integer_binary_part += '0'
non_integer_part_split = wrap(non_integer_binary_part, 4)

# print(integer_part_split)
# print(non_integer_part_split)


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

print('Decimal number ',decimal_number,'is equals ',hexadecimal_num, 'in hexadecimal')

hexadecimal_split = hexadecimal_num.split('.')
hexadecimal_int = hexadecimal_split[0]
hexadecimal_non_int = hexadecimal_split[1]
# print('--------------------------------------')
# print(hexadecimal_split)
# print(hexadecimal_int)
# print(hexadecimal_non_int)
# print('--------------------------------------')



int_part_exponent_index = len(hexadecimal_int) - 1
# print(int_part_exponent_index)
int_decimal_part = 0
for iter in hexadecimal_int:
    for hex_iter in hexadecimal_decimal_dictionary:
        if iter == hex_iter:
            int_decimal_part += (16**int_part_exponent_index) * hexadecimal_decimal_dictionary[hex_iter]
            int_part_exponent_index -= 1



none_int_part_exponent_index = len(hexadecimal_non_int)
# print(none_int_part_exponent_index)
# print('--------------------------------------')
none_int_decimal_part = 0
for iter in hexadecimal_non_int:
    for non_int_hex_iter in hexadecimal_decimal_dictionary:
        if iter == non_int_hex_iter:
            none_int_decimal_part += ((1 / (16**none_int_part_exponent_index))) *\
                                     hexadecimal_decimal_dictionary[non_int_hex_iter]
            # print(none_int_decimal_part)
            none_int_part_exponent_index -= 1

decimal_number_result = int_decimal_part + none_int_decimal_part
print(decimal_number_result)
print(datetime.now() - start_time)

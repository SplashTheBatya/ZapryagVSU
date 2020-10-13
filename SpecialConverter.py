import Changer  # Файл с предыдущими функция перевода числе из разных систем счисления
from textwrap import wrap

eight_four_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                           '7': '0111', '8': '1000', '9': '1001', '10': '1010', '11': '1011', '12': '1100', '13': ''}

four_two_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '1000', '5': '1001', '6': '1010',
                         '7': '1011', '8': '1110', '9': '1111'}

five_four_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '1000', '6': '1001',
                          '7': '1010', '8': '1011', '9': '1100'}


def bin_to_dec_changer(bin: str):
    exponent = len(bin) - 1
    dec_result = 0
    for iter in bin:
        dec_result += (2 ** exponent) * int(iter)
        exponent -= 1

    return str(dec_result)


def bin_to_gray_code_changer(bin: str):
    bin_arr = [x for x in bin]
    gray_result_arr = [bin_arr[0]]
    for bin_iter in range(1, len(bin_arr)):
        if int(bin_arr[bin_iter]) + int(bin_arr[bin_iter - 1]) == 2:
            gray_result_arr.append('1')
        else:
            gray_result_arr.append(str(int(bin_arr[bin_iter]) + int(bin_arr[bin_iter - 1])))

    gray_result = ''
    for iter in gray_result_arr:
        gray_result += iter
    return gray_result


def dec_to_gray_code_changer(dec: int):
    bin_num = Changer.positive_dec_to_bin_convert(dec)
    bin_arr = [x for x in bin_num]
    for iter in bin_arr:
        if iter == '.':
            bin_arr.remove(iter)
    bin_num = ''
    for iter in bin_arr:
        bin_num += iter

    while len(bin_num) % 4 != 0:
        bin_num = '0' + bin_num
    return bin_to_gray_code_changer(bin_num)


def dec_to_xs3_changer(dec: int):
    dec_str = str(dec)
    dec_str_list = [x for x in dec_str]
    dec_int_list = [int(item)+3 for item in dec_str_list]
    print(dec_int_list)
    xs3_result = ''
    for dec_list_iter in dec_str_list:
        buff = Changer.positive_dec_to_bin_convert(float(dec_list_iter))
        print(buff)
        buff_list = [x for x in buff]
        for buff_list_iter in buff_list:
            if buff_list_iter == '.':
                buff_list.remove(buff_list_iter)
        buff = ''
        for buf_iter in buff_list:
            buff += buf_iter
        while len(buff) % 4 != 0:
            buff = '0' + buff
        xs3_result += buff

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


def eight_four_two_one_bcd_to_dec_changer(bcd_efto: str):
    dec_result = ''

    bcd_efto_list = wrap(bcd_efto, 4)
    for iter in bcd_efto_list:
        for dec_iter, bcd_efto_iter in eight_four_two_one_dict.items():
            if iter == bcd_efto_iter:
                dec_result += dec_iter

    return dec_result


def four_two_two_one_bcd_to_dec_changer(bcd_ftto: str):
    dec_result = ''

    bcd_ftto_list = wrap(bcd_ftto, 4)
    for iter in bcd_ftto_list:
        for dec_iter, bcd_ftto_iter in four_two_two_one_dict.items():
            if iter == bcd_ftto_iter:
                dec_result += dec_iter

    return dec_result


def _five_four_two_one_bcd_to_dec_changer(bcd_ffto: str):
    dec_result = ''

    bcd_ffto_list = wrap(bcd_ffto, 4)
    for iter in bcd_ffto_list:
        for dec_iter, bcd_ffto_iter in five_four_two_one_dict.items():
            if iter == bcd_ffto_iter:
                dec_result += dec_iter

    return dec_result


def xs3_to_dec_changer(xs3_num: str):
    xs3_num_list = wrap(xs3_num, 4)
    binary_buff_list = []
    for iter in xs3_num_list:
        binary_buff_list.append(str((int(iter, 2) - int('0011', 2)))[0:2])

    return binary_buff_list


def gray_code_to_dec_changer(gray_num: str):
    pass


def special_converter_core_func(input_type: str, output_type: str, input_data: str):
    pass


#print(dec_to_eight_four_two_one_bcd_changer(357))
#print(dec_to_four_two_two_one_bcd_changer(357))
print(dec_to_xs3_changer(357))
#print(bin_to_gray_code_changer('0010'))
#print(dec_to_gray_code_changer(3))
#print(eight_four_two_one_bcd_to_dec_changer('001101010111'))
#print(bin_to_dec_changer('1011'))
#print(xs3_to_dec_changer(dec_to_xs3_changer(357)))

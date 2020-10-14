from textwrap import wrap

eight_four_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                           '7': '0111', '8': '1000', '9': '1001', '10': '1010', '11': '1011', '12': '1100', '13': ''}

four_two_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '1000', '5': '1001', '6': '1010',
                         '7': '1011', '8': '1110', '9': '1111'}

five_four_two_one_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '1000', '6': '1001',
                          '7': '1010', '8': '1011', '9': '1100'}


def dec_to_bin_changer(dec: str):
    dec = int(dec)
    binary_str = ''
    while dec > 0:
        binary_str = str(dec % 2) + binary_str
        dec = dec // 2
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str
    return binary_str


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
            gray_result_arr.append('0')
        else:
            gray_result_arr.append(str(int(bin_arr[bin_iter]) + int(bin_arr[bin_iter - 1])))

    gray_result = ''
    for iter in gray_result_arr:
        gray_result += iter
    return gray_result


def dec_to_gray_code_changer(dec: str):
    bin_num = dec_to_bin_changer(dec)
    bin_arr = [x for x in bin_num]
    bin_num = ''
    for iter in bin_arr:
        bin_num += iter
    while len(bin_num) % 4 != 0:
        bin_num = '0' + bin_num
    return bin_to_gray_code_changer(bin_num)


def dec_to_xs3_changer(dec: str):
    dec_str = str(dec)
    dec_str_list = [x for x in dec_str]
    dec_int_list = [int(item)+3 for item in dec_str_list]
    xs3_result = ''
    for dec_list_iter in dec_int_list:
        buff = dec_to_bin_changer(str(dec_list_iter))
        buff_list = [x for x in buff]
        buff = ''
        for buf_iter in buff_list:
            buff += buf_iter
        while len(buff) % 4 != 0:
            buff = '0' + buff
        xs3_result += buff

    return xs3_result


def dec_to_five_four_two_one_bcd_changer(dec: str):
    dec_num = str(dec)

    five_four_two_one_result = ''
    for iter in dec_num:
        five_four_two_one_result += five_four_two_one_dict[iter]

    return five_four_two_one_result


def dec_to_four_two_two_one_bcd_changer(dec: str):
    dec_num = str(dec)

    four_two_two_one_result = ''
    for iter in dec_num:
        four_two_two_one_result += four_two_two_one_dict[iter]

    return four_two_two_one_result


def dec_to_eight_four_two_one_bcd_changer(dec: str):
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


def five_four_two_one_bcd_to_dec_changer(bcd_ffto: str):
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

    dec_result = ''
    for iter in binary_buff_list:
        dec_result += iter

    return dec_result


def gray_code_to_dec_changer(gray_num: str):
    gray_arr = [x for x in gray_num]
    bin_num_arr = [gray_arr[0]]
    for iter in range(1, len(gray_arr)):
        if int(gray_arr[iter]) + int(bin_num_arr[iter - 1]) == 2:
            bin_num_arr.append('0')
        else:
            bin_num_arr.append(str(int(gray_arr[iter]) + int(bin_num_arr[iter - 1])))

    bin_res = ''
    for iter in bin_num_arr:
        bin_res += iter

    return bin_to_dec_changer(bin_res)


"""
Словарь соотнощений - аналог блока if else в функции-ядре
"""
command_dict = {
        ('dec', 'bin'): dec_to_bin_changer,
        ('dec', 'eight_four_two_one'): dec_to_eight_four_two_one_bcd_changer,
        ('dec', 'five_four_two_one'): dec_to_five_four_two_one_bcd_changer,
        ('dec', 'four_two_two_one'): dec_to_four_two_two_one_bcd_changer,
        ('dec', 'gray'): dec_to_gray_code_changer,
        ('dec', 'xs3'): dec_to_xs3_changer,
        ('bin', 'gray'): bin_to_gray_code_changer,
        ('bin', 'dec'): bin_to_dec_changer,
        ('bin', 'xs3'): lambda x: dec_to_xs3_changer(bin_to_dec_changer(x)),
        ('bin', 'eight_four_two_one'): lambda x: dec_to_eight_four_two_one_bcd_changer(bin_to_dec_changer(x)),
        ('bin', 'five_four_two_one'): lambda x: dec_to_five_four_two_one_bcd_changer(bin_to_dec_changer(x)),
        ('bin', 'four_two_two_one'): lambda x: dec_to_four_two_two_one_bcd_changer(bin_to_dec_changer(x)),
        ('xs3', 'bin'): lambda x: dec_to_bin_changer(xs3_to_dec_changer(x)),
        ('xs3', 'eight_four_two_one'): lambda x: dec_to_eight_four_two_one_bcd_changer(xs3_to_dec_changer(x)),
        ('xs3', 'five_four_two_one'): lambda x: dec_to_five_four_two_one_bcd_changer(xs3_to_dec_changer(x)),
        ('xs3', 'four_two_two_one'): lambda  x: dec_to_four_two_two_one_bcd_changer(xs3_to_dec_changer(x)),
        ('xs3', 'dec'): xs3_to_dec_changer,
        ('xs3', 'gray'): lambda x: dec_to_gray_code_changer(str(xs3_to_dec_changer(x))),
        ('eight_four_two_one', 'dec'): eight_four_two_one_bcd_to_dec_changer,
        ('eight_four_two_one', 'bin'):lambda x: dec_to_bin_changer(eight_four_two_one_bcd_to_dec_changer(x)),
        ('eight_four_two_one', 'xs3'): lambda x: dec_to_xs3_changer(eight_four_two_one_bcd_to_dec_changer(x)),
        ('eight_four_two_one', 'gray'): lambda x: dec_to_gray_code_changer(eight_four_two_one_bcd_to_dec_changer(x)),
        ('eight_four_two_one', 'five_four_two_one'):
                    lambda x: dec_to_five_four_two_one_bcd_changer(eight_four_two_one_bcd_to_dec_changer(x)),
        ('eight_four_two_one', 'four_two_two_one'):
                    lambda x: dec_to_four_two_two_one_bcd_changer(eight_four_two_one_bcd_to_dec_changer(x)),
        ('five_four_two_one', 'dec'): five_four_two_one_bcd_to_dec_changer,
        ('five_four_two_one', 'bin'): lambda x: dec_to_bin_changer(five_four_two_one_bcd_to_dec_changer(x)),
        ('five_four_two_one', 'gray'): lambda  x: dec_to_gray_code_changer(five_four_two_one_bcd_to_dec_changer(x)),
        ('five_four_two_one', 'xs3'): lambda x: dec_to_xs3_changer(five_four_two_one_bcd_to_dec_changer(x)),
        ('five_four_two_one', 'eight_four_two_one'):
                    lambda x: dec_to_eight_four_two_one_bcd_changer(five_four_two_one_bcd_to_dec_changer(x)),
        ('five_four_two_one', 'four_two_two_one'):
                    lambda x: dec_to_four_two_two_one_bcd_changer(five_four_two_one_bcd_to_dec_changer(x)),
        ('four_two_two_one', 'dec'): four_two_two_one_bcd_to_dec_changer,
        ('four_two_two_one', 'bin'): lambda x: dec_to_bin_changer(four_two_two_one_bcd_to_dec_changer(x)),
        ('four_two_two_one', 'xs3'): lambda x: dec_to_xs3_changer(four_two_two_one_bcd_to_dec_changer(x)),
        ('four_two_two_one', 'gray'): lambda x: dec_to_gray_code_changer(four_two_two_one_bcd_to_dec_changer(x)),
        ('four_two_two_one', 'eight_four_two_one'):
                    lambda x: dec_to_eight_four_two_one_bcd_changer(four_two_two_one_bcd_to_dec_changer(x)),
        ('four_two_two_one', 'five_four_two_one'):
                    lambda x: dec_to_five_four_two_one_bcd_changer(four_two_two_one_bcd_to_dec_changer(x)),
        ('gray', 'dec'): gray_code_to_dec_changer,
        ('gray', 'bin'): lambda x: dec_to_bin_changer(gray_code_to_dec_changer(x)),
        ('gray', 'xs3'): lambda x: dec_to_xs3_changer(gray_code_to_dec_changer(x)),
        ('gray', 'eight_four_two_one'):
                    lambda x: dec_to_eight_four_two_one_bcd_changer(gray_code_to_dec_changer(x)),
        ('gray', 'five_four_two_one'):
                    lambda x: dec_to_five_four_two_one_bcd_changer(gray_code_to_dec_changer(x)),
        ('gray', 'four_two_two_one'): lambda x: dec_to_four_two_two_one_bcd_changer(gray_code_to_dec_changer(x)),
        }


def special_converter_core_func(input_type: str, output_type: str, input_data: str):
    """
    Функция-ядро перевода чисел из систем счисления input_type обозначает систему счисления входного
    числа в формате строки
    output_type обозначает выходную систему счисления в формате строки
    input_data означает входные данные в системе input_type в формате строки
    """
    condition_list = (input_type, output_type)
    return command_dict[condition_list](input_data)


print(special_converter_core_func('xs3', 'gray', '0110'))
print(special_converter_core_func('dec', 'gray', '10'))
print(special_converter_core_func('bin', 'xs3', '0110'))

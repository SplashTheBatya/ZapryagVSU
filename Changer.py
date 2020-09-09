from datetime import datetime
import time
import math

start_time = datetime.now()

print('Input decimal number: ')
decimal_number = float(input())
print(decimal_number)
integer_part = math.trunc(decimal_number)
non_integer_part = decimal_number - integer_part
#print('non_integer_part  ' + str(non_integer_part))


integer_binary_part = ''
while integer_part > 0:
    integer_binary_part = str(integer_part % 2) + integer_binary_part
    #print(integer_binary_part)
    integer_part = integer_part // 2

non_integer_binary_part = ''
while non_integer_part > 0:
    non_integer_part = non_integer_part * 2
    #print(math.trunc(non_integer_part))
    buff = math.trunc(non_integer_part)
    if(buff > 0):
        non_integer_binary_part += str(1)
        non_integer_part -= 1
    else:
        non_integer_binary_part += str(0)


print('Decimal number '+ str(decimal_number) + ' is equals ' + integer_binary_part + '.' + non_integer_binary_part + ' in binary')
print(datetime.now() - start_time)








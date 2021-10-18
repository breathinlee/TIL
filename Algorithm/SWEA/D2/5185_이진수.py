"""
16진수 1자리는 2진수 4자리로 표시된다.
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
단, 2진수의 앞자리 0도 반드시 출력한다.
"""

def dec_to_binary(num):
    res = ''
    for i in range(3, -1, -1):
        if num & (1 << i):
            res += '1'
        else:
            res += '0'
    return res


def hex_to_binary(hex_value):
    dec_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if hex_value.isdigit():
        dec_value = int(hex_value)
    else:
        dec_value = dec_dict.get(hex_value)

    res = ''
    res += dec_to_binary(dec_value)
    return res

# def hex_to_binary(hex_value):
# if hex_value >= 9:
#   return ord(hex_value) - ord('0')
# else:
#   return ord(hex_value) - ord('A') + 10


T = int(input())
for tc in range(1, T+1):
    N, lst = map(int, input().split())    # N : 자리수 / lst : N자리 16진수
    binary_number = ''
    for w in lst:
        binary_number += hex_to_binary(w)

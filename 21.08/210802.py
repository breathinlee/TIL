# 1926. 간단한 369게임

"""
3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.

1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.
  1 2 3 4 5 6 7 8 9…
2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.  
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.

입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
"""

N = int(input())
game = [3, 6, 9]

for num in range(1, N+1):
    num1 = num // 10
    num2 = num % 10
    if num2 not in game and num1 not in game:
        print(num, end = ' ')
    else:    
        list1 = []
        if num1 in game and num2 in game:
            list1.append(num1)
            list1.append(num2)
            cnt = len(list1)
            print(''.join('-' * cnt), end = ' ')  
        elif num1 in game:
            print('-', end = ' ')
        else:
            print('-', end = ' ')
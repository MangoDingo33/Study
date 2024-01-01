from random import randint

def quiz(ans):
    if a == ran_num:
        print('정답')
        return 1
    elif a > ran_num:
        print('다운')
        return 0
    elif a < ran_num:
        print('업')
        return 0

ran_num = randint(1, 20)

for i in range(3):
    a = int(input('숫자를 입력하세요(0 ~ 20) : '))
    ans = quiz(a)
    if ans == 1:
        break
    
print()
if ans == 1:
    print('성공')
else:
    print('실패')
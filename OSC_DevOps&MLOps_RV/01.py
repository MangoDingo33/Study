print('안녕하세요')
q= ['취존', '솔까말', '케바케']
abb = {'취존': '취향 존중', '솔까말': '솔직히 까놓고 말해서', '케바케': '케이스 바이 케이스'}
point = 0

for i in q:
    a = input(f'{i}이(가) 어떤 문장의 줄임말인가요? : ').replace(' ', '')
    if a == abb[i].replace(' ', ''):
        print('정답')
        point += 1
    else:
        print('오답')
        
print(f'3개 퀴즈 중 {point}개 정답')

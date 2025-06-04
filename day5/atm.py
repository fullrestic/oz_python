# 잔액 초기화
balance = 1000

while True :
    num = input('사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ')

    # 1번 입금 기능 코드 
    if num == '1' :
        print('입금')
    # 4번 종료 기능 코드
    if num == '4' : 
        print('종료')
        break

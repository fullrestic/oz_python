# 잔액 초기화
balance = 1000

while True :
    num = input('사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ')

    # 1번 입금 기능 코드 
    if num == '1' :
        # 입금할 금액 입력
        deposit_amount = int(input('입금할 금액을 입력해주세요 : '))
        balance += deposit_amount
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
    
    # 2번 출금 기능 코드
    if num == '2' : 
        # 출금할 금액 입력
        withdraw_amount = int(input('출금할 금액을 입력해주세요 : '))

        # 잔액만큼만 빠져나가게 설정
        withdraw_amount = min(withdraw_amount, balance)
        balance -= withdraw_amount
        
        if not balance : print('잔액이 부족합니다.')
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')

    # 4번 종료 기능 코드
    if num == '4' : 
        print('종료')
        break

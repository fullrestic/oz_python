from typing import Callable

def validate_transaction(func : Callable) -> Callable :
    def wrapper(self, amount) :
        try :
            if amount <= 0 :
                raise NegativeAmountError()
            func(self, amount)
        except NegativeAmountError as e :
            print(e)
    return wrapper



class Transaction :
    def __init__(self, transaction_type : str, amount : int, balance : int) -> None :
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str :
        return f"거래 종류 : {self.transaction_type}\n거래 금액 : {self.amount}\n잔액 : {self.balance}\n"
    
    def to_tuple(self) -> tuple : 
        return (self.transaction_type, self.amount, self.balance)   
    


class Account :
    def __init__(self) -> None : 
        self.__balance = 0
        self.transactions = []

    @validate_transaction
    def deposit(self, amount : int) -> None :       
        self.__balance += amount
        self.transactions.append(Transaction('입금', amount, self.__balance))

    @validate_transaction
    def withdraw(self, amount : int) -> None :
        try :
            if amount > self.__balance :
                raise InsufficientFundsError(self.__balance)
        
            self.__balance -= amount
            self.transactions.append(Transaction('출금', amount, self.__balance))
        except InsufficientFundsError as e :
            print(e)

    def get_balance(self) -> int :
        return self.__balance
    
    def get_transaction(self) -> list :
        return self.transactions
    

    bank_name = ""

    @classmethod
    def get_bank_name(cls) -> str :
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name : str) -> None :
        cls.bank_name = name


    
class User :
    def __init__(self, username : str) -> None:
        self.username = username
        self.account = Account()



class BankingService :
    def __init__(self) -> None:
        self.users = []

    def add_user(self, username : str) -> None :
        self.users.append(User(username))

    def find_user(self, username : str) -> User :
        try : 
            for i in self.users :
                if i.username == username :
                    return i
                
            raise UserNotFoundError(username)
        except UserNotFoundError as e:
            print(e)
    
    def user_menu(self, username : str) -> None :
        while(True) :
            user = self.find_user(username)
            if not user : break
            
            function = input('\n사용하실 기능을 선택하세요(1.입금 2.출금 3.잔고 확인 4.거래 내역 5.종료) : ')

            if function in ('1', '입금') :
                try : 
                    amount = int(input('입금액을 입력해주세요 : '))
                    user.account.deposit(amount)
                except ValueError :
                    print('금액을 숫자로 입력해주세요.')
            elif function in ('2', '출금') :
                try : 
                    amount = int(input('출금액을 입력해주세요 : '))
                    user.account.withdraw(amount)
                except ValueError :
                    print('금액을 숫자로 입력해주세요.')
            elif function in ('3', '잔고 확인', '잔고확인') :
                print(f'현재 잔고는 {user.account.get_balance()}원 입니다.')
            elif function in ('4', '거래 내역', '거래내역') :
                transactions = user.account.get_transaction()
                if not transactions :
                    print('거래 내역이 없습니다.')
                else :
                    print()
                    for t in transactions :
                        print(t)
            elif function in ('5', '종료') :
                print('은행 시스템이 종료되었습니다.')
                break
            else :
                print('입력이 잘못되었습니다.')
            


class InsufficientFundsError(Exception) :
    def __init__(self, balance: int) -> None :
        super().__init__(f'잔액이 부족합니다. 현재 잔고 {balance}원')

class NegativeAmountError(Exception) :
    def __init__(self) -> None :
        super().__init__('금액은 양수여야 합니다.')
        
class UserNotFoundError(Exception) :
    def __init__(self, username: str) -> None :
        super().__init__(f'{username} 사용자를 찾을 수 없습니다.')




def main() -> None :
    bs = BankingService()

    while(True) :
        option = input('\n은행 서비스를 이용할 사용자를 선택해주세요.(1.사용자 추가 2.사용자 검색 3.취소) : ')
        
        if option in ('1', '사용자추가', '사용자 추가') :
            username = input('추가할 사용자 이름을 입력해주세요 : ')
            bs.add_user(username)
            bs.user_menu(username)
        elif option in ('2', '사용자검색', '사용자 검색') :
            username = input('검색할 사용자 이름을 입력해주세요 : ')
            bs.user_menu(username)
        elif option in ('3', '취소') :
            print('은헹 시스템 사용이 취소되었습니다.')
            break
        else :
            print('입력이 잘못되었습니다.')


main()
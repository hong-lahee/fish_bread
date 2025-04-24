class Bread_Shop:
    def __init__(self):
        self.stock = {"팥붕어빵" : 10, "슈크림붕어빵" : 8, "초코붕어빵" : 10}
        self.sales = {"팥붕어빵" : 0, "슈크림붕어빵" : 0, "초코붕어빵" : 0}
        self.price ={'팥붕어빵' : 500, '슈크림붕어빵' : 700,'초코붕어빵' : 800}
        self.pw = 'ghdfkgml'

    def order_bread(self):
        while True:
            bread_type = input('주문할 붕어빵맛을 입력해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가길 원하시면 뒤로가기를 입력하세요')
            if bread_type == "뒤로가기":
                print('뒤로 돌아갑니다')
                break
            if bread_type in self.stock:
                bread_count = int(input('구매할 갯수를 입력하세요'))
                if  self.stock[bread_type] >= bread_count:
                    self.stock[bread_type] -= bread_count
                    self. sales[bread_type] += bread_count
                    print(f'{bread_type}를 {bread_count}개 구매하셨습니다')
                else:
                    print(f'재고가 부족합니다 현재 {self.stock[bread_type]}개만 주문 가능합니다')
            else:
                print('잘못입력하셨습니다')

    def admin_mode(self):
        pwd = input('비밀번호를 입력하세요')
        if pwd not in self.pw:
            print('비밀번호가 틀리셨습니다')
            return
        while True:
            bread_type = (input('추가 할 붕어빵의 맛을 입력하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 뒤로가고 싶다면 뒤로가기를 입력하세요'))
            if bread_type == "뒤로가기":
                print('뒤로 돌아갑니다')
                break
            if bread_type in self.stock:
                bread_count = int(input('추가할 수량을 입력하세요'))
                self.stock[bread_type] += bread_count
                print(f'{bread_type}의 재고가 {bread_count}개 추가 되어 현재 {bread_type}의 재고는 {self.stock[bread_type]}개 입니다.')
            else:
                print('잘못입력하셨습니다')

    def purchase_sales(self):
            total_salse = sum(self.sales[key] * self.price[key] for key in self.sales)
            print(f'오늘의 총 매출은 {total_salse}원 입니다')
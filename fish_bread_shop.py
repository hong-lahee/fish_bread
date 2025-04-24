from fishbread_model import Bread_Shop

shop = Bread_Shop()

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
    if mode == "종료":
        shop.purchase_sales()
        print('시스템이 종료되었습니다')
        break
    elif mode == "주문":
        shop.order_bread()
    elif mode == "관리자":
        shop.admin_mode()
    else:
        print('잘못 입력 하셨습니다')

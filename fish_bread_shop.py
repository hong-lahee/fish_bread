#   조건, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들겁니다
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
    if mode == "종료":
        print('시스템이 종료되었습니다')
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
    else:
        print('잘못 입력 하셨습니다')

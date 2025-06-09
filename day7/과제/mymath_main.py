import mymath as mm

b, h = map(int, input('삼각형의 밑변과 높이를 입력하세요 : ').split())
print('삼각형의 넓이 : ', mm.tri_area(b, h))

r = int(input('원의 반지름을 입력하세요 : '))
print('원의 넓이 : ', mm.circ_area(r))

rb, rh = map(int, input('사각형의 밑변과 높이를 입력하세요 : ').split())
print('사각형의 넓이 : ', mm.rect_area(rb, rh))
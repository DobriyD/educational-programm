def IsPointInArea(x, y):
    in_circle = 2 * 2 >= abs(x + 1) * abs(x + 1) + abs(y - 1) * abs(y - 1)
    on_circle = 2 * 2 == abs(x + 1) * abs(x + 1) + abs(y - 1) * abs(y - 1)
    above_line1 = y >= 2 * x + 2
    above_line2 = y >= -x
    below_line1 = y <= 2 * x + 2
    below_line2 = y <= -x
    st1 = in_circle and above_line1 and above_line2
    st2 = (on_circle or not in_circle)
    st3 = below_line1 and below_line2
    return st1 or st2 and st3


x = float(input())
y = float(input())

if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')

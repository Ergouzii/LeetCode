x = 321
sign = 1
if x < 0:
    sign = -1
    x = -x

new_x = 0
while x != 0:
    pop = x % 10
    x = x // 10
    new_x = new_x * 10 + pop

new_x = sign * new_x

if new_x >= 2**31 or new_x < -2**31:
    print(0)

print(new_x)
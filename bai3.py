n = int(input('Nhập số nguyên n: '))
def so_chu_so(n):
    n = abs(n)
    if n == 0:
        return 1
    dem = 0
    while n > 0:
        dem += 1
        n = n//10
    return dem

def tong_so(n):
    n = abs(n)
    tong = 0
    while n > 0:
        tong += n%10
        n = n//10
    return tong

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
so_chu_so = so_chu_so(n)
tong_so = tong_so(n)
print(f'Số chữ số: {so_chu_so}, Tổng chữ số: {tong_so}, {n} {'là' if so_nguyen_to else 'không là'} số nguyên tố')

thang = int(input('Nhập số tháng: '))
nam = int(input('Nhập số năm: '))
def so_ngay(thang, nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28
ketqua = so_ngay(thang, nam)
if ketqua == None:
    print('Tháng Năm không hợp lệ')
else:
    print(f'Số ngay trong thang {thang} nam {nam} là: {ketqua}')
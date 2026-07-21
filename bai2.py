ngay = int(input('Nhập số ngày sinh: '))
thang = int(input('Nhập số tháng sinh: '))
def so_ngay_hop_le(ngay, thang):
    if thang < 1 or thang > 12:
        return False
    so_ngay_toi_da = [31,29,31,30,31,30,31,31,30,31,30,31]
    if ngay < 1 or ngay > so_ngay_toi_da[thang - 1]:
        return False
    return True

def cung_hoang_dao(ngay, thang):
    if (ngay >= 21 and thang == 3) or (ngay <= 19 and thang == 4):
        return 'Bạch Dương'
    elif (ngay >= 20 and thang == 4) or (ngay <= 20 and thang == 5):
        return 'Kim Ngưu'
    elif (ngay >= 21 and thang == 5) or (ngay <= 20 and thang == 6):
        return 'Song Tử'
    elif (ngay >= 21 and thang == 6) or (ngay <= 22 and thang == 7):
        return 'Cự Giải'
    elif (ngay >= 23 and thang == 7) or (ngay <= 22 and thang == 8):
        return 'Sư Tử'
    elif (ngay >= 23 and thang == 8) or (ngay <= 22 and thang == 9):
        return 'Xử Nữ'
    elif (ngay >= 23 and thang == 9) or (ngay <= 22 and thang == 10):
        return 'Thiên Bình'
    elif (ngay >= 23 and thang == 10) or (ngay <= 22 and thang == 11):
        return 'Bọ Cạp'
    elif (ngay >= 22 and thang == 11) or (ngay <= 21 and thang == 12):
        return 'Nhân Mã'
    elif (ngay >= 22 and thang == 12) or (ngay <= 19 and thang == 1):
        return 'Ma Kết'
    elif (ngay >= 20 and thang == 1) or (ngay <= 18 and thang == 2):
        return 'Bảo Bình'
    elif (ngay >= 19 and thang == 2) or (ngay <= 20 and thang == 3):
        return 'Song Ngư'
if so_ngay_hop_le(ngay, thang):
    print(cung_hoang_dao(ngay, thang))
else:
    print('Ngày tháng không hợp lệ')
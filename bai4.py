n = int(input('Nhập số tiền: '))

def so_chai_bia(n, gia=28):
    so_chai_mua = n // gia
    tong_chai = so_chai_mua
    vo_chai = so_chai_mua

    while vo_chai >= 3:
        chai_doi_them = vo_chai // 3
        vo_du = vo_chai % 3
        tong_chai += chai_doi_them
        vo_chai = chai_doi_them + vo_du

    return tong_chai

print('Số chai bia mua được là: ', so_chai_bia(n))
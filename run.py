import numpy as np
from gen import *


lstMauMatTuNhien=["Đen","Nâu","Lam","Vàng","Xám","Lục","Đỏ","Tím","Dị sấc"]
lstKieuMat=["To","Vừa","Nhỏ"]
lstMauTocTuNhien=["Đen","Nâu","Lam","Vàng","Đỏ"]
#lstMauDaTuNhien=["Đen", "Trắng", "Vàng"]
lstSongMuiTuNhien=["Cao","Vừa","Thấp"]
lstKieuTocTuNhien=["Xoăn","Thẳng"]
lstKieuMoi=["Dày","Mỏng","Vừa"]

#lstChungToc=[1:"Đại chủng Xích đạo Phi",2:"Đại chủng Xích đạo Úc",3:"Hợp nhóm chuyên tiếp giữa các đại chủng Xích đạo đại chủng Âu",4:"Đại chủng Âu",5:"Hợp nhóm chuyển tiếp giữa Âu và Á",6:"Đại chủng Á",7:"Hợp nhóm chuyển tiếp giữa đại chủng Á và Xích đạo"]
#https://vi.wikipedia.org/wiki/M%C3%A0u_da


fieldnames = ['row', 'MauMatTuNhien','KieuMat', 'MauTocTuNhien', 'MauDaTuNhien', 'SongMuiTuNhien'
            , 'KieuTocTuNhien', 'KieuMoi', 'ChungToc']

records = []
for i in range(1000):
    record = {'row' : 0, 'MauMatTuNhien':'','KieuMat':'', 'MauTocTuNhien':'', 'MauDaTuNhien':'', 'SongMuiTuNhien':''
            , 'KieuTocTuNhien':'','KieuMoi':'',  'ChungToc':''}
    record['row'] = i+1
    record['MauMatTuNhien']=(choose2(lstMauMatTuNhien, 40, 50, 5.5,2,1,0.5,0.5,0.3,0.2))
    record['KieuMat']=(choose2(lstKieuMat, 40,10,50))
    record['MauTocTuNhien']=(choose2(lstMauTocTuNhien, 40, 44, 1,10,5))
    record['MauDaTuNhien']=(int(np.random.normal(22,6, 1)))
    record['SongMuiTuNhien']=(choose2(lstSongMuiTuNhien, 33, 33, 34))
    record['KieuTocTuNhien']=(choose2(lstKieuTocTuNhien, 50,50))
    record['KieuMoi']=(choose2(lstKieuMoi, 30,30,40))
    record['ChungToc']=''
    records.append(record)


with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

import numpy as np
from gen import *


lstMauMatTuNhien=["Đen","Lam","Vàng","Xám","Lục","Đỏ","Tím","Dị sấc"]
lstKieuMat=["To","Vừa","Nhỏ"]
lstMauTocTuNhien=["Đen","Vàng","Đỏ"]
lstRauTocLong=["Rậm", "Thưa"]
lstKieuMuiTuNhien=["Cao","Thấp"]
lstKieuTocTuNhien=["Xoăn","Thẳng","Lượn sóng"]
lstKieuMoi=["Dày","Mỏng","Vừa"]


def phanPhoiChuan(a,b,c):
    d=-1
    while d<1 or d>35:
        d=(int(np.random.normal(a,b,c)))
    return d


#lstChungToc=[1:"Đại chủng Xích đạo Phi",2:"Đại chủng Xích đạo Úc",3:"Hợp nhóm chuyên tiếp giữa các đại chủng Xích đạo đại chủng Âu",4:"Đại chủng Âu",5:"Hợp nhóm chuyển tiếp giữa Âu và Á",6:"Đại chủng Á",7:"Hợp nhóm chuyển tiếp giữa đại chủng Á và Xích đạo"]
#https://vi.wikipedia.org/wiki/M%C3%A0u_da


fieldnames = [ 'Màu Mắt','Kiểu Mắt', 'Màu Tóc Tự Nhiên', 'Màu Da', 'Kiểu Mũi'
            , 'Kiểu Tóc', 'Kiểu Môi','Râu Tóc Lông', 'Chủng Tộc']

records = []
for i in range(3000):
    record = { 'Màu Mắt':'','Kiểu Mắt':'', 'Màu Tóc Tự Nhiên':'', 'Màu Da':'', 'Kiểu Mũi':''
            , 'Kiểu Tóc':'','Kiểu Môi':'','Râu Tóc Lông':'',  'Chủng Tộc':''}
   
    record['Màu Mắt']=(choose2(lstMauMatTuNhien, 80, 10.5,2,6,0.5,0.5,0.3,0.2))
    record['Kiểu Mắt']=(choose2(lstKieuMat, 40,10,50))
    record['Màu Tóc Tự Nhiên']=(choose2(lstMauTocTuNhien, 75,20,5))
#    record['Màu Da']=(int(np.random.normal(22,6, 1)))
    record['Màu Da']=phanPhoiChuan(17,10, 1)
    record['Kiểu Mũi']=(choose2(lstKieuMuiTuNhien,40, 60))
    record['Kiểu Tóc']=(choose2(lstKieuTocTuNhien, 30,35,35))
    record['Kiểu Môi']=(choose2(lstKieuMoi, 30,30,40))
    record['Râu Tóc Lông']=(choose2(lstRauTocLong, 50,50))

    record['Chủng Tộc']=''
    records.append(record)


with open('dataSinhv2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

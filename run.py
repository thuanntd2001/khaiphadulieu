import numpy as np
from gen import *


lstMauMatTuNhien=["Đen","Nâu","Lam","Vàng","Xám","Lục","Đỏ","Tím","Dị sấc"]
lstKieuMat=["To","Vừa","Nhỏ"]
lstMauTocTuNhien=["Đen","Nâu","Lam","Vàng","Đỏ"]
lstRauTocLong=["Rậm", "Thưa"]
lstKieuMuiTuNhien=["Cao","Gãy","Thấp","Lỗ mũi to"]
lstKieuTocTuNhien=["Xoăn","Thẳng","Lượn sóng"]
lstKieuMoi=["Dày","Mỏng","Vừa"]
lstKieuKhuonMat=["Dài","Dô","Ngắn","Bẹt"]

#lstChungToc=[1:"Đại chủng Xích đạo Phi",2:"Đại chủng Xích đạo Úc",3:"Hợp nhóm chuyên tiếp giữa các đại chủng Xích đạo đại chủng Âu",4:"Đại chủng Âu",5:"Hợp nhóm chuyển tiếp giữa Âu và Á",6:"Đại chủng Á",7:"Hợp nhóm chuyển tiếp giữa đại chủng Á và Xích đạo"]
#https://vi.wikipedia.org/wiki/M%C3%A0u_da


fieldnames = [ 'Màu Mắt','Kiểu Mắt', 'Màu Tóc Tự Nhiên', 'Màu Da', 'Kiểu Mũi'
            , 'Kiểu Tóc', 'Kiểu Môi','Râu Tóc Lông','Kiểu Khuôn Mặt', 'Chủng Tộc']

records = []
for i in range(2000):
    record = { 'Màu Mắt':'','Kiểu Mắt':'', 'Màu Tóc Tự Nhiên':'', 'Màu Da':'', 'Kiểu Mũi':''
            , 'Kiểu Tóc':'','Kiểu Môi':'','Râu Tóc Lông':'','Kiểu Khuôn Mặt':'',  'Chủng Tộc':''}
   
    record['Màu Mắt']=(choose2(lstMauMatTuNhien, 35, 45, 10.5,2,6,0.5,0.5,0.3,0.2))
    record['Kiểu Mắt']=(choose2(lstKieuMat, 40,10,50))
    record['Màu Tóc Tự Nhiên']=(choose2(lstMauTocTuNhien, 40, 44, 1,10,5))
    record['Màu Da']=(int(np.random.normal(22,6, 1)))
    record['Kiểu Mũi']=(choose2(lstKieuMuiTuNhien,25, 15, 35,25))
    record['Kiểu Tóc']=(choose2(lstKieuTocTuNhien, 40,40,20))
    record['Kiểu Môi']=(choose2(lstKieuMoi, 30,30,40))
    record['Râu Tóc Lông']=(choose2(lstRauTocLong, 50,50))
    record['Kiểu Khuôn Mặt']=(choose2(lstKieuKhuonMat, 25,20,15,40))
    record['Chủng Tộc']=''
    records.append(record)


with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

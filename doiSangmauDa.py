import pandas as pd
import random
df = pd.read_csv('dataTrain.csv')


#1:Phi,2:Uc,3:Au,4:A
lstxoa=[]

for i in range(754):

    if df.iloc[i, 3] <10:
        df.iloc[i, 3] = "Trắng sáng"
    elif df.iloc[i, 3] <15:
        df.iloc[i, 3] = "Trắng"
    elif df.iloc[i, 3] <27:
        df.iloc[i, 3] = "Nâu Vàng"
    else:
        df.iloc[i, 3] = "Nâu Sậm"


    
df.to_csv('data1234.csv', encoding='utf-8', index=False)

import pandas as pd
import random
df = pd.read_csv('data.csv')

#1:,2:,3:Au,4

for i in range(0, 2999):
#mat
    if df.iloc[i, 0] != 'Đen':
        df.iloc[i, 8] = 3
    else:
#toc
        if df.iloc[i, 2] != 'Đen':
            df.iloc[i, 8] = 3
        else:
            if df.iloc[i, 3] < 10:
                df.iloc[i, 8] = 3
            elif df.iloc[i, 3] >= 10 and df.iloc[i, 3] < 16:
                if df.iloc[i, 4] == 'Thấp':
                    df.iloc[i, 8] = 4
                else:
                    if df.iloc[i, 7] == 'Rậm':
                        df.iloc[i, 8] = 3
                    else:
                        df.iloc[i, 8] = 4
            elif df.iloc[i, 3] >= 16 and df.iloc[i, 3] < 28:
                if df.iloc[i, 5] != 'Lượn sóng':
                    df.iloc[i, 8] = 4
                else:
                    if df.iloc[i, 7] == 'Rậm':
                        if df.iloc[i, 6] == 'Dày':
                            df.iloc[i, 8] = 2
                        else:
                            df.iloc[i, 8] = 4
                    else:
                        df.iloc[i, 8] = 4
            else:
                if df.iloc[i, 6] == 'Dày':
                    df.iloc[i, 8] = 1
                else:
                    if df.iloc[i, 1] == 'To':
                        if df.iloc[i, 7] == 'Rậm':
                            df.iloc[i, 8] = 2
                        else:
                            df.iloc[i, 8] = 1
                    else:
                        if df.iloc[i, 5] == 'Xoăn':
                            df.iloc[i, 8] = 1
                        elif df.iloc[i, 5] == 'Thẳng':
                            df.iloc[i, 8] = 4
                        else:
                            df.iloc[i, 8] = 2
df.to_csv('500_dong_tree/data.csv', encoding='utf-8', index=False)

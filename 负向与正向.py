import pandas as pd

data = pd.read_csv('data/情感分析结果.csv',header=0) # .astype(str)
pdata = data[data.情感得分 == 2]
mdata = data[data.情感得分 == 1]
ndata = data[data.情感得分 == 0]
pdata.to_csv('data\正向情感.csv',encoding='utf8',header=True)
mdata.to_csv('data\中性情感.csv',encoding='utf8',header=True)
ndata.to_csv('data\负向情感.csv',encoding='utf8',header=True)
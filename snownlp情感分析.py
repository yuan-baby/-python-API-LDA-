import pandas as pd
import numpy as np
from snownlp import SnowNLP
import jieba

data = pd.read_csv('data/评论.txt',header=0).astype(str)
with open('stopWords/1893（utf8）.txt','r',encoding='utf-8') as f:
    stopwords=set([line.replace('\n','')for line in f])
f.close()
sum=0
count=0
for i in range(len(data['评论内容'])):
    line=jieba.cut(data.loc[i,'评论内容'])           #分词
    words=''
    for seg in line:
        if seg not in stopwords and seg!=" ":        #文本清洗 
            words=words+seg+' '
    if len(words)!=0:
        #print(words)        #输出每一段评论的情感得分
        d=SnowNLP(words)
        #print('{}'.format(d.sentiments))
        data.loc[i,'情感得分']=float(d.sentiments)     #原数据框中增加情感得分列
        sum+=d.sentiments
        count+=1
score=sum/count
#print('finalscore={}'.format(score))    #输出最终情感得分
#将情感得分结果保存为新的csv文件
data.to_csv('data\情感分析结果.csv',encoding='utf8',header=True)
pdata = data[data.情感得分 >= 0.5]
ndata = data[data.情感得分 < 0.5]
pdata.to_csv('data\正向情感.csv',encoding='utf8',header=True)
ndata.to_csv('data\负向情感.csv',encoding='utf8',header=True)
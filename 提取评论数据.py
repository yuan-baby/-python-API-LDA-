import pandas as pd
import numpy as np
import re

a = pd.read_excel("data\111点评评论API采.xlsx",header=0,usecols=[1])
a['评论内容'] = a['评论内容'].apply(lambda x :' '.join(re.findall('[\u4e00-\u9fa5。，！：？]+',x)))
b = open("data\评论.txt",'w')
a.to_csv(b)

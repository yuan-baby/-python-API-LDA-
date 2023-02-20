import requests
import re
import json
import pandas as pd
import jieba

# 将 text 按照 lenth 长度分为不同的几段
def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    return textArr # 返回多段值

def get_emotion(data):
    # 请求地址
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'
    # 产品密钥
    access_token = token = '【之前获取的access token】' 
    # 请求参数
    params = {
        'access_token': access_token
    }
    # 请求头
    headers = {
        'Content-Type': 'application/json'
    }
    # 百度情感分析API的上限是2048字节，因此判断文章字节数小于2048，则直接调用
    if (len(data.encode()) < 2048):
        new_each = {
            'text': data  # 将文本数据保存在变量new_each中，data的数据类型为string
        }
        new_each = json.dumps(new_each)
        res = requests.post(url, params=params, headers=headers, data=new_each)  # 利用URL请求百度情感分析API
        # print("content: ", res.content)
        res_text = res.text  # 保存分析得到的结果，以string格式保存
        result = res_text.find('items')  # 查找得到的结果中是否有items这一项
        positive = 1
        if (result != -1):  # 如果结果不等于-1，则说明存在items这一项
            json_data = json.loads(res.text)
            negative = (json_data['items'][0]['negative_prob'])  # 得到消极指数值
            positive = (json_data['items'][0]['positive_prob'])  # 得到积极指数值
            print("positive:",positive)
            print("negative:",negative)
            # print(positive)
            if (positive > negative):  # 如果积极大于消极，则返回2
                return 2
            elif (positive == negative):  # 如果消极等于积极，则返回1
                return 1
            else:
                return 0  # 否则，返回0
        else:
            return 1
    else:
        data = cut_text(data, 1500)  # 如果文章字节长度大于1500，则切分
        # print(data)
        sum_positive = 0.0  # 定义积极指数值总合
        sum_negative = 0.0  # 定义消极指数值总和
        for each in data:  # 遍历每一段文字
            # print(each)
            new_each = {
                'text': each  # 将文本数据保存在变量new_each中
            }
            new_each = json.dumps(new_each)
            res = requests.post(url, params=params, headers=headers, data=new_each)  # 利用URL请求百度情感分析API
            # print("content: ", res.content)
            res_text = res.text  # 保存分析得到的结果，以string格式保存
            result = res_text.find('items')  # 查找得到的结果中是否有items这一项
            if (result != -1):
                json_data = json.loads(res.text)  # 如果结果不等于-1，则说明存在items这一项
                positive = (json_data['items'][0]['positive_prob'])  # 得到积极指数值
                negative = (json_data['items'][0]['negative_prob'])  # 得到消极指数值
                sum_positive = sum_positive + positive  # 积极指数值加和
                sum_negative = sum_negative + negative  # 消极指数值加和
                # print(positive)
        print(sum_positive)
        print(sum_negative)
        if (sum_positive > sum_negative):  # 如果积极大于消极，则返回2
            return 2
        elif (sum_positive == sum_negative):  # 如果消极等于于积极，则返回1
            return 1
        else:
            return 0  # 否则，返回0
    # # 请求体
    # data = {
    #     'text': '太好了'
    # }
    # # 发送请求
    # response = requests.post(url, params=params, headers=headers, data=json.dumps(data))
    # # 获取响应
    # result = response.json()

with open('stopWords/1893（utf8） copy.txt','r',encoding='utf-8') as f:
    stopwords=set([line.replace('\n','')for line in f])
f.close()
data = pd.read_csv('data/评论.txt',header=0).astype(str)
sum = 0
count = 0
for i in range(len(data['评论内容'])):
    line=jieba.cut(data.loc[i,'评论内容'])           #分词
    words=''
    for seg in line:
        if seg not in stopwords and seg!=" ":        #文本清洗 
            words=words+seg+' '
    if len(words)!=0:
        #print(words)        #输出每一段评论的情感得分
        d=get_emotion(words)
        #print('{}'.format(d.sentiments))
        data.loc[i,'情感得分']=float(d)     #原数据框中增加情感得分列
        sum+=d
        count+=1
score=sum/count
#print('finalscore={}'.format(score))    #输出最终情感得分
#将情感得分结果保存为新的csv文件
data.to_csv('data\情感分析结果.csv',encoding='utf8',header=True)
pdata = data[data.情感得分 == 2]
mdata = data[data.情感得分 == 1]
ndata = data[data.情感得分 == 0]
pdata.to_csv('data\正向情感.csv',encoding='utf8',header=True)
mdata.to_csv('data\中性情感.csv',encoding='utf8',header=True)
ndata.to_csv('data\负向情感.csv',encoding='utf8',header=True)
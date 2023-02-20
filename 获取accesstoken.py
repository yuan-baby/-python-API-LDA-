# encoding:utf-8
import requests

# client_id 为官网获取的API Key， client_secret 为官网获取的Secret Key
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【输入创建处的应用client ID】&client_secret=【输入创建处的应用client secret】'
response = requests.get(host)
if response:
    print(response.json())

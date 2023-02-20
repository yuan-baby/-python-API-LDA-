#绘制不同类型的词云图
import stylecloud
# with open('data\负向情感分词.txt','r',encoding='utf-8') as a:
with open('data\正向情感分词.txt','r',encoding='utf-8') as a:
# with open('data\分词和停用后.txt','r',encoding='utf-8') as a:
    b = a.read()
    a.close()
clouds=stylecloud.gen_stylecloud(
        text=b, # 上面分词的结果作为文本传给text参数
        size=512,
        font_path='C:/Windows/Fonts/msyh.ttc', # 字体设置
        palette='cartocolors.qualitative.Pastel_7', # 调色方案选取，从palettable里选择
        gradient='horizontal', # 渐变色方向选了垂直方向
        icon_name='fab fa-weixin',  # 蒙版选取，从Font Awesome里选
        # output_name='负向情感词云图.png')
        output_name='正向情感词云图.png')
        # output_name='总体词云图.png') # 输出词云图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']  #显示中文标签,处理中文乱码问题
plt.rcParams['axes.unicode_minus']=False  #坐标轴负号的处理
plt.axes(aspect='equal')  #将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆

#构造数据
edu = [0.1433, 0.8567] # 负向情感和正向情感评论的占比
labels = ['负向情感','正向情感']
# explode = [0, 0.1, 0, 0, 0]  #生成数据，用于凸显
colors = ['#5698c3', '#92b3a5']  #自定义颜色

plt.pie(x=edu,  #绘图数据
        # explode=explode, #指定饼图某些部分的突出显示，即呈现爆炸式
        labels=labels,  #添加教育水平标签
        colors=colors,
        autopct='%.2f%%',  #设置百分比的格式，这里保留两位小数
        pctdistance=0.8,  #设置百分比标签与圆心的距离
        labeldistance=1.1,  #设置教育水平标签与圆心的距离
        startangle=180,  #设置饼图的初始角度
        radius=1.2,  #设置饼图的半径
        counterclock=False,  #是否逆时针，这里设置为顺时针方向
        wedgeprops={'linewidth':1.5, 'edgecolor':'white'},  #设置饼图内外边界的属性值
        textprops={'fontsize':10, 'color':'black'},  #设置文本标签的属性值
        )

#添加图标题
plt.title('情感倾向性分析结果')
#显示图形
plt.savefig('data\情感倾向性分析结果.png',dpi = 200)
plt.show()
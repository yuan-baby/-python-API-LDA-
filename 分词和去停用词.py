# 载入停用词表
#
# 主要思想是分词过后，遍历一下停用词表，去掉停用词。
import jieba


# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopWords/1893（utf8） copy.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr



# inputs = open('data/评论.txt', 'r', encoding='utf8')
# inputs = open('data/正向情感.csv', 'r', encoding='utf8')
inputs = open('data/负向情感.csv', 'r', encoding='utf8')

# outputs = open('data/分词和停用后.txt', 'w',encoding='utf8')
# outputs = open('data/正向情感分词.txt', 'w',encoding='utf8')
outputs = open('data/负向情感分词.txt', 'w',encoding='utf8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
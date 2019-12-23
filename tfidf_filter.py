import db_tool
import DataModel
from sklearn.feature_extraction.text import TfidfVectorizer

session = db_tool.Session()
models = session.query_all(DataModel.JianggeWeiboWordcut)
corpus = []

for model in models:
    model: DataModel.JianggeWeiboWordcut
    weibo_line = model.post_text.replace(';',' ')
    corpus.append((weibo_line))
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names()
weight = tfidf_matrix.toarray()
for i in range(len(weight)):
    tuple_list = []
    for j in range(len(words)):
        word = words[j]
        tfidf_result = weight[i][j]
        tuple_list.append((word, tfidf_result))
    sorted_tuple_list = sorted(tuple_list, key=lambda o: o[1], reverse=True)
    #print(sorted_tuple_list[:3][0])
    # 排序使用的是元组的list，需要取出每个元素的第一个位置，组成一个新字符串的list，然后再join; 使用循环或者map函数
    result = ';'.join(list(map(lambda o:o[0],sorted_tuple_list[:3])))
    #print(result)
    new_model = DataModel.JianggeWeiboTfidfFilter()
    db_tool.model_setter(models[i], new_model)
    new_model.sid = models[i].sid
    new_model.tfidf = result
    session.db_writer(new_model)

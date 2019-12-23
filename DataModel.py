from sqlalchemy import Column, NVARCHAR, Integer, TEXT, DATE, TIME, BOOLEAN, VARCHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class JianggeWeibo(Base):
    __tablename__ = "jiangge_weibo"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(VARCHAR(255))
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)


class JianggeWeiboPostTextClean(Base):
    __tablename__ = "jiangge_weibo_post_text_clean"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(VARCHAR(255))
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)
    emoji = Column(VARCHAR)


class JianggeWeiboWordcut(Base):
    __tablename__ = "jiangge_weibo_wordcut"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(TEXT)
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)
    emoji = Column(VARCHAR)


class JianggeWeiboTfidfFilter(Base):
    __tablename__ = "jiangge_weibo_tfidf_filter"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(TEXT)
    tfidf = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)


class JianggeWeiboIsinTest(Base):
    __tablename__ = "jiangge_weibo_dataisin_test"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(VARCHAR(255))
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)
    emoji = Column(VARCHAR)


class JianggeWeiboTestWordcut(Base):
    __tablename__ = "jiangge_weibo_test_wordcut"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(TEXT)
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)
    emoji = Column(VARCHAR)


class JianggeWeiboTestTfidf(Base):
    __tablename__ = "jiangge_weibo_test_tfidf"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(TEXT)
    tfidf = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)


class JianggeWeiboStrip(Base):
    __tablename__ = "jiangge_weibo_strip"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(VARCHAR(255))
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)


class JianggeWeiboStripTest(Base):
    __tablename__ = "jiangge_weibo_striptest"
    sid = Column(Integer, primary_key=True)
    keyword = Column(VARCHAR(255))
    user_id = Column(VARCHAR(255))
    user_name = Column(VARCHAR(255))
    user_link = Column(VARCHAR(255))
    post_text = Column(VARCHAR(255))
    post_link = Column(VARCHAR(255))
    post_date = Column(DATE)
    post_time = Column(TIME)
    num_retweet = Column(Integer)
    num_comment = Column(Integer)
    num_like = Column(Integer)
    ori_flag = Column(Integer)
    emoji = Column(VARCHAR)
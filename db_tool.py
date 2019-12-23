from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import DataModel
import env


class Session(object):
    def __init__(self, connect_str=env.connect_str):
        engine = create_engine(connect_str)
        self.__session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)()

    def db_writer(self, model):
        self.__session.add(model)
        self.__session.commit()

    def db_list_writer(self, models):
        self.__session.bulk_save_objects(models)
        self.__session.commit()

    def close_session(self):
        self.__session.close()

    def query_all(self, model_name):
        return self.__session.query(model_name).all()

    def query_where_post_text_is_null(self):
        # 返回post_text列中有内容的全部数据
        return self.__session.query(DataModel.JianggeWeibo).filter(DataModel.JianggeWeibo.post_text).all()

    def update_with_ori_flag(self, model):
        self.__session.query(DataModel.JianggeWeibo).filter(DataModel.JianggeWeibo.sid == model.sid).update(
            {DataModel.JianggeWeibo.ori_flag: model.ori_flag})
        self.__session.commit()

    def posttext_delete(self, model):
        self.__session.query(DataModel.JianggeWeibo).filter(DataModel.JianggeWeibo.sid == model.sid).delete()
        self.__session.commit()

    def posttext_delete_test(self, model):
        self.__session.query(DataModel.JianggeWeiboIsinTest).filter(
            DataModel.JianggeWeiboIsinTest.sid == model.sid).delete()
        self.__session.commit()


# 复制model
def model_setter(src_model: object, des_model: object):
    props = list(filter(lambda o: o[0] != '_', dir(src_model)))
    for prop in props:
        # 不复制sid列
        if prop == 'sid':
            continue
        setattr(des_model, prop, getattr(src_model, prop))
    return des_model

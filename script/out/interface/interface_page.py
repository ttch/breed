# *-* coding=utf-8 *-*


#page接口



class page:
    #每个page都从上传递配置文件类，这是生命的根基
    def __init__(self,config):
        this.__config = config
        pass
    def __del__(self):
        pass
    # make函数
    #用来生成目标码
    def make(self):
        pass


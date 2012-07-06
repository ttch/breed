# *-* coding=utf-8 *-*

#核心组件父类
class br_component:
    def __init__(self):
        pass

#对象注册列表
class register_list:
    def __init__(self):
        self.__list = {}

    def append(self,component_name,class_object):
        if component_name == "" or component_name == None :
            print "组件名称为空串或者为空 错误 -247"
            return
        if class_object != None:
            self.__list[component_name] = class_object
        else:
            print "组件对象为空 错误 - 246"

#全局公用组件注册表
g_register_list = register_list()

#组件初始化
def component_list():
    pass
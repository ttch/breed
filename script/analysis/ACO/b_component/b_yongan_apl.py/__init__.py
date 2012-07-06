
component_chnname = "永安核心业务系统简易投保人模块"
component_name = "yongan_apl"
component_ver = "1.0"

class yongan_apl:
    def __init__(self,parent):
        pass
    def get_config(self):
        handle = open("component.config","r")
        config_str = ""
        for aline in handle.readlines():
            config_str = config_str + aline
        return config_str
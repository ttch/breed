# *-* coding=utf-8 *-*
#服务端代码输出
from jinja2 import Template
from jinja2 import Environment
import interface_outter

def write_file(filename,write_str):
    x = open(filename,"w")
    x.write(write_str)
    x.close


class web_outter:
    def __init__(self,col_list,main_config):
        self.__stru_list = col_list
        self.__main_config = main_config
        #print self.__stru_list.get_list()
    def make(self,stru_conf):
        stru_list = self.__stru_list.get_list()
        for tbl_item in stru_list:
            for tbl_name in tbl_item:
                tbl_list =  tbl_item[tbl_name]
                send = ""
                recv = ""
                for x in tbl_list:
                    send = send +self.servlet_send_js(x)+"\n"
                    recv = recv+self.servlet_recv_js(x)+"\n"

                write_file("D:\\Project\\PythonProject\\breed\\breed_orice\\out\\web\\recv\\"+tbl_name+".js",recv.encode("utf-8"))
                write_file("D:\\Project\\PythonProject\\breed\\breed_orice\\out\\web\\send\\"+tbl_name+".js",send.encode("utf-8"))
        #print stru_conf.get_out("out_dir")
    def servlet_send_js(self,field):
        var_f = open(self.__main_config.get_tpldir()+"UI\\form\\send_js.tpl")

        tpl_str = ""
        for x in var_f.readlines():
            tpl_str = tpl_str+x
        template = Template(tpl_str)
        x = template.render( name = field[1].decode("utf-8"),remarks=field[6].decode("gb2312") )
        return x
    def servlet_recv_js(self,field):
        var_f = open(self.__main_config.get_tpldir()+"UI\\form\\recv_js.tpl")

        tpl_str = ""
        for x in var_f.readlines():
            tpl_str = tpl_str+x
        template = Template(tpl_str)
        x = template.render( name = field[1].decode("utf-8"),remarks=field[6].decode("gb2312") )
        return x

    def make_WEB_INF(self):
        pass
    def __replace (self,id,str,tpl_str):
        field_reder = Template(tpl_str)
        return field_reder.render({id:str})

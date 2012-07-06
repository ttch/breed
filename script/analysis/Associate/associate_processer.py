# *-* coding=utf-8 *-*
import oracle_db
import database_config
import jstruct

#关系代码处理器
class associate_processer:
    def __init__(self,var_main,var_struct):
        self.__var_main = var_main
        self.__var_struct = var_struct

    def process(self):
        #var_db = oracle_db.oracle_db_create_database(self.__var_struct.get_structs())
        #var_db.make()
        #先处理DB
        var_stru = self.__var_struct.get_structs()
        for x in var_stru:
            config_name = self.__var_main.get_page_config_dir()+"\\database\\"+self.__var_struct.get_db_config_file(x)

            #读取db_field的配置
            a_var = database_config.db_config(self.__var_main,config_name,)
            a_var.read_all()
            a_list =a_var.get_fields()

            oracle_db.create_all(a_list,a_var.get_table_name())

            #然后trans
            var_struct = jstruct.json_struct(a_list,a_var.get_table_name())
            var_struct.make()

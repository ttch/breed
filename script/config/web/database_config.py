# *-* coding=utf-8 *-*


class db_config:
    def __init__(self,main_config,config_filename):
        self.__main_config = main_config
        self.__cfg_filename = config_filename
        self.__tbl_name = ""
        self.__file_dict = []
    def __del__(self):
        self.__main_config = None
        #self.file_handle = open(config_dir+"main.config")
    def read_all(self):
        var_structs = self.__main_config.get_strcuts()
        var_file = open(self.__cfg_filename)
        for var_line in var_file.readlines():
            self.__tbl_name = var_line.split("|")[0]
            #跳过注释
            if var_line[0] == "#":
                continue
            #跳过空行和换行
            elif var_line[0] == "\n":
                continue
            else:
                self.__file_dict.append( var_line[0:-1])
        var_file.close
        var_file = None

    def get_table_name(self):
        return self.__tbl_name

    def get_fields(self):
        list = []
        for a_item in self.__file_dict:
            list.append( a_item.split("|") )
        return list
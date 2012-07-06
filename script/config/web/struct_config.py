# *-* coding=utf-8 *-*


# struct read config
class struct_config:

    def __init__(self,main_config):
        self.__file_dict = []
        self.__main_config = main_config
        self.__struct_list = {}
        self.__db_list = {}
        self.__struct = []
        self.__out_name = {}

    def __del__ (self):
        self.__file_dict = []
        self.__action_list = {}

    def __read__struct(self):
        iread = 0

        for x in self.__file_dict:
            if x == "--struct--":
                iread = 1
                continue
            if iread == 1:
                if x == "--end--":
                    return
                else:
                    self.__struct.append(x)
    #读取Action
    def __read__dict(self):
        action_name = ""
        for x in self.__struct:
            item = x.split("|")

            if action_name != item[0]:
                action_name = item[0]
                self.__struct_list[item[0]] = []
            else:
                pass
            self.__struct_list[item[0]].append(item)
    def __read__outname(self):
        iread = 0
        temp_list = []
        for x in self.__file_dict:
            if x == "--out--":
                iread = 1
                continue
            if iread == 1:
                if x == "--end--":
                    break
                else:
                    temp_list.append(x)
        for x in temp_list:
            aline = x.split("=")
            self.__out_name[aline[0]] = aline[1]
    #读取DB
    def __read_db(self):
        iread = 0
        temp_list = []
        for x in self.__file_dict:
            if x == "--db--":
                iread = 1
                continue
            if iread == 1:
                if x == "--end--":
                    break
                else:
                    temp_list.append(x)
        for x in temp_list:
            a_item =x.split("=")
            self.__db_list[a_item[0].strip()] = a_item[1].strip()

    #读取所有
    def read_all(self):
        var_structs = self.__main_config.get_strcuts()
        for x in var_structs:
            var_file = open(self.__main_config.get_page_config_dir()+"struct\\"+x)
            for var_line in var_file.readlines():
                #跳过注释
                if var_line[0] == "#":
                    continue
                #跳过空行和换行
                elif var_line[0] == "\n":
                    continue
                else:
                    self.__file_dict.append( var_line[0:-1])
            self.__read__struct()
            self.__read__dict()
            self.__read_db()
            self.__read__outname()

            var_file.close
            var_file = None
    def get_struct(self,name):
        return self.__struct_list[name]
    def get_structs(self):
        return self.__struct_list
    def get_db_list(self):
        return self.__db_list
    def get_db_config_file(self,name):
        filename = self.__db_list[name].split(".")[0] + ".config"
        return filename
    def get_out(self,name):
        return self.__out_name[name]



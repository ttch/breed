# *-* coding=utf-8 *-*


# struct read config
class associate_config:

    def __init__(self,main_config):
        self.__file_dict = []
        self.__main_config = main_config

        self.__process_set = []
        self.__pages = []

    def __del__ (self):
        self.__file_dict = []

    #读取trans节
    def __read__process_set(self):
        iread = 0
        self.__process_set = []

        for x in self.__file_dict:
            if x == "--trans--":
                iread = 1
                continue
            if iread == 1:
                if x == "--end--":
                    return
                else:
                    self.__process_set.append(x)

    #读取page节
    def __read__pages(self):
        iread = 0
        self.__pages = []

        for x in self.__file_dict:
            if x == "--page--":
                iread = 1
                continue
            if iread == 1:
                if x == "--end--":
                    return
                else:
                    self.__pages.append(x)

    #读取所有
    def read_all(self):
        var_structs = self.__main_config.get_associate()
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

            self.__read__pages()
            self.__read__process_set()


            var_file.close
            var_file = None

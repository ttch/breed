# *-* coding=utf-8 *-*

#oracle 建库操作程序
"""


"""


#TODO: 设计template来替换现在手工的网页

def create_all(field_list,tbl_name):
    var_create = oracle_db_create_database(field_list,tbl_name)
    var_create.make()
    var_insert = oracle_db_insert_database(field_list,tbl_name)
    var_insert.make()
    var_update = oracle_db_update_database(field_list,tbl_name)
    var_update.make()

class oracle_db_create_database:
    def __init__(self,field_list,tbl_name):
        self.__field_list = field_list
        self.__name = tbl_name
    def make(self):
        #生成代码
        create_sql = "drop table %s ;\ncreate table %s (\n" % (self.__name,self.__name)
        for field in self.__field_list:
            field_sql = "\t%s " % field[1]
            if field[3] == "varchar2":
                field_sql = "%s%s(%s) "% (field_sql,field[3],field[2])
            else:
                field_sql = "%s%s " % (field_sql,field[3])
            if field[5] == "Y":
                field_sql = "%s%s " % (field_sql," NOT NULL")
            create_sql = create_sql+field_sql+",\n"
        create_sql = create_sql[0:-2]+"\n);\n"

#插入语句
class oracle_db_insert_database:
    def __init__(self,field_list,tbl_name):
        self.__field_list = field_list
        self.__name = tbl_name
    def make(self):
        insert_sql = "\"insert into "+self.__name+" (\"+\n"
        field_sql = "";
        value_sql = "";
        for field in self.__field_list:
            if field[3] == "varchar2":
                field_sql = "%s\",%s\"+\n" % ( field_sql,field[1])
                value_sql = "%s\",'\"+GetField(aJson,\"%s\")+\"'\"+\n" % (value_sql,field[1])
            if field[3][0:6] == "Number":
                field_sql = "%s\",%s\"+\n" % ( field_sql,field[1])
                value_sql = "%s\",\"+GetStringField(aJson,\"%s\")+\n" % (value_sql,field[1])
            #if field[3] == "date":
            #    field_sql = "%s\",%s\"+\n" % ( field_sql,field[1])
            #    value_sql = "%s\",'\"+GetStringField(\"%s\")+\"'\"+\n" % (value_sql,field[1])

        insert_sql = insert_sql+field_sql+"\") VALUES (\"+\n"+value_sql+"\")\";"


class oracle_db_update_database:
    def __init__(self,field_list,tbl_name):
        self.__field_list = field_list
        pass
    def make(self):
        pass

#增加字段
class oracle_db_alert_field:
    pass

#减少字段
class oracle_db_drop_field:
    pass

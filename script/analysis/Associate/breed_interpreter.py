# *-* coding=utf-8 *-*
import simplejson as json

def error_print(object,str):
    print( "%s %s" % (object,str) )
def _replace(str,old,new):
    return str.replace(old, new)

#------------------------------------------------------------------------------
#        breed 语言解析模块
#------------------------------------------------------------------------------
class BreedInterpreter:
    def __init__(self,tokens):
        self.__tokens = tokens
        self.__nameStack= []
        self.name = ""

        self.lib_sys = []
        self.lib_componet = []
        self.lib_custom = []

        self.out = {}
        #field字段
        self.field_list = []
        self.field_extends = []

        #组件
        self.function = {}

        self.com_desc = ""
    #------------------------------------------------------------------------------
    #    编译函数
    #------------------------------------------------------------------------------
    def Compile(self):
        adata = self.getNextToken()
        print adata
        if adata.type == 'PAGE' :
            self.process_page()
        elif adata.type == "COMPONENT":
            self.com_desc = self.process_component()
    #------------------------------------------------------------------------------
    #    处理组件模块部分
    #------------------------------------------------------------------------------
    def process_component(self):
        adata = self.getNextToken()
        if adata == None:
            print "ERROR PAGE IS NULL on lineno:%s - 0001" % (adata.lineno)
            return
        elif adata.type != "ID":
            print "ERROR PAGE IS NOT ID on lineno:%s - 00002" % (adata.lineno)
            return
        else:
            self.name = adata.value
        return self.process_lib()
    #------------------------------------------------------------------------------
    #    处理页函数
    #------------------------------------------------------------------------------
    def process_page(self):
        adata = self.getNextToken()
        if adata == None:
            print "ERROR PAGE IS NULL on lineno:%s - 0001" % (adata.lineno)
            return
        elif adata.type != "ID":
            print "ERROR PAGE IS NOT ID on lineno:%s - 00002" % (adata.lineno)
            return
        else:
            self.name = adata.value
        self.process_common()

    #------------------------------------------------------------------------------
    #    处理库部分函数
    #------------------------------------------------------------------------------
    def process_lib(self):
        a_var = Component(self.__tokens,self.function)
        return a_var.make()
            #处理component数据
    #------------------------------------------------------------------------------
    #                    处理公用部分
    #------------------------------------------------------------------------------
    def process_common(self):
        while(True):
            #tok.type, tok.value.decode("utf-8"), tok.lexpos , tok.lineno
            #解析page头
                #print self.__page_name
            #解析lib段
            adata = self.getNextToken()
            if adata == None:
                break
            if adata.type == 'LIB':
                while adata.type != 'END':
                    if adata.type == 'IMPORT':
                        self.process_import()
                    adata = self.getNextToken()
            #解析out段
            if adata.type == 'OUT':
                while adata.type != 'END':
                    if adata.type == 'ID':
                        if adata.value == 'out_dir':
                            key = adata.value
                            adata = self.getNextToken()
                            if adata.type == "EQUALS":
                                adata = self.getNextToken()
                                if adata.type == "STRING":
                                    value = adata.value
                                    self.out[key] = value
                    adata = self.getNextToken()
            #解析control段
            if adata.type == 'CONTROL':
                self.process_control()
    #------------------------------------------------------------------------------
    #        处理import模块代码
    #------------------------------------------------------------------------------
    def process_import(self):
        adata = self.getNextToken()
        if adata == None:
            print "ERROR PAGE IS NULL on lineno:%s - 0001" % (adata.lineno)
            return
        elif adata.type != "ID":
            print "ERROR PAGE IS NOT ID on lineno:%s - 00002" % (adata.lineno)
            return
        if adata.type == "ID":
            #系统部件
            if adata.value == "sys":
                #分析系统组件中的内容
                adata = self.getNextToken()
                self.read_lib("sys")
            if adata.value == "aoc":
                #分析标准组件中的内容
                adata = self.getNextToken()
                self.read_lib("aoc")
            if adata.value == "custom":
                #分析自定义组件中的内容
                adata = self.getNextToken()
                self.read_lib("custom")

    #------------------------------------------------------------------------------
    #                        获得下一个词
    #------------------------------------------------------------------------------
    def getNextToken(self):
        return self.__tokens.token()
    #------------------------------------------------------------------------------
    #                        分析库代码
    #------------------------------------------------------------------------------
    def read_lib(self,lib_type):
        while (True):
            adata = self.getNextToken()
            if adata.type == "COMMA":
                continue
            if adata == None or adata.type == "RPAREN":
                break
            if lib_type == "sys":
                self.lib_sys.append(adata.value)
            if lib_type == "aoc":
                self.lib_componet.append(adata.value)
            if lib_type == "custom":
                self.lib_custom.append(adata.value)

    #------------------------------------------------------------------------------
    #                分析控件代码
    #------------------------------------------------------------------------------
    def process_control(self):
        adata = self.getNextToken()
        while adata.type != 'END':
            adata = self.getNextToken()
            if adata.type == 'FIELD':
                adata = self.getNextToken()
                if (adata.type != 'DOT'):
                    error_print(a,"this site is a dot")
                    break
                adata = self.getNextToken()
                if adata.type == 'STRING':
                    self.field_list.append(adata.value)
                elif adata.type == "EXTENDS":
                    while(True):
                        adata = self.getNextToken()
                        if adata.type == "SEMI": break
                        self.__nameStack.append(adata)

                    self.process_function()
                    self.__nameStack = []
            if adata == None:
                return
    #------------------------------------------------------------------------------
    #        处理函数
    #------------------------------------------------------------------------------
    def process_function(self):
        i = 0
        l = len(self.__nameStack)
        while ( True):
            #(object . func ( param ) )
            adata = self.__nameStack[i]
            if adata.type == 'DOT':
                obj = self.__nameStack[i-1].value
                func = self.__nameStack[i+1].value
                i = i+1
            if adata.type == "LPAREN":
                adata = self.__nameStack[i+1]
                if adata.type == "ID":
                    param = adata.value
                if adata.type == "STRING":
                    param = adata.value
            i = i+1
            if i == l:
                break
        self.field_extends.append({"object":obj,"function":func,"param":param})
        isfunc = False

#------------------------------------------------------------------------------
#
# 处理控件格式类，1.0
# 需要把大部分数据都处理成json数据 格式。然后在模版中进行替换
#------------------------------------------------------------------------------
class Component:
    def __init__(self,tokens,function):
        self.__tokens = tokens
        self.__tokenStack = []
        self.__json_str = ""
        self.function =function
    #------------------------------------------------------------------------------
    #    获得下一个词
    #------------------------------------------------------------------------------
    def getNextToken(self):
        return self.__tokens.token()
    #------------------------------------------------------------------------------
    #    生成需要的格式
    #------------------------------------------------------------------------------
    def make(self):
        #读取lib中的内容
        while ( True ) :
            adata = self.getNextToken()
            if adata == None:
                break
            if adata.type == "FUNCTION":
                self.process_function()
            self.__tokenStack.append(adata)
        i = 0
        l = len ( self.__tokenStack )
        i,value = self.submake(self.__tokenStack,i,l)
        return value

    #------------------------------------------------------------------------------
    # 处理函数的函数
    # 只处理单语句 变量赋值
    # 暂时不支持跳转，函数调用，循环，循环嵌套等高级用法
    #------------------------------------------------------------------------------
    def process_function(self):
        func_name = ""
        param = []
        is_block = False
        while ( True):
            adata = self.getNextToken()
            #参数
            if adata.type == "ID":
                self.function[adata.value] = ""
                func_name = adata.value
            #参数
            if adata.type == "LPAREN":
                while(True):
                    adata = self.getNextToken()
                    if adata.type == "RPAREN":
                        break
                    if adata.type == "ID":
                        param.append(adata.value)
            if adata.type == "BLPAREN":
                while(True):
                    ( result,body ) = self.process_function_body()
                    if result == "BRPAREN":
                        self.function[func_name] = (param,body)
                        return



    #------------------------------------------------------------------------------
    #
    #    处理函数体
    #------------------------------------------------------------------------------
    def process_function_body(self):
        body = []
        body_stack = []
        while (True):
            adata = self.getNextToken()
            if adata.type == "BRPAREN":
                break
            body_stack.append(adata)
        i = 0
        l = len(body_stack)
        token = []

        while( True ):
            if i == l:
                break
            if body_stack[i].type == "SEMI":
                body.append(token)
                token = []
            token.append(body_stack[i])
            i = i+1
        return "BRPAREN" , body

    #------------------------------------------------------------------------------
    #    递归制作分析词组成JSON格式串
    #------------------------------------------------------------------------------
    def submake(self,tokenStack,i,l):
        jStr = "{"
        __json_token = []
        while ( True ) :
            #组装key

            if i >= l or i ==l-1 :
                jl = len(__json_token)
                ji = 0
                for atoken in __json_token:
                    if ji == jl-1:
                        jStr = jStr + atoken
                    else:
                        jStr = jStr +atoken+ " , "
                    ji = ji+1
                jStr = jStr + "}"
                return ( i , jStr)
            if tokenStack[i+1].type == "BRPAREN" and tokenStack[i+2].type == "SEMI":
                jl = len(__json_token)
                ji = 0
                for atoken in __json_token:
                    if ji == jl-1:
                        jStr = jStr + atoken
                    else:
                        jStr = jStr +atoken+ " , "
                    ji = ji+1
                jStr = jStr + "}"
                return ( i , jStr)
            adata = tokenStack[i]
            if adata.type == "EQUALS":
                if tokenStack[i+1].type == "STRING":
                    key = ""
                    value = ""
                    if i < l-1 and tokenStack[i+2].type == "PLUS":
                        key = _replace(_replace(tokenStack[i-1].value,"\"", "\\\""),"\'","\"")
                        value = ""
                        j = i+1
                        while (True):
                            if tokenStack[j].type == "STRING":
                                value = value + tokenStack[j].value
                            if tokenStack[j].type == "SEMI":
                                break
                            j = j+1
                        value = _replace(_replace(_replace(value,"\'",""),"\t",""),"\"","\\\"")
                        value = "\""+value+"\""
                        i = j
                    else:
                        key = _replace(_replace(tokenStack[i-1].value,"\"", "\\\""),"\'","\"")
                        value = _replace(_replace(tokenStack[i+1].value,"\"", "\\\""),"\'","\"")
                    __json_token.append("\"%s\":%s " % (
                                                 key,
                                                 value
                                                  )
                                        )
                if tokenStack[i+1].type == "BLPAREN":
                    key = tokenStack[i-1].value
                    value = ""
                    i,value = self.submake(tokenStack,i+1,l)
                    __json_token.append( "\"%s\": %s " % (key , value) )
            i = i+1






# *-* coding=utf-8 *-*
import sys
sys.path.append(".\\script\\analysis\\Associate")

import breed_lex
import breed_yacc
import breed_interpreter

compile_list = {}

def getScriptContent(script_name):
    file_handle = open(script_name)

    data = ""

    for aline in file_handle.readlines():
        data = data + aline
    return data

def readComponent(lib_name,components):
    if lib_name == "sys":
        for alib in components:
            data = getScriptContent(".\\script\\analysis\\ACO\\t_component\\"+alib+"\\component.config")
            breed_lex.lex.input(data)
            aCompile = breed_interpreter.BreedInterpreter(breed_lex.lex)
            aCompile.Compile()
            compile_list[aCompile.name] = aCompile
    if lib_name == "component":
        pass
    if lib_name == "custom":
        pass

def Compile(config_name):
    data = getScriptContent(config_name)

    # give the lexer some input
    breed_lex.lex.input(data)

    aCompile = breed_interpreter.BreedInterpreter(breed_lex.lex)
    aCompile.Compile()
    compile_list[aCompile.name] = aCompile
    #读取lib，进行分解进入库
    readComponent("sys",aCompile.lib_sys)
    readComponent("component",aCompile.lib_componet)
    readComponent("custom",aCompile.lib_custom)
    return compile_list

#!/usr/bin/env python3
#coding: utf-8

"""
This script transform cgd txt file to their symbolic represention
"""
import re
import sys
import os

DEFINED = ['char', 'int', 'float', 'double', 'wchar', 'wchar_t', 'unionType', 'uint32_t', 'uint8_t', 'size_t'
        'char*', 'int*', 'float*', 'double*', 'wchar*', 'wcahr_t*', 'unionType*', 'uint32_t*', 'uint8_t*', 'size_t*']

KEYWORD = ['Asm', 'auto', 'bool', 'break', 'case', \
        'catch', 'char', 'class', 'const_cast', 'continue', \
        'default', 'delete', 'do', 'double', 'else', \
        'enum', 'dynamic_cast', 'extern', 'false', 'float', \
        'for', 'union', 'unsigned', 'using', 'friend', \
        'goto', 'if', 'inline', 'int', 'long', \
        'mutable', 'virtual', 'namespace', 'new', 'operator', \
        'private', 'protected', 'public', 'register', 'void', \
        'reinterpret_cast', 'return', 'short', 'signed', 'sizeof' \
        'static	static_cast', 'volatile', 'struct', 'switch', \
        'template', 'this', 'throw', 'true', 'try', \
        'typedef', 'typeid', 'unsigned', 'wchar_t', 'while', \
        'buffer', 'flag', 'size', 'len', 'length', 'str', 'string', \
        'a', 'b', 'c', 'i', 'j', 'k']

def cgd_reader(file_name):
    cgd_list = []
    cgd_block = []
    cgd_dicts = []
    with open(file_name, 'rt') as f:
        for line in f:
            if line != '\n':
                cgd_block.append(line[:-1])
            else:
                cgd_list.append(cgd_block)
                cgd_block = []
    for block in cgd_list:
        cgd_dict = {}
        cgd_dict['name'] = block[0]
        cgd_dict['codes'] = block[1:-1]
        cgd_dict['res'] = block[-1]
        cgd_dicts.append(cgd_dict)
    return cgd_dicts

def get_variable(codes):
    var_list = []
    for line in codes:
        tokens = remove_empty(line.split(' '))
        for k, v in enumerate(tokens):
            rex = re.search('[a-z]+_[a-z]+_?[a-z]*_?[a-z]*[^(]', v)
            if rex:
                m = rex.group(0)
                var_list.append(re.sub('[-,;)*\[]', '', m))
            if v in DEFINED:
                tmp = remove_empty(''.join(tokens[k+1:]).split(','))
                for i in tmp:
                    if '=' in i:
                        var = i.split('=')[0]
                    else:
                        var = i
                    var_list.append(re.sub('[,;)*]', '', var))
    var_list = [x for x in var_list if x not in DEFINED and x not in KEYWORD]
    var_list_s = list(set(var_list))
    var_list_s.sort(key=var_list.index)
    return var_list_s

def var2sym(var_list, codes):
    syml = codes[:]
    for ind, var in enumerate(var_list):
        tmp_syml = []
        for k, v in enumerate(syml):
            tmp_syml.append(v.replace(var, 'VAR'+str(ind)))
        syml = tmp_syml[:]
    return syml

def remove_empty(l):
    return list(filter(None, l))

def cgd2sym(file_path, file):
    cgd_list = cgd_reader(file_path + '/' + file)
    sym_list = []
    for cgd in cgd_list:
        codes = cgd['codes']
        vl = get_variable(codes)
        symr = var2sym(vl, codes)
        cgd['symr'] = symr
        sym_list.append(cgd)
    with open(file[:-4]+'_symr.txt', 'wt') as f:
        for block in sym_list:
            f.write(block['name'] + '\n')
            for symr in block['symr']:
                f.write(symr + '\n')
            f.write(block['res'] + '\n')
            f.write('\n')


if __name__ == '__main__':
    file_path = sys.argv[1]
    file_list = os.listdir(file_path)
    for file in file_list:
        cgd2sym(file_path, file)

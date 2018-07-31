#!/usr/bin/env python3
#coding: utf-8

"""
This file load the data file and tranform it's cntent as python object.
"""
import re


KEYWORD = ['char', 'int', 'double', 'float', 'long', 'short', 'wchar',  \
        'char*', 'int*', 'double*', 'float*', 'long*', 'short*', 'wchar*']


class Loader:
    def __init__(self, file_path, file_type):
        self.file_path = file_path
        self.file_type = file_type
        self.raw_symr_list = []
        self.symr_list = []

    def txt2list(self):
        raw_symr = []
        with open(self.file_path) as f:
            for line in f:
                if line != '---------------------------------\n':
                    raw_symr.append(line[:-1])
                else:
                    self.raw_symr_list.append(raw_symr)
                    raw_symr = []
                    if len(self.raw_symr_list) == 10:
                        break

    def symr_list_praser(self):
        for block in self.raw_symr_list:
            self.symr_list.append(self.block_praser(block))

    def block_praser(self, block):
        symr_dict = {}
        symr_data = block[0].split(' ')
        symr_dict['id'] = symr_data[0]
        symr_dict['cve'] = symr_data[1].split('/')[0]
        symr_dict['name'] = symr_data[1].split('/')[1]
        symr_dict['type'] = symr_data[2]
        symr_dict['label'] = symr_data[3]
        code_block = [x for x in block[1:-1]]
        symr_dict['code'] = self.code_normalize(code_block)
        symr_dict['res'] = block[-1]
        return symr_dict

    def code_normalize(self, code_block):
        var_list = []
        for l in code_block:
            tmp = l.split(' ')
            for i in range(len(tmp)):
                if tmp[i] in KEYWORD:
                    var_list.append(tmp[i+1])
        for w in range(len(var_list)):
            var_list[w] = re.sub(r'[*, (, ), ;]', '', var_list[w])
        codes = code_block[:]
        for var in range(len(var_list)):
            for n in range(len(codes)):
                codes[n] = codes[n].replace(var_list[var], 'var'+str(var))
        return codes


if __name__ == '__main__':
    ld = Loader('data/cwe119_cgd.txt', 'cgd')
    ld.txt2list()
    ld.symr_list_praser()
    print(ld.symr_list[0])


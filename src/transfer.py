#!/usr/bin/env python3
#coding: utf-8

import utils
import re


class Transfer:
    def __init__(self, sym_set):
        self._sym_set = sym_set[:]
        self._sym_split_set = []
        self._vec_set = None
        self._word_list = []
        self._str_split()
        self._get_word_list()

    def _str_split(self):
        for sym in self._sym_set:
            tmp = []
            tmp.append(sym[0])
            tmp.append(utils.code_split(sym[1]))
            tmp.append(sym[2])
            self._sym_split_set.append(tmp)

    def _get_word_list(self):
        for i in self._sym_split_set:
            for j in i[1]:
                for k in j:
                    if k not in self._word_list:
                        self._word_list.append(k)


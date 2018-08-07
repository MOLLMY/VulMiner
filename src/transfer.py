#!/usr/bin/env python3
#coding: utf-8

"""
This file transform symbolic to vector
"""

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
        """
        split code into words
        """
        for sym in self._sym_set:
            tmp = []
            tmp.append(sym[0])
            tmp.append([utils.code_split(x) for x in sym[1]])
            tmp.append(sym[2])
            self._sym_split_set.append(tmp)

    def _get_word_list(self):
        """
        collect all words
        """
        for block in self._sym_split_set:
            for code in block[1]:
                for word in code:
                    if word not in self._word_list:
                        self._word_list.append(word)


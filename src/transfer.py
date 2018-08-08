#!/usr/bin/env python3
#coding: utf-8

"""
This file transform symbolic to vector
"""

import utils
import re
import gensim

class Transfer:
    def __init__(self, sym_set):
        self._sym_set = sym_set[:]
        self._sym_split_set = []
        self._vec_set = None
        self._word_list = []
        self._word_record = []
        self._word_curpos = []
        self._sentence_curpos = []
        self._str_split()
        self._get_sentence_curpos()
        self._word_to_vec()

    def _str_split(self):
        """
        split code into words
        """
        for sym in self._sym_set:
            tmp = []
            tmp.append(sym[0])
            tmp.append([list(filter(lambda x: x not in [None, '', ' '], utils.code_split(x)))for x in sym[1]])
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

    def _get_word_curpos(self):
        """
        collect word curpos
        """
        for block in self._sym_split_set:
            rec = []
            rec_len = 0
            rec.append(block[0])
            for code in block[1]:
                cl = list(filter(lambda x: x not in [None, '', ' '], code))
                rec_len += len(cl)
                self._word_curpos += cl
            rec.append(rec_len)
            rec.append(block[2])
            self._word_record.append(rec)

    def _get_sentence_curpos(self):
        for block in self._sym_split_set:
            for code in block[1]:
                self._sentence_curpos.append(code)

    def _word_to_vec(self):
        self.model = gensim.models.Word2Vec(self._sentence_curpos)
        self.model.save('vul.model')
        print(self.model[self._sentence_curpos[0]])

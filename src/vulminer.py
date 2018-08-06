#!/usr/bin/env python3
#coding: utf-8

import sys
import re
from loader import Loader
from preper import Preper
from transfer import Transfer
from trainer import Trainer


class Vulminer:
    def __init__(self):
        self._cgd_set = None
        self._sym_set = None
        self._vec_set = None

    def load(self, file_path):
        loader = Loader(file_path)
        self._cgd_set = loader.get_cgd()

    def prep(self):
        preper = Preper(self._cgd_set)
        self._sym_set = preper.get_symr()

    def trans(self):
        transfer = Transfer(self._sym_set)
        print(len(transfer._word_list))
        #self._vec_set = transfer.get_vec()

    def train(self):
        trainer = Trainer(self._vec_set)
        model = trainer.get_model()

    def test(self):
        pass

if __name__ == '__main__':
    vm = Vulminer()
    vm.load(sys.argv[1])
    vm.prep()
    #with open('sym_list.txt', 'wt') as f:
    #    for i in vm._sym_set:
    #        f.write(i[0] + '\n')
    #        for j in i[1]:
    #            f.write(j + '\n')
    #        f.write(i[2] + '\n')
    #        f.write('\n')
    #with open('cgd_list.txt', 'wt') as f:
    #    for i in vm._cgd_set:
    #        f.write(i[0] + '\n')
    #        for j in i[1]:
    #            f.write(j + '\n')
    #        f.write(i[2] + '\n')
    #        f.write('\n')
    vm.trans()
    #vm.train()
    #vm.test()

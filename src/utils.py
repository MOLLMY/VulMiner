#!/usr/bin/env python3
#coding: utf-8
import re

def code_split(code):
    return list(filter(lambda x: x not in [None, ''], re.split(r'([\s,;\(\)\[\]\*(->)])', code)))

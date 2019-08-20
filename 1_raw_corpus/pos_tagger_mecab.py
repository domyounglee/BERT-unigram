#-*- coding: utf-8 -*-
from konlpy.tag import Mecab
import json
from pprint import pprint
from collections import OrderedDict
mecab = Mecab()
results = OrderedDict()

files = ["wiki_5x.txt", "namuwiki.txt"]


for file in files:

    with open(file) as ft:
        for line in ft:
            try:           
                morphs = mecab.pos(line)
            except :
                continue    
            new_line = " ".join([x[0]+"/"+x[1] for x in morphs])
            print(new_line)
        

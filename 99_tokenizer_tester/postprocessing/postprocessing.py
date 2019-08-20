#-*- coding: utf-8 -*-
from konlpy.tag import Mecab
import json
from pprint import pprint
from collections import OrderedDict
mecab = Mecab()
results = OrderedDict()
with open('./predictions/predictions_unigram.json') as json_file:
    json_data = json.load(json_file)
    for key,value in json_data.items():
        tokens = value.split(' ')
        morphs = mecab.pos(tokens[-1])
        # print(morphs)
        remove_position = len(morphs)
        for morph in reversed(morphs):
            if morph[1].startswith('J') or (morph[1].startswith('ETM') and (morph[0]=='는' or morph[0]=='은' or morph[0]=='이' or morph[0]=='가')):
                remove_position-=1
                continue
            else:
                break
        last = "".join([ x[0] for x in morphs[0:remove_position] ])
        result = " ".join(tokens[0:len(tokens)-1])+" "+last
        result = result.strip()
        # if remove_position != len(morphs):
            # print('value',value,'result',result)
        results[key] = result
print(json.dumps(results))
        

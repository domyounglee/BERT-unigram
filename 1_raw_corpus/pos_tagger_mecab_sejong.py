#-*- coding: utf-8 -*-
from konlpy.tag import Mecab
import json
from pprint import pprint
from collections import OrderedDict
import urllib3
import urllib.parse
import sys
headers={"Content-Type": "application/json; charset=UTF-8"}
http = urllib3.PoolManager()


mecab = Mecab()

results = OrderedDict()

files = ["wiki.txt"]

for line in sys.stdin:
    print(line)
    encode= urllib.parse.quote(line)
    params = {"targetText":line}
    openApiURL = "http://10.100.1.121:8080/api/morpheme/etri?targetText="+encode
    response = http.request(
            "GET",
            openApiURL,
	
            headers=headers
            )
    result = response.data.decode('utf-8')
    print(result)
    try:
        result = json.loads(result)
    except:
        continue
    try :
        morphs = result['sentences'][0]['morp']
        tagged_line = " ".join([x['lemma']+'/'+x['type'] for x in morphs])
        print(tagged_line)
    except:
        continue

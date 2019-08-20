import urllib3 
import urllib.parse
from urllib.parse import urlencode
import json
import pprint
def get_morps(p_json):
    text=''   
    morp_list=[]
    position_list =[]
    text = p_json['text']
    for morp in p_json['morp']:
        morp_list.append(morp['lemma']+'/'+morp['type'])
        position_list.append(int(morp['position']))
    return { 'text': text, 'morp_list':morp_list, 'position_list':position_list }

def do_lang ( text ) : 
    openApiURL = "http://10.100.1.121:8080/api/morpheme/etri"
    http = urllib3.PoolManager()
    print (urlencode({'targetText':text}))
#response = http.request( "POST", openApiURL, body=urlencode({'targetText':text}))
    response = http.request( "POST", openApiURL, fields={'targetText':text})

    return response.data.decode()

def do_lang_ETRI( openapi_key, text ) :
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
    requestJson = { "access_key": openapi_key, "argument": { "text": text, "analysis_code": "morp" } }
    http = urllib3.PoolManager()
    response = http.request( "POST", openApiURL, headers={"Content-Type": "application/json; charset=UTF-8"}, body=json.dumps(requestJson) )
    return response.data.decode()
text= "토트넘 홋스퍼와의 경기결과"
paragraph_text= do_lang(text) 
print(paragraph_text)
print("+++++++++++++++++++++")
ETRI= do_lang_ETRI("8a8b422b-811d-4442-a908-00f78c5f53a0",text)
print(ETRI)
#p_json = json.loads(paragraph_text)['sentences'][0]
#rep_p = get_morps(p_json)
#print(rep_p)



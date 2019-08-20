import sentencepiece as spm
from tokenizer.tokenization_morp import BertTokenizer as tokenization
import urllib3
from urllib.parse import urlencode
import json

def do_lang ( text ) :
    openApiURL = "http://10.100.1.121:8080/api/morpheme/etri?"+urlencode({'targetText':text})
    http = urllib3.PoolManager()
    response = http.request( "GET", openApiURL, headers={"Content-Type": "application/json; charset=UTF-8"})
    
    json_data = json.loads(response.data.decode('utf-8'))
    json_result = json_data["result"]
    if json_result == -1:
        return ""
    else:
        json_data = json.loads(response.data.decode('utf-8'))
        return_result = ""
        json_sentence = json_data["sentences"]
        for json_morp in json_sentence:                        
            for morp in json_morp["morp"]:
                return_result = return_result+str(morp["lemma"])+"/"+str(morp["type"])+" "
        return return_result

text ="""2013년 11월 15일, 방송통신위원회 전체회의에서 의결된 2012년도 방송평가에 따르면 JTBC는 SBS와 MBC를 제치고 지상파 포함 3위를 기록하였으며, 2013년 말 조사한 여론조사에서도 방송 신뢰도가 지상파채널인 MBC와 SBS를 추월했다. 그러나 이러한 지상파급 막대한 투자를 하다보니 과유불급인지 2012년 영업손실은 1397억원으로 종합편성채널과 보도전문편성 사업자들 중 가장 높은 것으로 집계되었다. 그럼에도 제작비가 비교적 적게 드는 시사, 교양 프로에 치중하는 다른 종편사들에 비해 예능, 드라마, 스포츠 같은 다양한 장르에 꾸준히 투자하는 모양새. 종합편성채널이란 원래 취지엔 가장 부합하는 포지션을 취하고 있다."""

morpheme = do_lang(text)
tokenizer = tokenization.from_pretrained('./models/vocab.korean_morp.list', do_lower_case=False)
tokens_a = tokenizer.tokenize(morpheme)
print(tokens_a)
# print("UNIGRAM MODEL \n" , tokenizer.tokenize(text))

# print()

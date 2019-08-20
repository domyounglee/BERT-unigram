import sentencepiece as spm
import tokenizer.tokenization_unigram as tokenization
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

text ="""같은 해 5월 11일의 하코다테 총공격(하코다테 해전)에서 벤텐 다이바와 기관 고장으로 움직일 수 없는 떠 있는 포대가 된 가이텐마루의 원호를 받으며 신정부 군 함대와 응전을 벌인다. 새 정부 군함 초요마루의 화약고에 작렬탄을 명중시켜 초요마루는 대폭발을 일으켜 2분만에 굉침된다. 이것은 구 막부군의 사기를 단번에 향상시켰다. 그후 반류마루는 신정부군의 집중 포화를 맞았다. 응전을 계속했지만, 오후가 되면서 탄약이 완전히 소진되었기 때문에 부득이 퇴함을 결정했고, 벤텐 다이바 아래까지 물러나 얕은 물에 좌초시켰다. 승무원은 기관을 파괴 후 (함장 마쓰오카 바키치가 ‘나중에 사용할 수도 있을 것’이라고 방화를 금지했기 때문에 불태우지는 않음), 벤텐 다이바 근처에 도착, 적지 한 가운데를 가로질러 오다이바로 들어갔다. 이날 신정부군의 손에 반류마루는 방화를 당했지만, 화재는 돛대를 태우는 정도에 그쳤고, 선체는 대부분 타지 않았으며, 그 중간 돛대가 부러지면서 균형을 잃고 전복되면서 진화되었다."""

morpheme = do_lang(text)
tokenizer = tokenization.FullTokenizer('/home/user01/gyun/2_unigram_result/final2.vocab', do_lower_case=False)
#tokenizer = tokenization.FullTokenizer('/home/user01/gyun/2_unigram_result/vocab_base+1+total_nosplit.txt', do_lower_case=False)
tokens_a = tokenizer.tokenize(morpheme)
print(tokens_a)
# print("UNIGRAM MODEL \n" , tokenizer.tokenize(text))

# print()

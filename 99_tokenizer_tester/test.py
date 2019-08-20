import sentencepiece as spm
import tokenization as tokenization
import tokenizer.unigram as unigram
s = spm.SentencePieceProcessor()
s.Load('./models/kor_unigram_news_voc32k.model')
output_tokens = list()
skip_token = False;
text ="""지원 이동통신의 경우, LTE Cat.12·13, LTE Cat.9 그리고 LTE Cat.6 모델이 있다. 우선, 업로드 속도는 Cat.13이 150 Mbps, Cat.9와 Cat.6이 50 Mbps로 최대 속도가 잡혀있고, 다운로드 속도는 Cat.12가 600 Mbps, Cat.9가 450 Mbps 그리고 Cat.6이 300 Mbps로 최대 속도가 잡혀져있다. 3 Band 캐리어 어그리게이션의 경우 상황에 따라 추가적으로 지원하며, VoLTE를 지원한다. 또한, 갤럭시 S7과 같이 모든 기기의 통신 모뎀 솔루션이 모바일 AP에 내장된 최초의 갤럭시 S 시리즈 중 하나이다. 이는 퀄컴 스냅드래곤 시리즈를 탑재한 기존 갤럭시 S 시리즈 스마트폰은 극소수를 제외하면 통신 모뎀 솔루션이 기본적으로 내장되어 있었으나, 삼성 엑시노스 시리즈는 플래그십 AP로는 삼성 엑시노스 8890이 통신 모뎀 솔루션을 내장한 최초의 모바일 AP이기 때문이다."""



#uni_token = unigram.FullTokenizer(model='./models/namu+news_half+wiki.model',vocab_file='./models/namu+news_half+wiki_vocab.txt', do_lower_case=False)
tokenizer = tokenization.FullTokenizer(vocab_file='./models/vocab_unigram.txt', do_lower_case=False)
bert_token = tokenization.FullTokenizer(vocab_file='./models/vocab_bert.txt', do_lower_case=False)
bpe_tokenizer = tokenization.FullTokenizer(vocab_file='../2_unigram_result/final_total_vocab.txt', do_lower_case=False)
# print("UNIGRAM MODEL : \n", output_tokens)
# print()
#print("UNIGRAM MODEL \n" , uni_token.tokenize(text))
print("UNIGRAM FULL MATCHING : \n" , tokenizer.tokenize(text))
print("BERT FULL MATCHING : \n" , bert_token.tokenize(text))
# print()
print("BPE : \n" , bpe_tokenizer.tokenize(text))
# print()
print("INPUT : " ,text)

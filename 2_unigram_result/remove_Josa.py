from konlpy.tag import Mecab
import json 
mecab = Mecab()

def split_it(morphs):
    last_lemma=""
    i=0
    golden_tag = morphs[0][1][0]
    for lemma, tag in morphs:
        
        if tag.startswith(golden_tag):
            i+=1
            last_lemma=lemma
        else:
            break
    #"아버지의" 의 "의"를 NNG로 태그함        
    if last_lemma =="의" and i>1:
        i-=1

    return "".join([morph[0] for morph in morphs[:i]]), "".join([morph[0] for morph in morphs[i:]])

            
        
with open("total_vocab.txt") as f:
    vocab = []
    for word in f:
        hassharp=False
        word = word.strip()
        
        if word.startswith("##"):
            word = word[2:]
            hassharp=True

        #eumjol
        if len(word)==1 or word.startswith("[") or word.startswith("<"):
            vocab.append("##"+word) if  hassharp else vocab.append(word)
            
        else:
            morphs= mecab.pos(word)
            if len(morphs)==1:
                #print(morphs) 
                vocab.append("##"+word) if hassharp else vocab.append(word)
            else:
                #if the first tag is N or VV split it 
                if morphs[0][1].startswith("N") or morphs[0][1].startswith("VV"):
                    word_a, word_b = split_it(morphs)
                    
                    vocab.append("##"+word_a) if hassharp else vocab.append(word_a)
                    vocab.append("##"+word_b)
                
                else:
                    vocab.append("##"+word) if hassharp else vocab.append(word)
for subtok in list(set(vocab)):
    print(subtok) 

#print(mecab.pos("경찰의"))

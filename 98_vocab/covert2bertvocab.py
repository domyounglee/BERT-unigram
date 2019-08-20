fv= open("vocab_ref.txt")
ref = [ line.strip() for line in fv]
f = open("kor_bpe_news_voc32k.vocab")
fw = open("vocab.txt","w")
for tok in ref:
    fw.write(tok+"\\n")
for line in f:
    tok,idx = tuple(line.strip().split("\\t"))
    if tok.startswith("▁"):
        tok = tok[1:]
    else:
        tok = "##"+tok
    if tok in ref:
        continue
    fw.write(tok+"\\n")
fv.close()
f.close()
fw.close()

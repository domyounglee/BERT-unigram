#-*- coding: utf-8 -*-
fv= open("vocab_base+eumjol+ETRIeumjol.txt")
ref = [ line.strip() for line in fv]
f = open("total.vocab")
fw = open("vocab_base+eumjol+ETRIeumjol+unigram32k","w")
unused_number = 102
for tok in ref:
    fw.write(tok+"\n")
for line in f:
    tok,idx = line.strip().split("\t")
    if tok == "▁" or tok == "<s>" or tok == "</s>":
        tok = "[unused"+str(unused_number)+"]"
        unused_number+=1
    elif tok == "<unk>":
        tok = "[UNK]"
    elif tok.startswith("▁"):
        tok = tok[1:]
    else:
        tok = "##"+tok
    if tok in ref:
        continue
    fw.write(tok+"\n")
fv.close()
f.close()
fw.close()

f2 = open("vocab_base+eumjol.txt")
pool = [x.strip() for x in f2]
new_pool = []
with open("vocab_ETRIeumjol.txt") as f:
    for word in f:
        if word in pool or len(word.strip())==0:
            continue
        else:
            new_pool.append(word.strip())
with open("vocab_base+eumjol+ETRIeumjol.txt","w") as fw:
    fw.write("\n".join(pool+new_pool))

f2.close()



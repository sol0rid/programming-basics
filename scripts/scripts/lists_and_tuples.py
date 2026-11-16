seqs = ["ATG", "GGC"]
seqs.append("TTA")
print(len(seqs))
print(seqs[1])
print(seqs[1][0])      # 🤔
print(sorted(seqs))

exon = (300, 450)
start, stop = exon
print(stop - start)
exon[0] = 310          # 🤔 what happens?
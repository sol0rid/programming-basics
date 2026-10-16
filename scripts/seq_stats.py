sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)

print(len(sequences))
sequences.append("GTAGAGT")
seqs_lenght = [len(sequences[0]),len(sequences[1]),len(sequences[2]),len(sequences[3]),len(sequences[4])]
print(seqs_lenght)
print(max(seqs_lenght))
print(min(seqs_lenght))
print(sum(seqs_lenght)/len(sequences))
names = gene[0]
chrom = gene[1]
start = gene[2]
end = gene[3]
lenght = end-start
print(f"BRCA1 is on chr17 and is", lenght, "bases long")
#gene[0] = "124354" # TypeError: 'tuple' object does not support item assignment
genes = [("BRCA1", 81188), ("TP53", 25759)]
print(genes[1][0])

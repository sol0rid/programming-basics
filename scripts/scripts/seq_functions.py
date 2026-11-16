def gc_content(seq):
    gc_count = (seq.count("G") + seq.count("C"))/len(seq)
    return round(gc_count, 2)

def reverse_complement(seq):
    return seq[::-1]

def is_usable(seq, min_lenght = 30):
    if len(seq) >= min_lenght and seq.find("N") == -1:
        return True
    else: 
        return False

seq1 = "CATCATCACGCTACGATCGGGCGCATATATATATTAGAGAGGAGAGAGAGATGATAGATA"
seq2 = "ATGCAC"
seq3 = "GTCAGCTACGGTACGNNACTAGCATNCATTCACTAGC"

print(gc_content(seq3))
print(reverse_complement(seq3))
print(is_usable(seq3))


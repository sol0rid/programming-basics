seq = "CGCGCGCGCGCGGCGCGCGCGGCGCGCGCGCTCATCAGCGTACGACTAGCTACGACGA"

if len(seq) < 30:
    print("too short")

if "N" in seq:
    print("contains unknown bases")

seql = len(seq)
g_count = seq.count("G")
c_count = seq.count("C")
gc = round(((g_count + c_count)/seql)*100, 1)

if gc > 60:
    print("GC rich")
elif gc < 40:
    print("AT rich")
else:
    "balanced"

if seq.startswith("ATG") and len(seq) % 3 == 0:
    print("possible ORF")

seq2 = "ATGATATATATATATATATATAATATATATATTTTATTATCGCGG"

if len(seq2) < 30:
    print("too short")

if "N" in seq2:
    print("contains unknown bases")

seql2 = len(seq2)
g_count2 = seq2.count("G")
c_count2 = seq2.count("C")
gc2 = round(((g_count2 + c_count2)/seql2)*100, 1)

if gc2 > 60:
    print("GC rich")
elif gc2 < 40:
    print("AT rich")
else:
    "balanced"

if seq2.startswith("ATG") and len(seq2) % 3 == 0:
    print("possible ORF")

seq3 = "NATATATATGNGGCG"

if len(seq3) < 30:
    print("too short")

if "N" in seq3:
    print("contains unknown bases")

seql3 = len(seq3)
g_count3 = seq3.count("G")
c_count3 = seq3.count("C")
gc3 = round(((g_count3 + c_count3)/seql3)*100, 1)

if gc3 > 60:
    print("GC rich")
elif gc3 < 40:
    print("AT rich")
else:
    "balanced"

if seq3.startswith("ATG") and len(seq3) % 3 == 0:
    print("possible ORF")
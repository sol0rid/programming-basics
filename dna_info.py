DNA = "ATGCTACGACGTACGTTTAAGCGCGATTAGCAG"
x = len(DNA)
y = DNA.count("G")
z = DNA.count("C")
gc = ((y+z)/x)*100
print("GC:", gc, "%")
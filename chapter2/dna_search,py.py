from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s: str):
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # don't run off end!
            return gene
        #  initialize codon out of three nucleotides
        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)  # add codon to gene
    return gene


my_gene = string_to_gene(gene_str)


def linear_contains(gene, key_codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G) # one of codon example
gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T) # one of codon example
print(linear_contains(my_gene, acg))  # True
print(linear_contains(my_gene, gat))  # False

# this is ordinary linear search where you need to look at each index
# ----------------------------------------------------------------------

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT®"

def string_to_gene(string):
    gene = []
    for i in range(0, len(string), 3):
        if (i + 2) > len(string):
            return gene

        #  initialize codon out of three nucleotides
        codon = (Nucleotide[string[i]], Nucleotide[string[i + 1]], Nucleotide[string[i + 2]])
        gene.append(codon)  # add codon to gene
    return gene


my_gene = string_to_gene(gene_str)
print(my_gene)

def linear_contains(my_gene, key_codon):
    for codon in my_gene:
        if codon == key_codon:
            return True
    return False


acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G) # one of codon example
gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T) # one of codon example
print(linear_contains(my_gene, acg))  # True
print(linear_contains(my_gene, gat))  # False


print(acg in my_gene)
print(my_gene.__contains__(acg))
# # this is ordinary linear search where you need to look at each index
# # ----------------------------------------------------------------------

def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low < high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True

    return False



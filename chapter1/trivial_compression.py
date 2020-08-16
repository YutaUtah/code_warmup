class CompressedGene(object):
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # let bit_string be 2 shinsu
            if nucleotide == 'A': # bottom 2 bits to be 00
                self.bit_string |= 0b00
            elif nucleotide == 'C': # bottom 2 bits to be 01
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10 # bottom 2 bits to be 10
            elif nucleotide == 'T':
                self.bit_string |= 0b11 # bottom 2 bits to be 11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] reverses string by slicing backwards

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


# _compress() function turns str to bit sequence. if you have underbar, it means its a private function
# meaning that it cannot be called outside of class

if __name__ == "__main__":
    from sys import getsizeof
    original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
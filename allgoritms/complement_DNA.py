# it is onw code wars challenge 
# the challenge is :
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G"
# Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side
# DNA strand is never empty or there is no DNA at all
#


def complement_DNA(dna_strand):

    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    complementary_strand = ''.join(complement_dict[n] for n in dna_strand)

    return complementary_strand


input_strand1 = "ATTGC"
input_strand2 = "GTAT"

output_strand1 = complement_DNA(input_strand1)
output_strand2 = complement_DNA(input_strand2)

print(f'"{input_strand1}" --> "{output_strand1}"')
print(f'"{input_strand2}" --> "{output_strand2}"')
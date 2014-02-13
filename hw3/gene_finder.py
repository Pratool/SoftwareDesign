# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Pratool Gadtaula
"""
# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from load import load_seq
import random

dna = load_seq("data/X73525.fa")

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents a protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    translations = ''
    for i in range(len(dna)/3): # does not return last codon if less than 3 bases
        for j in range(len(codons)):
            for k in range(len(codons[j])):
                if (codons[j][k]) == (dna[3*i:(3*i)+3]):
                    translations = translations + aa[j]
    
    return translations

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    print 'input: ATGCGA, expected output: MR, actual output: ',
    print coding_strand_to_AA("ATGCGA")
    print 'input: ATGCCCGCTTT, expected output: MPA, actual output: ',
    print coding_strand_to_AA("ATGCCCGCTTT")

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    reverse = ''
    complements = ''
    for i in range(len(dna)):
        reverse = reverse + dna[(len(dna)-1)-i]
    for i in range(len(dna)):
        if reverse[i] == 'A':
            complements = complements + 'T'
        elif reverse[i] == 'T':
            complements = complements + 'A'
        elif reverse[i] == 'C':
            complements = complements + 'G'
        elif reverse[i] == 'G':
            complements = complements + 'C'
            
    return complements

def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    print 'input: ATGCCCGCTTT, expected output: AAAGCGGGCAT, actual output:',
    print get_reverse_complement("ATGCCCGCTTT")
    print 'input: CCGCGTTCA, expected output: TGAACGCGG, actual output:',
    print get_reverse_complement("CCGCGTTCA")

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    if ('TAG' in dna):
        return dna[0:dna.find('TAG')]
    elif ('TAA' in dna):
        return dna[0:dna.find('TAA')]
    elif ('TGA' in dna):
        return dna[0:dna.find('TGA')]
    
    return dna

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    print 'input: ATGTGAA, expected output: ATG, actual output:',
    print rest_of_ORF('ATGTGAA')
    print 'input: ATGAGATAGG, expected output: ATGAGA, actual output:',
    print rest_of_ORF('ATGAGATAGG')

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORFs = []
    index = dna.find('ATG')
    next_index = 0
    while index != -1 and next_index < len(dna):
        if index % 3 == 0:
            new_dna = rest_of_ORF(dna[index:len(dna)])
            next_index = index + len(new_dna)+3
            ORFs.append(new_dna)
            index = dna.find('ATG', next_index)
        else:
            next_index = next_index + 1
            index = dna.find('ATG', next_index)
    return ORFs
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    print find_all_ORFs_oneframe('ATGGAATAGATGTAG')
    print find_all_ORFs_oneframe('ATAGTAGATAGTAGTAGTAGATGTGCTAG')
    print find_all_ORFs_oneframe('TAGTAGATGTAGATGCCCGCCATGTAG')
    print find_all_ORFs_oneframe('ATGCATGAATGTAGATAGATGTGCCC')

#find_all_ORFs_oneframe_unit_tests()

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_ORFs = find_all_ORFs_oneframe(dna) + find_all_ORFs_oneframe(dna[1:(len(dna))]) + find_all_ORFs_oneframe(dna[2:(len(dna))])
    return all_ORFs

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    print find_all_ORFs("ATGCATGAATGTAG")

#find_all_ORFs_unit_tests()

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")

#find_all_ORFs_both_strands_unit_tests()

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    all_strands = find_all_ORFs_both_strands(dna)
    i = 0
    longest = ''
    for i in range(len(all_strands)):
        if len(all_strands[i]) > len(longest):
            longest = all_strands[i]
    return longest

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    print longest_ORF("ATGCGAATGTAGCATCAAA")

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    DNA = list(dna)
    longest = len(longest_ORF(collapse(DNA)))
    i = 0
    for i in range(num_trials):
        random.shuffle(DNA)
        if  len(longest_ORF(collapse(DNA))) > longest:
            longest = len(longest_ORF(collapse(DNA)))
    return longest

#init = ['A', 'T', 'C', 'G', 'A', 'T', 'G', 'A', 'A', 'A', 'T', 'A', 'G']
#random.shuffle(init)
#print init

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    all_DNA = find_all_ORFs_both_strands(dna)
    longest = []
    for i in range(len(all_DNA)):
        if len(all_DNA[i]) > threshold:
            longest.append(coding_strand_to_AA(all_DNA[i]))
    return longest

#print longest_ORF_noncoding(dna, 1500)
print gene_finder(dna, 500)
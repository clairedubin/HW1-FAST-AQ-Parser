# write tests for parsers
import sys
import re


from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    f = FastaParser('data/test.fa')

    for record in f:
        assert len(record) == 2, "The parsed FASTA does not consist of 2 elements."
        assert isinstance(record[0], str), "The header is not a string"
        assert isinstance(record[1], str), "The sequence is not a string"
        assert re.match('^[a-zA-Z/-]+$',record[1]),  "The sequence contains non-alphabetic characters (gaps are also allowed)."



def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    f = FastqParser('data/test.fq')

    for record in f:
        assert len(record) == 3, "The parsed FASTQ does not consist of 3 elements."
        assert isinstance(record[0], str), "The header is not a string"
        assert isinstance(record[1], str), "The sequence is not a string"
        assert isinstance(record[2], str), "The quality line is not a string"
        assert re.match('^[a-zA-Z/-]+$',record[1]), "The sequence contains non-alphabetic characters (gaps are also allowed)."

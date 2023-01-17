# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """

    test_seq = 'ACTGCTAGGAT'
    correct_transcribed_seq = 'UGACGAUCCUA'
    transcribed_seq = transcribe(test_seq)

    assert 'T' not in transcribed_seq
    assert transcribed_seq == correct_transcribed_seq


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    test_seq = 'ACTGCTAGGAT'
    correct_rev_transcribed_seq = 'AUCCUAGCAGU'

    rev_transcribed_seq = reverse_transcribe(test_seq)

    assert 'T'  not in rev_transcribed_seq
    assert rev_transcribed_seq == correct_rev_transcribed_seq
# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    rna = {"A":"U", "C":"G", "T":"A", "G":"C"}
    return ''.join([rna.get(dna) for dna in seq])


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq)[::-1]

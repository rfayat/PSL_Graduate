"Functions for computing substitution matrices from sequences"
import pandas as pd
import numpy as np
AMINO_ACIDS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
               'Q', 'R', 'S', 'T', 'V', 'W', 'Y']


def empty_substitution_matrix(dtype=int):
    "Return a dataframe filled with zeros whose rows and cols are the amino-acids"
    values = np.zeros((len(AMINO_ACIDS), len(AMINO_ACIDS)), dtype=dtype)
    substitution_matrix = pd.DataFrame(values,
                                       index=AMINO_ACIDS,
                                       columns=AMINO_ACIDS)
    return substitution_matrix


def compute_substitution_count(sequence_1, sequence_2):
    """Compute a substition matrix from to array-like objects
    
    Parameters
    ----------
    sequence_1, sequence_2: array-like
        The amino-acid sequences that will be compared.
    
    Returns
    -------
    substitution_count, dataframe
        A pandas DataFrame with rows corresponding to the amino-acids in
        sequence_1, the columns corresponding to the amino-acids in sequence_2
        and the values corresponding to the count of substitions.
    """
    substitution_count = empty_substitution_matrix()
    # Loop over each pair of aligned amino-acids
    for aa_1, aa_2 in zip(sequence_1, sequence_2):
        substitution_count.loc[aa_1, aa_2] += 1
    
    return substitution_count


def compute_substition_matrix(sequence_1_all, sequence_2_all):
    """Compute a substitution matrix for two sets of sequences
    
    Parameters
    ----------
    sequence_1_all, sequence_2_all: iterable
        Lists of amino-acids sequences. Each amino-acid sequence must be
        stored as an array-like object.
    """
    substitution_matrix = empty_substitution_matrix()
    # Loop over each pair of sequence
    for sequence_1 in sequence_1_all:
        for sequence_2 in sequence_2_all:
            # Compute the substitution count for one pair and add it to the matrix
            substitution_matrix += compute_substitution_count(sequence_1, sequence_2)
    return substitution_matrix
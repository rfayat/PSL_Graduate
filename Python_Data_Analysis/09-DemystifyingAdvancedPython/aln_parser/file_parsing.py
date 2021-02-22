"Helper functions for reading aln files"
import pandas as pd
import numpy as np
import re
from .utils import convert_first_arg_to_path


def read_aln_row(row):
    """Parse a row of an aln file and return its content.
    
    If the row does not contain any data, None is returned.
    
    Parameters
    ----------
    row: str
        A row of an aln file.
        
    Returns
    -------
    parsed_row: dict or None
        A dictionary containing the parsed data.
        The dictionary has format:
        
            {"organism_id": organism_id,
             "sequence": sequence,
              "end_position": end_position}
              
        Where organism_id, sequence and end_position correspond to:
        
        organism_id: int
            The organism ID.

        sequence: str
            The protein sequence stored on the row.

        end_position: int
            The position of the last amino-acid of the row.
    """
    pattern = "(?P<organism_id>^\d+)\s+(?P<sequence>[A-Z]+)\s+(?P<end_position>\d+)\n$"
    match = re.search(pattern, row)
    # If we get a match, return the id, sequence and end_postion
    if match is not None:
        parsed_row = match.groupdict()
        # conversion of organism_id and end_position to integers
        parsed_row["organism_id"] = int(parsed_row["organism_id"])
        parsed_row["end_position"] = int(parsed_row["end_position"])
        # Return the parsed row
        return parsed_row
    # Otherwise, return None
    else:
        return None


@convert_first_arg_to_path
def read_text_file(path):
    """Return the rows of a text file as elements of a list
    
    Parameters
    ----------
    path: Path
        The path to the text file to read
    
    Returns
    -------
    list of str
        A list containing the text file's rows.
    """
    # Open the file and return its content
    with path.open("r") as f:
        rows = f.readlines()
    return rows


def load_aln_data(path):
    """Load an aln file as a pandas dataframe
    
    Parameters
    ----------
    path: Path
        The path to the data file.
        
    Returns
    -------
    df: pd.DataFrame
        The aligned sequences stored in a dataframe.
        Each row correspond to a position in the sequence,
        each column to an organism ID.
    """
    # Open the file whose path is given as input and read its content
    row_all = read_text_file(path)
    
    # Parse each row and store those containing data in a list
    parsed_row_all = []
    for row in row_all:
        parsed_row = read_aln_row(row)
        if parsed_row is not None:
            parsed_row_all.append(parsed_row)

    # Find the maximum value of end position and all organism IDs
    end_position_max = -1
    organism_id_all = []
    for parsed_row in parsed_row_all:
        if parsed_row["end_position"] > end_position_max:
            end_position_max = parsed_row["end_position"]
        if parsed_row["organism_id"] not in organism_id_all:
            organism_id_all.append(parsed_row["organism_id"])
            
    # Preallocate the output dataframe
    df = pd.DataFrame(index=np.arange(1, end_position_max + 1),
                      columns=organism_id_all, dtype=str)
    
    # Parse the content of each row and store it in df
    for parsed_row in parsed_row_all:
        end_position = parsed_row["end_position"]
        start_position = end_position - len(parsed_row["sequence"]) + 1
        
        # Convert the sequence from a str to a list where each element is an AA
        sequence_as_list = [amino_acid for amino_acid in parsed_row["sequence"]]
        
        # Store the sequence in df
        df.loc[start_position:end_position, parsed_row["organism_id"]] = sequence_as_list
    return df
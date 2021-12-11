import os, glob
import numpy as np


def _get_read_files(data_dir, barcode_fastq_name):

    """
    Parameters:
    -----------
    data_dir
        directory of poolQ inputs
        type: str
    bc
        string indicator in filename of which fastq contains the barcodes
        type: str
    Returns:
    --------
    col_reads, row_reads
    Notes:
    ------
    (1) list comprehension setup should scale to future, multi-pool analyses.
    """
    
    fastq_matches = np.array(glob.glob(os.path.join(data_dir, "*.fastq.gz")))
    out = np.array([i for i, v in enumerate(fastq_matches) if bc in v])

    col_reads = barcode = fastq_matches[out][0]  # barcode
    row_reads = read_fq = fastq_matches[~out][0]  # read_fq

    return col_reads, row_reads

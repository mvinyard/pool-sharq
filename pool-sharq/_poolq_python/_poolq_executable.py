import os
import licorice

def _poolq_executable(
    data_dir,
    barcode_filename,
    conditions_filename,
    java_path,
    barcode_indicator,
    dry_run,
    run_name,
):

    """
    Execute poolQ commands.
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

    col_reads, row_reads = _get_read_files(data_dir, barcode_indicator)
    barcodes = os.path.join(data_dir, barcode_filename)
    conditions = os.path.join(data_dir, conditions_filename)

    executable = " ".join(
        [
            "bash",
            java_path,
            "--row-reference {}".format(barcodes),
            "--col-reference {}".format(conditions),
            "--row-reads {}".format(row_reads),
            "--col-reads {}".format(col_reads),
            "--row-barcode-policy PREFIX:CACCG@12 --col-barcode-policy FIXED:0",
        ]
    )

    formatted_runtitle = licorice.font_format("Run name: {}".format(run_name), ["BOLD", "RED"])
    licorice.underline("Run name: {}".format(run_name))
    licorice.underline("PoolQ executable:", ['BOLD', 'CYAN'])
    licorice.underline("executable", ['BOLD', 'CYAN'])
    
    if dry_run:
        print(
            licorice.font_format(
                "\nDry run complete. Please inspect PoolQ executable.", ["BOLD"]
            )
        )
    else:
        os.system(executable)

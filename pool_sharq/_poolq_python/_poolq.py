
from ._poolq_executable import _poolq_executable

class _poolq:

    def __init__(self,
        data_dir=False,
        metadata=False,
        outpath=False,        
    ):

        self.data_dir = data_dir
        barcode_indicator="barcode",
        barcode_filename="rows.txt",
        conditions_filename="column.txt",
        self.standard_PoolQ_outfiles = standard_PoolQ_outfiles=[
          "barcode-counts.txt",
          "correlation.txt",
          "counts.txt",
          "lognormalized-counts.txt",
          "poolq3.log",
          "quality.txt",
          "runinfo.txt",
          "unexpected-sequences.txt",
        ],
      
    def run(
        self,
        data_dir=False,
        run_name=False,
        dry_run=False,
        barcode_filename=False,
        conditions_filename=False,
        barcode_indicator=False,
        outpath=False,
    ):
        if not run_name:
            self.run_name = "run_{}".format(
                "".join(np.random.choice(list(string.ascii_lowercase), 6))
            )
        else:
            self.run_name = run_name

        if data_dir:
            self.data_dir = data_dir
        if barcode_filename:
            self.barcode_filename = barcode_filename
        if conditions_filename:
            self.conditions_filename = conditions_filename
        if barcode_indicator:
            self.barcode_indicator = barcode_indicator
        if outpath:
            self.outpath = outpath

        _poolq_executable(
            self.data_dir,
            self.barcode_filename,
            self.conditions_filename,
            poolq_path,
            self.barcode_indicator,
            dry_run,
            self.run_name,
        )

        if not dry_run:
            self.outs = _organize_PoolQ_outputs(
                self.run_name,
                self.standard_PoolQ_outfiles,
                self.outpath,
                fetch_only=False,
            )
            self.ResultsDict = _make_results_dict(self.outs)
    
    
    def parse(self,
            run_name=False,
            standard_PoolQ_outfiles=False,
            outpath=False,
            fetch_only=False,):

        if run_name:
                self.run_name = run_name

        if standard_PoolQ_outfiles:
            self.standard_PoolQ_outfiles = standard_PoolQ_outfiles

        if outpath:
            self.outpath = outpath

        self.outs = _organize_PoolQ_outputs(
            self.run_name, self.standard_PoolQ_outfiles, self.outpath, fetch_only
        )
        self.ResultsDict = _make_results_dict(self.outs)

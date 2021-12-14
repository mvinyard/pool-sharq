
import licorice
import os


from ._build_poolq_shell_executable import _build_poolq_shell_executable


def _run_poolq(poolq_path,
               barcode_file,
               condition_file,
               barcode_reads,
               condition_reads,
               verbose):

    executable = _build_poolq_shell_executable(poolq_path,
                                               barcode_file,
                                               condition_file,
                                               barcode_reads,
                                               condition_reads,)
    
    licorice.underline("PoolQ executable:", ['BOLD', 'CYAN'])
    
    printable_executable = executable.split("--")
    
    for n, line in enumerate(printable_executable):
        if n == 0:
            print(line)
        elif n == (len(printable_executable)-1):
            print("\t--{}\n".format(line))
        else:
            print("\t--{} \ ".format(line))
            
    os.system(executable)
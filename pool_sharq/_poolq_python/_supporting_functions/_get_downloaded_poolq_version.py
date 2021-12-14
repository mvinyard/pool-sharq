
import glob, os
import pyrequisites as pyrex


def _get_downloaded_poolq_version():
    
    """"""
    
    package_path  = pyrex.parent_dir(__file__, levels=3)
    poolq_distribution_dir = glob.glob(os.path.join(package_path, "_distribution/*"))[0] 
    poolq_version = poolq_distribution_dir.split('-')[-1]
    poolq_path = os.path.join(poolq_distribution_dir, "poolq3.sh")
    
    return poolq_version, poolq_path
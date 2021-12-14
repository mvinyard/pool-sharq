
import os
from .._fetch._poolq_downloader import _poolq_downloader

def _download_test_data():
    
    """"""
    
    
    _poolq_download_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_tests/")
    
    if os.path.exists(os.path.join(_poolq_download_path, "barcode-counts.txt")):
        pass
    else:
        get_pq = _poolq_downloader()
        get_pq.fetch_available(verbose=False)
        print("\nDownloading...")
        get_pq.download_tests(_poolq_download_path)
# __init__.py

from ._fetch._poolq_downloader import _look_for_poolq
from ._fetch._download_test_data import _download_test_data as download_test_data

from ._poolq_python._poolq_module import _poolq as poolq

_look_for_poolq(__file__)
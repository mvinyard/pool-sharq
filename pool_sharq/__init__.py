# __init__.py

from ._fetch._poolq_downloader import _look_for_poolq
from ._poolq_python._poolq import _poolq as poolq


_look_for_poolq(__file__)
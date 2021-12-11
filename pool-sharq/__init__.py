# __init__.py

from ._fetch._poolq_downloader import _look_for_poolq

_look_for_poolq(path=__module__.__path__)

from _poolq_python._poolq import _poolq as poolq

import os
import sys

from minecraft_data.tools import convert, commondata
from minecraft_data.data import SUPPORTED_VERSIONS, get_data_path


class mod(sys.modules[__name__].__class__):
    def __call__(self, version, edition="pc"):
        # First try to use lazy-loaded data from Pooch
        try:
            _dir = get_data_path(version)
        except ValueError:
            # Fallback to bundled data if version not supported by Pooch
            _dir = os.path.join(os.path.dirname(__file__), "data/data/")

        return type(version, (object,), convert(_dir, version, edition))

    def common(self, edition="pc"):
        # Common data is version-independent; reuse any supported version's data root
        _dir = get_data_path(SUPPORTED_VERSIONS[0])
        return type("common", (object,), commondata(_dir, edition))


sys.modules[__name__].__class__ = mod

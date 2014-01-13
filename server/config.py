import os
import sys

envkeys = []
this_module = sys.modules[__name__]
for key in envkeys:
    setattr(this_module, key, os.environ.get(key, None))

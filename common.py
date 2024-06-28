"""
common.py: a program to import the entire content of the general course-specific python file to help with building the documentation.
The docs are built in such a way that dealing with directories outside of ./ is difficult, so it is easier to do things like this. 

Much of the structure here goes against standard conventions and recommendations, so I would not suggest reusing this code outside of the purpose of passing through
"""

import importlib.util
import sys

# Define the path to the mkatomic.py file
module_path = './code/mkatomic.py'

# Load the module
spec = importlib.util.spec_from_file_location("mkatomic", module_path)
mkatomic = importlib.util.module_from_spec(spec)
sys.modules["mkatomic"] = mkatomic
spec.loader.exec_module(mkatomic)

# Update the current global namespace with names from the module
globals().update(vars(mkatomic))

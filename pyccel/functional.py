"""
This file contains functions and classes needed for the functional programing
feature of Pyccel.
"""

# TODO: THIS IS STILL EXPERIMENTAL

import operator

#==============================================================================
class Where(dict):
    pass

#==============================================================================
class AnyArgument(object):
    """a class representing any argument."""
    pass

#==============================================================================
# user friendly
_ = AnyArgument()
where = Where
add = operator.add
mul = operator.add
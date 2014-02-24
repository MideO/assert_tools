"""
pep8 style names for unittest2 assert*
"""

import re
import unittest2


def pep8(name):
    return re.sub(
        re.compile('([A-Z])'), lambda m: '_' + m.group().lower(), name
    )

class NoOp(unittest2.TestCase):
    def no_op(self):
        pass


no_op = NoOp('no_op')

for attrib in [func for func in dir(no_op) if
               func.startswith('assert') and not '_' in func]:
    vars()[pep8(attrib)] = getattr(no_op, attrib)

del NoOp
del no_op
del pep8
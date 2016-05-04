#!/usr/bin/env python
# coding: utf-8
"""
Script to write GW Input for VASP and ABINIT / set up work flows.
"""
from __future__ import unicode_literals, division, print_function, absolute_import

__author__ = "Michiel van Setten"
__copyright__ = " "
__version__ = "0.9"
__maintainer__ = "Michiel van Setten"
__email__ = "mjvansetten@gmail.com"
__date__ = "May 2014"

import os
import sys
import os.path

from abipy.gw.datastructures import get_spec

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


def main(update=True):
    """
    main gw setup
    """
    try:
        spec_in = get_spec('GW')
    except None:
        return 1

    try:
        spec_in.read_from_file('spec.in')
    except (IOError, OSError):
        try:
            spec_in.read_from_file('$HOME/.abinit/abipy/spec.in')
        except (IOError, OSError):
            pass
        pass

    if update:
        # in testing mode there should not be interactive updating
        spec_in.update_interactive()

    try:
        spec_in.test()
        spec_in.write_to_file('spec.in')
        spec_in.loop_structures('i')
        return 0
    except None:
        return 2

if __name__ == "__main__":
    sys.exit(main())

"""
DUNE plot style - matplotlib interface

Provides matplotlib style file and utility functions for use with matplotlib.
"""

try:
    # this handles the arrangement that comes out
    #  when dune-plot-style is set up standalone by using `pip install`.
    # (the UPS product sets $MPLCONFIGDIR directly in its setup process.)
    import os, os.path, pathlib
    import dunestyle.stylelib as module
    import matplotlib
    os.environ["MPLCONFIGDIR"] = str(pathlib.Path(module.__path__[0]).parent.absolute())+"/stylelib/" + (":" + os.environ["MPLCONFIGDIR"] if "MPLCONFIGDIR" in os.environ else "")
except:
    pass

from .dunestyle import *

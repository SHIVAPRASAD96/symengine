from .lib.csympy_wrapper import (Symbol, Integer, sympify, SympifyError, Add,
        Mul, Pow, sin, cos, sqrt, function_symbol, I)
from .utilities import var

def test():
    import pytest, os
    return not pytest.cmdline.main(
        [os.path.dirname(os.path.abspath(__file__))])

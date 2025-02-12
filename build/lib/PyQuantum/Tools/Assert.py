# ---------------------------------------------------------------------------------------------------------------------
# sys
import sys
# ---------------------------------------------------------------------------------------------------------------------
# inspect
from inspect import getframeinfo
# ---------------------------------------------------------------------------------------------------------------------
# PyQuantum.Tools
from PyQuantum.Tools.Print import print
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
def FILE():
    cf = sys._getframe(1)

    return getframeinfo(cf).filename


def LINE():
    cf = sys._getframe(1)

    return cf.f_lineno
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
def print_error(err_msg, file, line):
    print("Error: ", color="red")
    print(err_msg)

    print()

    print("File: ", color="yellow")
    print("\"" + file + "\"")

    print("Line: ", color="yellow")
    print(line)

    print()
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
def Assert(condition, err_msg, file, line):
    if not condition:
        print_error(err_msg, file, line)
        exit(1)
# ---------------------------------------------------------------------------------------------------------------------


# =====================================================================================================================
# Example: Assert(1 == 2, "1 != 2", FILE(), LINE())
# =====================================================================================================================

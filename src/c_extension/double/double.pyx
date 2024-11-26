cdef extern from "double_extension.h":
    int double_value(int x)

def double(int x):
    return double_value(x)

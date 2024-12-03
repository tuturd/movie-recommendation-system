cdef extern from "double_extension.h":
    int double_value(int x)
    void execute_sql_query(char* db_directory, char* pseudo)

def double(int x):
    return double_value(x)

def execute_sql(bytes db_directory, bytes pseudo):
    execute_sql_query(<char*>db_directory, <char*>pseudo)
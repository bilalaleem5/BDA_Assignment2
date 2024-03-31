#Reducer for Query Vectorization:

#!/usr/bin/env python3
import sys

def reducer_query_vectorization():
    query_vector = eval(sys.argv[1])  # Assuming the query vector is passed as a command-line argument
    print(query_vector)

if _name_ == "_main_":
    reducer_query_vectorization()

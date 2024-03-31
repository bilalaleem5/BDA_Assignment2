#Mapper for Query Vectorization:

#!/usr/bin/env python3
import sys

def mapper_query_vectorization():
    
    query_vector = {}
    for line in sys.stdin:
        term, count = line.strip().split('\t')
        query_vector[term] = int(count)
    
    print(query_vector)

if _name_ == "_main_":
    mapper_query_vectorization()


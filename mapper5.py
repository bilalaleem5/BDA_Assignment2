#Mapper for Query Processing:

#!/usr/bin/env python3
import sys

def mapper_query_processing():
    query = sys.argv[1]  # Assuming the query is passed as a command-line argument
    query_terms = query.lower().split()
    for term in query_terms:
        print(f"{term}\t1")

if _name_ == "_main_":
    mapper_query_processing()


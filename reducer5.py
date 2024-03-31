#reducer for Query Processing:

#!/usr/bin/env python3
import sys

def reducer_query_processing():
    query_term_counts = {}
    
    for line in sys.stdin:
        term, count = line.strip().split('\t')
        query_term_counts[term] = int(count)
    
    print(query_term_counts)

if _name_ == "_main_":
    reducer_query_processing()


#Reducer for Vocabulary:

#!/usr/bin/env python3
import sys

def reducer_vocabulary():
    current_term = None
    term_count = 0
    
    for line in sys.stdin:
        term, _ = line.strip().split('\t')
        
        if current_term == term:
            term_count += 1
        else:
            if current_term:
                print(f"{current_term}\t{term_count}")
            current_term = term
            term_count = 1
    
    if current_term:
        print(f"{current_term}\t{term_count}")

if _name_ == "_main_":
    reducer_vocabulary()

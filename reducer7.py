Reducer for Document Identification:

#!/usr/bin/env python3
import sys

def reducer_document_identification():
    current_document_id = None
    word_counts = {}
    
    for line in sys.stdin:
        document_id, term_count = line.strip().split('\t')
        term, term_frequency = term_count.split(':')
        
        if current_document_id == document_id:
            word_counts[term] = int(term_frequency)
        else:
            if current_document_id:
                print(f"{current_document_id}\t{word_counts}")
            current_document_id = document_id
            word_counts = {term: int(term_frequency)}
    
    if current_document_id:
        print(f"{current_document_id}\t{word_counts}")

if _name_ == "_main_":
    reducer_document_identification()


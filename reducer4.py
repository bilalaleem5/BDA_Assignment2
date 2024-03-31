#Reducer for TF/IDF Model:

#!/usr/bin/env python3
import sys

def reducer_tf_idf():
    current_term = None
    document_info = {}
    
    for line in sys.stdin:
        term, doc_info = line.strip().split('\t')
        doc_id, term_frequency, document_frequency = doc_info.split(':')
        
        if current_term == term:
            document_info[doc_id] = (term_frequency, document_frequency)
        else:
            if current_term:
                print(f"{current_term}\t{document_info}")
            current_term = term
            document_info = {doc_id: (term_frequency, document_frequency)}
    
    if current_term:
        print(f"{current_term}\t{document_info}")

if _name_ == "_main_":
    reducer_tf_idf()

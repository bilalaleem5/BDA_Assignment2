#!/usr/bin/env python3
import sys

def reducer_word_indexing():
    current_term = None
    document_tfidf_weights = {}
    
    for line in sys.stdin:
        term, doc_weight_pair = line.strip().split('\t')
        doc_id, tfidf_weight = doc_weight_pair.split(':')
        
        if current_term == term:
            document_tfidf_weights[doc_id] = tfidf_weight
        else:
            if current_term:
                print(f"{current_term}\t{document_tfidf_weights}")
            current_term = term
            document_tfidf_weights = {doc_id: tfidf_weight}
    
    if current_term:
        print(f"{current_term}\t{document_tfidf_weights}")

if __name__ == "__main__":
    reducer_word_indexing()



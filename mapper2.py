#!/usr/bin/env python3
import sys

def mapper_word_indexing():
    for line in sys.stdin:
        term, document_id, tfidf_weight = line.strip().split('\t')
        print(f"{term}\t{document_id}:{tfidf_weight}")

if __name__ == "__main__":
    mapper_word_indexing()


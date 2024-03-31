#Mapper for TF/IDF Model:

#!/usr/bin/env python3
import sys

def mapper_tf_idf():
    for line in sys.stdin:
        document_id, term, term_frequency, document_frequency = line.strip().split('\t')
        print(f"{term}\t{document_id}:{term_frequency}:{document_frequency}")

if _name_ == "_main_":
    mapper_tf_idf()


Mapper for Document Identification:

#!/usr/bin/env python3
import sys

def mapper_document_identification():
    for line in sys.stdin:
        document_id, term, term_frequency = line.strip().split('\t')
        print(f"{document_id}\t{term}:{term_frequency}")

if _name_ == "_main_":
    mapper_document_identification()

#Mapper for Vocabulary:

#!/usr/bin/env python3
import sys

def mapper_vocabulary():
    for line in sys.stdin:
        term, _ = line.strip().split('\t')
        print(f"{term}\t1")

if _name_ == "_main_":
    mapper_vocabulary()

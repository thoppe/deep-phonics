import numpy as np
import random

keep = []

f_dict = "6of12.txt"
with open(f_dict) as FIN:
    for line in FIN:
        line = line.strip()

        # unmarked abbreviation
        if ":" in line: continue

        # designation
        if "." in line: continue

        # Phrases
        if " " in line or "/" in line:
            continue

        # Non-english usage
        if "&" in line:
            continue

        # Hyphanted words
        if "-" in line:
            continue

        # Proper noun or ABBR
        if line!=line.lower(): continue

        # "signature word", keep
        if "+" in line:
            line = line.replace('+','')

        # "second-class word", keep
        if "=" in line:
            line = line.replace('=','')

        # common spelling variant
        if "^" in line:
            line = line.replace('^','')
            
        # less-common spelling variant
        if "#" in line:
            line = line.replace('#','')

        # less-common spelling variant
        if "~" in line:
            line = line.replace('~','')
            
        # less-common spelling variant
        if "<" in line:
            line = line.replace('<','')

        # Remove apostrophes
        if "'" in line:
            line = line.replace("'",'')
        
        if line.isalpha() and line==line.lower():
            keep.append(line)
            continue
        
def line_iterator(W,words_per_line=10):
    random.shuffle(W)

    overflow = len(W) % words_per_line
    if overflow:
        W = W[:-overflow]
    
    #W = np.array(W)[:-(len(W)%words_per_line)]
    W = np.array(W)

    for line in np.split(W,len(W)//words_per_line):
        yield ' '.join(line)

for repeat in range(4):
    for line in line_iterator(keep):
        print line

        

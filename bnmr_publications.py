# formatted using black

import os,glob
import numpy as np
import matplotlib.pyplot as plt
from bibliography import bib_collection


# types of entries in bnmr publications list
# ~ kinds = ("article", "preprint", "proceeding", "thesis")

# read bib files
data_dir = 'data'

all_files = glob.glob(data_dir+'/*.bib')
kinds = [os.path.splitext(os.path.basename(f))[0] for f in all_files]
publications = [bib_collection(f) for f in all_files]

# sort by year, reverse chronological order
keys = [b.sort_keys('year','month',ascending=(False,False)) for b in publications]

# write the sorted/formatted publication lists to files
for k,pub in zip(kinds,publications):
    lines = ['<ol reversed id="publications">']
    
    for entry in pub.data:
        lines.append("<li>")
        lines.append(pub.data[entry].format())
        lines.append("</li>")
    lines.append("</ol>")
    
    with open("_html/%s.html"%k, "w") as fid:
        fid.write('\n'.join(lines))

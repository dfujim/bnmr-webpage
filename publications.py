# formatted using black

import os,glob
import numpy as np
import matplotlib.pyplot as plt
from bibliography import bib_collection

# source directory
data_dir = 'data'
out_dir = '_html'

# make out directory 
if not os.path.isdir(out_dir):   
    os.makedirs(out_dir)

# read bib files
all_files = glob.glob(data_dir+'/*.bib')
kinds = [os.path.splitext(os.path.basename(f))[0] for f in all_files]
publications = [bib_collection(f,os.path.join(data_dir,'bibnotes.csv')) for f in all_files]

# sort by year, reverse chronological order
keys = [b.sort_keys('year','month',ascending=(False,False)) for b in publications]

# write the sorted/formatted publication lists to files
for kind,pub,key in zip(kinds,publications,keys):
    lines = ['<ol reversed id="publications">']
    
    for entry in key:
        lines.append("<li>")
        lines.append(pub.data[entry].format(kind))
        lines.append("</li>")
    lines.append("</ol>")
    
    with open(out_dir+"/%s.html"%kind, "w") as fid:
        fid.write('\n'.join(lines))

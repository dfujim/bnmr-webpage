# Get bibtex object referece by field. Search files
# Derek Fujimoto
# May 2019

from bibliography import *

# ~ from bnmr_proceedings import proceedings as biblist
# ~ from bnmr_preprints import preprints as biblist
# ~ from bnmr_theses import theses as biblist
from bnmr_articles import articles as biblist


filenames = ['article','news','proceeding','thesis','unpublished']
filenames = ['data/'+f+'.bib' for f in filenames]
collection = [bib_collection(f,'') for f in filenames]

def find(field,string):
    
    for coll in collection: 
        for key in coll.data.keys():
            dat = coll.data[key]
            if getattr(dat,field) == string:
                return key
    print("Couldn't find %s"%string) 


# print out note list
for b in biblist:
    
    # get info
    key = find('doi',b.doi)
    # ~ key = find('title',b.title)
    openaccess = b.openaccess
    note = b.note
    
    # print csv style
    print('%s,%s,%s'%(key,openaccess,note))

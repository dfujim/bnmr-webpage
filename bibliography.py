# formatted using black

import datetime
import bibtexparser
import os
import pandas as pd

class bib_collection(object):
    """
        Holds all bib objects corresponding to a bibtex file
        
        data:   dictionary of bib objects
        kind:   type of entries contained: article, proceeding, thesis, etc.
    """
    
    def __init__(self,bibfile,notes=''):
        """
            bibfile:    path to bibtex file. Name is applied to "kind" input to 
                        bibobject
            notes:      file with keys referencing bibfile. Applies openaccess 
                        and note fields. csv: key,openaccess,note
        """
        
        # check file 
        if not os.path.isfile(bibfile):
            raise IOError('File not found')
        
        # open file 
        with open(bibfile,'r') as fid: 
            lines = fid.readlines()
            
        # get rid of commented lines
        lines = [l for l in lines if l.strip() and '%' != l.strip()[0]]
        
        # get rid of mid-line comments
        for i,l in enumerate(lines):
            j = l.find('%')
            if l[j-1] != '\\':
                lines[i] = l[:j]
            
        # get list of inputs 
        entries = bibtexparser.loads('\n'.join(lines)).entries_dict
        
        # get kind
        kind = os.path.basename(os.path.splitext(bibfile)[0])
        for k in entries:   entries[k]['kind'] = kind
        self.kind = kind
        
        # get notes
        if notes:
            df = pd.read_csv(notes)
            df.set_index('key',inplace=True)
            
            for k in entries:
                if k in df.index:
                    entries[k]['openaccess'] = df.loc[k,'openaccess']
                    entries[k]['note'] = df.loc[k,'note']
            
        # make bib objects
        self.data = {k:bib(**(entries[k])) for k in entries}

    def sort_keys(self,*fields,ascending=None):
        """
            Sort by the values of a particular field
            ascendign default is True for all fields
            
            Ex: b.sort_keys('title','month',ascending=(True,False))
            
            returns list of keys corresponding to the entries in that order
        """
        
        # get keys and field values
        dat = {f:[] for f in fields}
        dat['key'] = []
        for k in self.data.keys():
            for f in fields:
                dat[f].append(getattr(self.data[k],f))
            dat['key'].append(k)
            
        # sort with pandas data frame
        dat = pd.DataFrame(dat)
        
        if ascending is None:
            ascending = [True for i in range(len(fields))]
        
        dat.sort_values(list(fields),
                        ascending=ascending,
                        inplace=True)
        return dat['key'].tolist()
    
class bib(object):
    """ A simple class for holding bibliography entry info """

    # icons 
    icon_doi = '<i class="ai ai-doi"></i>'
    icon_arxiv = '<i class="ai ai-arxiv"></i>'
    icon_orcid = '<i class="ai ai-orcid"></i>'
    icon_openaccess = '<i class="ai ai-open-access" style="color:orangered"></i>'

    # base urls
    urlbase_doi = "https://doi.org/"
    urlbase_arxiv = "https://arxiv.org/abs/"

    def __init__(self,**kwargs):
            
        """ type of entry (article, proceeding, preprint, thesis) """
        self.kind = kwargs.get("kind", None)

        """ common for all types """
        self.author = kwargs.get("author", None)
        self.title = kwargs.get("title", None)
        self.abstract = kwargs.get("abstract", None)

        """ for journal article data """
        self.journal = kwargs.get("journal", None)
        self.volume = kwargs.get("volume", None)
        self.number = kwargs.get("number", None)
        self.pages = kwargs.get("pages", None)

        """ digital object identifiers """
        self.doi = kwargs.get("doi", None)
        self.url = kwargs.get("url", None)

        """ openaccess """
        self.openaccess = kwargs.get("openaccess", False)
        
        """ arxiv preprints identifiers """
        self.arxiv = kwargs.get("arxiv", None)
        self.arxiv_cat = kwargs.get("arxiv_cat", None)
        
        """ thesis fields """
        entry_type = kwargs.get("ENTRYTYPE", None)
        if 'mastersthesis' == entry_type:
            self.degree = "MSc thesis"
        elif 'phdthesis' == entry_type:
            self.degree = "PhD thesis"
        self.school = kwargs.get("school", None)
        self.address = kwargs.get("address", None)
        
        """ note about entry (e.g., editors' choice, cover article, etc.) """
        self.note = kwargs.get("note", None)

        """ date published """
        self.year = kwargs.get("year", "0001")
        self.month = kwargs.get("month", "01")
        
    # number of coauthors
    def n_authors(self):
        return 1 + self.author.count(",")
        
    def format_thesis(self):
        
        fmt = "<p>" + self.author + "</p>\n"
        # title in quotation marks
        fmt += '<p>"' + self.title + '"</p>\n'
        fmt += (
            "<p><i>"
            + self.degree
            + " "
            + self.kind
            + "</i> ("
            + self.school
            + ", "
            + self.address
            + ", "
            + self.year
            + ")"
        )
        
        # add openaccess symbol
        if self.openaccess:
            fmt += " " + self.icon_openaccess
        fmt += "</p>\n"
    
        # new paragraph if there is stuff to link to
        if self.doi != None or self.arxiv != None:
            fmt += "<p>"
            # format the doi: icon + linked url
            if self.doi != None:
                fmt += (
                    " "
                    + self.icon_doi
                    + ' <a href="'
                    + self.urlbase_doi
                    + self.doi
                    + '">'
                    + self.doi
                    + "</a>"
                )
            # format the arxiv: icon + linked url
            if self.arxiv != None:
                fmt += (
                    " "
                    + self.icon_arxiv
                    + ' <a href="'
                    + self.urlbase_arxiv
                    + self.arxiv
                    + '">arXiv:'
                    + self.arxiv
                )
                if self.arxiv_cat != None:
                    fmt += " [" + self.arxiv_cat + "]"
                fmt += "</a>"
            fmt += "</p>\n"
        return fmt

    def format(self,kind='article'):

        if kind == "thesis":
            return self.format_thesis()

        fmt = "<p>" + self.author + "</p>\n"
        # title in quotation marks
        fmt += '<p>"' + self.title + '"</p>\n'
        # italic journal, bold volume, year in parentheses
        # only if there is a journal
        if self.journal != None:
            fmt += (
                "<p><i>"
                + self.journal
                + "</i> <b>"
                + self.volume
                + "</b>, "
                + self.pages
                + " ("
                + self.year
                + ")"
            )
            if self.openaccess == True:
                fmt += " " + self.icon_openaccess
            if self.note != None:
                fmt += " <mark>" + self.note + "</mark>"
            fmt += "</p>\n"
        # new paragraph if there is stuff to link to
        if self.doi != None or self.arxiv != None:
            fmt += "<p>"
            # format the doi: icon + linked url
            if self.doi != None:
                fmt += (
                    " "
                    + self.icon_doi
                    + ' <a href="'
                    + self.urlbase_doi
                    + self.doi
                    + '">'
                    + self.doi
                    + "</a>"
                )
            # format the arxiv: icon + linked url
            if self.arxiv != None:
                fmt += (
                    " "
                    + self.icon_arxiv
                    + ' <a href="'
                    + self.urlbase_arxiv
                    + self.arxiv
                    + '">arXiv:'
                    + self.arxiv
                )
                if self.arxiv_cat != None:
                    fmt += " [" + self.arxiv_cat + "]"
                fmt += "</a>"
            fmt += "</p>\n"
        # add newline if neeeded
        if fmt.endswith("\n"):
            return fmt
        return fmt + "\n"

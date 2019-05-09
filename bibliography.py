# formatted using black

import datetime
import bibtexparser
import os
import pandas as pd
import numpy as np

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
            df.replace(np.nan,'',regex=True,inplace=True)
            
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

    # ======================================================================= # 
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
    
    # ======================================================================= # 
    def _format_article(self):
        """
            Format nice output for journal articles
        """

        # get author names
        lines = [self._get_authors()]
        
        # title in quotation marks
        lines.append(self._get_title())
        
        # italic journal, bold volume, year in parentheses
        # only if there is a journal
        if not self.journal is None:
            jline = "<p><i>%s</i> <b>%s</b>, %s (%s)" % \
                    (self.journal,self.volume,self.pages,self.year)
                    
            openacc = self._get_openaccess()
            note = self._get_note()
            
            lines.append(" ".join((jline,openacc,note,'</p>')))
            
        # format the arxiv: icon + linked url
        arxiv_line = self._get_arxiv()
        
        # format the doi: icon + linked url
        doi_line = self._get_doi()    
        
        # make new paragraph
        lines.append(''.join(("<p>",doi_line,arxiv_line,"</p>")))

        fmt = '\n'.join(lines)
        return fmt+'\n'
    
    # ======================================================================= # 
    def _format_thesis(self):
        """
            Format nice output for thesis
        """
        lines = [self._get_authors()]
        
        # title in quotation marks
        lines.append(self._get_title())
        
        # degree and openaccess
        lines.append("<p><i>%s</i> (%s, %s, %s) %s</p>" % \
                                            (self.degree,self.school,
                                             self.address,self.year,
                                             self._get_openaccess()))
        
        lines.append('<p>%s %s</p>' % (self._get_doi(),self._get_arxiv()))
        
        return '\n'.join(lines)

    # ======================================================================= # 
    def _get_authors(self):
        """Format author string"""
        return '<p>%s</p>' % (', '.join(self.get_author_list(initials=True)))
    
    # ======================================================================= # 
    def _get_arxiv(self):
        """Format arxiv string and linking"""
        
        if not self.arxiv is None:
            line = ' %s <a href="%s%s">arXiv:%s' % \
                (self.icon_arxiv,self.urlbase_arxiv,self.arxiv,self.arxiv)
            
            if not self.arxiv_cat is None:
                line += " [%s]" % self.arxiv_cat
        
            line += "</a>"
            return line
        return ''
    
    # ======================================================================= # 
    def _get_doi(self):
        """Format doi string and linking"""
        if not self.doi is None:
            return ' %s <a href="%s%s">%s</a>'  % ( self.icon_doi,
                                                    self.urlbase_doi,
                                                    self.doi,
                                                    self.doi)
        return ''
    
    # ======================================================================= # 
    def _get_note(self):
        """Format note string"""
        if self.note != "": return " <mark>%s</mark>" % self.note
        return ""
    
    # ======================================================================= # 
    def _get_openaccess(self):
        """Format openaccess symbol"""
        if self.openaccess: return " %s" % self.icon_openaccess
        return ""
    
    # ======================================================================= # 
    def _get_title(self):
        """Format title string"""
        return '<p>"%s"</p>' % self.title
        
    # ======================================================================= # 
    def get_author_list(self,initials=True):
        """
            Make a list of author names. Assume bibtex entry style: 
            
                Author names split by "and"
                If ',' in name, format assumed to be "last, first"
                otherwise format assumed to be "first last"
            
            initials: if true, contract first name to initials
        """
    
        # get authors 
        author_string = self.author
        
        # get list
        authors = author_string.split('and')
        
        # get author in [first],last order
        for i,aut in enumerate(authors):
            
            # get list of list(first) names, and last name
            if ',' in aut:
                name = aut.split(',')[::-1]
                name[0] = name[0].split()
            else:
                name = aut.split()
                name = [name[:-1],name[-1]]
                
            # remove spaces
            name[-1] = name[-1].strip()
                
            # Make first names initials
            if initials:
                first = [f.upper()[0] for f in name[0]]
                name[0] = '. '.join(first)+'.'
            else:
                name[0] = ' '.join(name[0]) 
            
            # make full name
            authors[i] = ' '.join(name)
                
        return authors
            
    # ======================================================================= # 
    def format(self,kind='article'):
        """
            Format nice output control script
        """
        if kind == "thesis":
            return self._format_thesis()
        else:
            return self._format_article()

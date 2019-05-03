# formatted using black

import datetime


class bib:
    """ a simple class for holding bibliography entry info """

    """ debatably a much dumber re-implementation bibtex, but whatever... """

    """ icons """
    icon_doi = '<i class="ai ai-doi"></i>'
    icon_arxiv = '<i class="ai ai-arxiv"></i>'
    icon_orcid = '<i class="ai ai-orcid"></i>'
    icon_openacess = '<i class="ai ai-open-access" style="color:orangered"></i>'

    """ base urls """
    urlbase_doi = "https://doi.org/"
    urlbase_arxiv = "https://arxiv.org/abs/"

    def __init__(self, **kwargs):
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
        self.year = kwargs.get("year", "0001")

        """ (legacy) date info - fails when journal year/pub_year don't match"""
        self.month = kwargs.get("month", "01")
        self.day = kwargs.get("day", "01")

        """ digital object identifiers """
        self.doi = kwargs.get("doi", None)
        self.url = kwargs.get("url", None)

        """ arxiv preprints identifiers """
        self.arxiv = kwargs.get("arxiv", None)
        self.arxiv_cat = kwargs.get("arxiv_cat", None)

        """ open access article flag """
        self.openacess = kwargs.get("openacess", False)

        """ thesis fields """
        self.degree = kwargs.get("degree", None)
        self.school = kwargs.get("school", None)
        self.address = kwargs.get("address", None)

        """ path to pdf """
        self.pdf = kwargs.get("pdf", None)

        """ note about entry (e.g., editors' choice, cover article, etc.) """
        self.note = kwargs.get("note", None)

        """ date published """
        self.pub_year = kwargs.get("pub_year", "0001")
        self.pub_month = kwargs.get("pub_month", "01")
        self.pub_day = kwargs.get("pub_day", "01")
        self.pub_date = kwargs.get("pub_date", None)

        """ date submitted """
        self.sub_year = kwargs.get("sub_year", "0001")
        self.sub_month = kwargs.get("sub_month", "01")
        self.sub_day = kwargs.get("sub_day", "01")
        self.sub_date = kwargs.get("sub_date", None)

        """ convert strings to datetime.date objects """
        if self.sub_date != None:
            self.sub_date = datetime.datetime.strptime(self.sub_date, "%Y-%m-%d").date()

        if self.pub_date != None:
            self.pub_date = datetime.datetime.strptime(self.pub_date, "%Y-%m-%d").date()

        self.date = datetime.date(int(self.year), int(self.month), int(self.day))

    """ number of days between sub_date and pub_date """
    def days2publish(self):
        if self.sub_date == None or self.pub_date == None:
            return None
        return (self.pub_date - self.sub_date).days
    
    """ number of coauthors """
    def n_authors(self):
        return 1 + self.author.count(",")
        
    def format_thesis(self):
        if self.kind != "thesis":
            return ""
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
        if self.openacess == True:
            fmt += " " + self.icon_openacess
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

    def format(self):

        if self.kind == "thesis":
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
            if self.openacess == True:
                fmt += " " + self.icon_openacess
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

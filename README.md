# BNMR Group Website

Backend files for the UBC's BNMR reserach group, led by Rober Kiefl and Andrew MacFarlane. 


## Developer Notes

### Running locally: 

* In `bnmr-webpage`, run `bash build.bash`
* In `bnmr-webpage/_site` run `jekell serve`

### Pages 

The following list the markdown files needed to format the various subpages of the site. 

* [index](https://github.com/dfujim/bnmr-webpage/blob/master/index.md)
* [people](https://github.com/dfujim/bnmr-webpage/blob/master/people.md)
* [experiments](https://github.com/dfujim/bnmr-webpage/blob/master/experiments.md)
* [publications](https://github.com/dfujim/bnmr-webpage/blob/master/publications.md)

## Adding Publications 

Everything you need is in [data/](https://github.com/dfujim/bnmr-webpage/tree/master/data). Here is a step-by-step procedure for adding a new publication to the website: 

* Add the bibtex formatted entry to the proper `.bib` file. This will account for the sorting of the files. Make a new `.bib` file if there are no good sorting options. Please make sure the reference key is unique.
* If there are additional notes (front cover, etc.) or if the publication is openaccess please add the corresponding line to [`bibnotes.csv`](https://github.com/dfujim/bnmr-webpage/blob/master/data/bibnotes.csv). The line should have the format `key,True,note`. It is important that the `True`/`False` is capitalized, and that there is no trailing comma after the note.
* If you have created a new category (i.e. a new bib file) then you should edit the [`publications.md`](https://github.com/dfujim/bnmr-webpage/blob/master/publications.md) file, so that it will be linked on the main page. 
* Re-generate the page with `bash build.bash`.

## Bibliography 

Website design based on that of Ryan MacFadden: [rmlm.gitlab.io](https://rmlm.gitlab.io), which in turn cites the following: 

The web design used here is based on Joseph Wright's blog
[texdev.net](https://www.texdev.net/), whose source can be found on
[GitHub](https://github.com/josephwright/josephwright.github.io).
Joseph's design work is based on that used by the
[LaTeX Project](https://www.latex-project.org), which was carried out by
[Jonas Jacek](http://jonas.me/), and is licensed under the
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

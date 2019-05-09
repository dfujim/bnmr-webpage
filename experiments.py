# formatted using black

import requests
import pandas as pd

# public list of triumf experiments
baseurl = "https://mis.triumf.ca/science/experiment/list.jsf"

# we want every MMS experiment
schedule = "View+all"
discipline = "M"
status = "View+all"

# make the full url
url = (
    baseurl
    + "?"
    + "schedule="
    + schedule
    + "&"
    + "discipline="
    + discipline
    + "&"
    + "status="
    + status
)

expbaseurl = "https://mis.triumf.ca/science/experiment/view/"

# get the page html
html = requests.get(url).content

# extract the table
df_list = pd.read_html(html)
df = df_list[-1]

# drop NaN containing rows (i.e., ones with missing elements)
df = df.dropna()

# tables can be accessed by the column names:
# 'Number', 'Title', 'Spokespersons'

# list of our experiments
with open('data/triumf_experiments.dat','r') as fid:
    experiments = fid.readlines()

# sort and reorder
experiments = [e.strip() for e in experiments]
experiments = sorted(experiments, reverse=True)

def md_table_row(number, title, spokespersons):
    # make the link in markdown
    exp_url = "https://mis.triumf.ca/science/experiment/view/" + number
    exp_link = "[" + number + "](" + exp_url + ")"

    # format some text for better appearence in html
    # check = ['8Li', 'Li+',]
    # for c in check:

    # create the string for the table row
    # row = '| ' + exp_link + ' | ' + title + ' | ' + spokespersons + ' |'
    row = "| " + exp_link + " | " + title + " |"
    return row

def html_table_row(number, title, spokespersons):
    # make the link in markdown
    exp_url = "https://mis.triumf.ca/science/experiment/view/" + number
    exp_link = '<a href="' + exp_url + '">' + number + "</a>"

    row = "<tr>\n"
    row += "\t<td>" + exp_link + "</td>\n"
    row += "\t<td>" + title + "</td>\n"
    row += "</tr>"
    return row

# conveniently print n tabs
def tabs(num_tabs):
    tab_str = ""
    for i in range(num_tabs):
        tab_str += "\t"
    return tab_str

def html_table_row_tabs(number, title, spokespersons, tabs):
    # make the link in markdown
    exp_url = "https://mis.triumf.ca/science/experiment/view/" + number
    exp_link = '<a href="' + exp_url + '">' + number + "</a>"

    row = tabs + "<tr>\n"
    row += tabs + "\t<td>" + exp_link + "</td>\n"
    row += tabs + "\t<td>" + title + "</td>\n"
    row += tabs + "</tr>\n"
    return row

# fix the formatting of isotopes & chemical compounds
def fix_fmt(string):
    fixed = string

    pairs = [
        ["8Li", "<sup>8</sup>Li"],
        ["9Li", "<sup>9</sup>Li"],
        ["Li+", "Li<sup>+</sup>"],
        ["31Mg", "<sup>31</sup>Mg"],
        ["UBe13", "UBe<sub>13</sub>"],
        ["CO2", "CO<sub>2</sub>"],
        ["Cr2O3", "Cr<sub>2</sub>O<sub>3</sub>"],
        ["LiV2O4", "LiV<sub>2</sub>O<sub>4</sub>"],
        ["SrTiO3", "SrTiO<sub>3</sub>"],
    ]

    for p in pairs:
        fixed = fixed.replace(p[0], p[1])

    return fixed

# write the list as a html table a file
with open("_html/triumf_experiments.html", "w") as fh:

    # write the table
    fh.write(tabs(0) + "<center>\n")
    fh.write(tabs(1) + '<table id="experiments">\n')

    # head
    fh.write(tabs(2) + "<thead>\n")
    fh.write(tabs(3) + "<th>Number</th>\n")
    fh.write(tabs(3) + "<th>Title</th>\n")
    fh.write(tabs(2) + "</thead>\n")

    # body
    fh.write(tabs(2) + "<tbody>\n")
    for e in experiments:
        for n, t, s in zip(df["Number"], df["Title"], df["Spokespersons"]):
            if e == n:
                row = html_table_row_tabs(n, fix_fmt(t), s, tabs(3))
                fh.write(row)
    fh.write(tabs(2) + "</tbody>\n")
    fh.write(tabs(1) + "\t</table>\n")
    fh.write(tabs(0) + "</center>\n")

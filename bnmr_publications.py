# formatted using black

import numpy as np
import matplotlib.pyplot as plt

from bnmr_articles import articles
from bnmr_preprints import preprints
from bnmr_proceedings import proceedings
from bnmr_theses import theses


# unabridged list of bnmr publications out of triumf
publications = articles + preprints + proceedings + theses


# sorting lists inplace
# https://stackoverflow.com/a/403426
# https://stackoverflow.com/a/4233482

# sort articles into reverse chronological order and desceding page number
# (i.e., for conference proceedings that are published on the same day)
publications.sort(key=lambda p: (p.pub_date.isoformat(), p.pages), reverse=True)

# types of entries in bnmr publications list
kinds = ["article", "preprint", "proceeding", "thesis"]

# write the sorted/formatted publication lists to files
for k in kinds:
    fname = "_posts/bnmr_" + k + ".html"
    with open(fname, "w") as fh:
        fh.write('<ol reversed id="publications">\n')
        for p in publications:
            if p.kind == k:
                fh.write("<li>\n")
                fh.write(p.format())
                fh.write("</li>\n")
        fh.write("</ol>\n")


# get only the journal articles
ja_sub_dates = []
ja_pub_dates = []
ja_days2pub = []
for p in publications:
    if p.kind != "thesis":
        ja_sub_dates.append(p.sub_date)
        ja_pub_dates.append(p.pub_date)
        ja_days2pub.append(p.days2publish())
        # print(p.n_authors())

ja_sub_dates = np.array(ja_sub_dates)
ja_pub_dates = np.array(ja_pub_dates)
ja_days2pub = np.array(ja_days2pub)

not_zero = ja_days2pub > 0

avg = np.average(ja_days2pub[not_zero])
std = np.std(ja_days2pub[not_zero], ddof=1)

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, gridspec_kw=dict(width_ratios=[5, 1]))
for ax in (ax1, ax2):
    ax.tick_params(direction="in", top=True, bottom=True, left=True, right=True)

ax1.plot(ja_pub_dates[not_zero], ja_days2pub[not_zero], "o")
# ax.hist(ja_days2pub)
ax1.axhline(avg, linestyle="--", color="gray", zorder=0)
ax1.axhspan(avg - std, avg + std, facecolor="lightgray", zorder=0)

ax2.boxplot(ja_days2pub[not_zero])
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax2.axis("off")


"""
dates = [p.date for p in publications]
v = [1 for p in publications]
journals = [p.journal for a in publications]

fig, ax = plt.subplots(1, 1)  # constrained_layout=True
# ax.axhline(0, linestyle='-', color='black', zorder=0)
ax.plot(dates, v, "o")
"""

"""
for d, y, j in zip(dates, v, journals):
    ax.annotate(j, (d, y), (d, y), va="bottom", ha="left", rotation=60)
"""
ax1.set_ylim(0, None)
# ax.set_xlabel("Date")
ax1.set_ylabel("Days")
# ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
# ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax1.set_title(
    "Time between submission and online\npublication for a β-NMR journal article\n"
)

fig.autofmt_xdate()

fig.tight_layout()


plt.show()

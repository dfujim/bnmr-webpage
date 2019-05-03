# formatted using black

from bibliography import bib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


publications = [
    bib(
        author="R. M. L. McFadden, A. Chatzichristos, K. H. Chow, D. L. Cortie, M. H. Dehn, D. Fujimoto, M. D. Hossain, H. Ji, V. L. Karner, R. F. Kiefl, C. D. P. Levy, R. Li, I. McKenzie, G. D. Morris, O. Ofer, M. R. Pearson, M. Stachura, R. J. Cava, and W. A. MacFarlane",
        title="Ionic and electronic properties of the topological insulator Bi<sub>2</sub>Te<sub>2</sub>Se investigated via β-detected nuclear magnetic relaxation and resonance of <sup>8</sup>Li",
        journal="Phys. Rev. B",
        volume="99",
        pages="125201",
        year="2019",
        month="02",
        day="15",
        doi="10.1103/PhysRevB.99.125201",
        arxiv="1810.07879",
        arxiv_cat="cond-mat.mtrl-sci",
        kind="article",
        sub_date="2018-10-26",
        pub_date="2019-03-08",
    ),
    bib(
        author="D. Szunyogh, R. M. L. McFadden, V. L. Karner, A. Chatzichristos, T. Day Goodacre, M. H. Dehn, L. Formenti, D. Fujimoto, A. Gottberg, E. Kallenberg, I. Kálomista, R. F. Kiefl, F. H. Larsen, J. Lassen, C. D. P. Levy, R. Li, W. A. MacFarlane, I. McKenzie, G. D. Morris, S. Pallada, M. R. Pearson, S. P. A. Sauer, P. Schaffer, P. W. Thulstrup, L. Hemmingsen, and M. Stachura",
        title="Direct observation of Mg<sup>2+</sup> complexes in ionic liquid solutions by <sup>31</sup>Mg β-NMR spectroscopy",
        journal="Dalton Trans.",
        volume="47",
        pages="14431",
        year="2018",
        month="10",
        day="03",
        doi="10.1039/C8DT02350F",
        openacess=True,
        kind="article",
        sub_date="2018-06-07",
        pub_date="2018-10-03",
    ),
    bib(
        author="I. McKenzie, Y. Chai, D. L. Cortie, J. A. Forrest, D. Fujimoto, V. L. Karner, R. F. Kiefl, C. D. P. Levy, W. A. MacFarlane, R. M. L. McFadden, G. D. Morris, M. R. Pearson, and S. Zhu",
        title="Direct measurements of the temperature, depth and processing dependence of phenyl ring dynamics in polystyrene thin films by β-detected NMR",
        journal="Soft Matter",
        volume="14",
        pages="7324",
        year="2018",
        month="04",
        day="24",
        doi="10.1039/C8SM00812D",
        openacess=False,
        kind="article",
        sub_date="2018-04-19",
        pub_date="2018-05-24",
        note="Inside Front Cover",
    ),
    bib(
        author="M. H. Dehn, D. J. Arseneau, T. Buck, D. L. Cortie, D. G. Fleming, S. R. King, W. A. MacFarlane, A. M. McDonagh, R. M. L. McFadden, D. R. G. Mitchell, and R. F. Kiefl",
        title="Nature of magnetism in thiol-capped gold nanoparticles investigated with muon spin rotation",
        journal="Appl. Phys. Lett.",
        volume="112",
        pages="053105",
        year="2018",
        month="01",
        day="31",
        doi="10.1063/1.5017768",
        openacess=False,
        kind="article",
        sub_date="2017-11-30",
        pub_date="2018-01-31",
    ),
    bib(
        author="R. M. L. McFadden, T. J. Buck, A. Chatzichristos, C.-C. Chen, K. H. Chow, D. L. Cortie, M. H. Dehn, V. L. Karner, D. Koumoulis, C. D. P. Levy, C. Li, I. McKenzie, R. Merkle, G. D. Morris, M. R. Pearson, Z. Salman, D. Samuelis, M. Stachura, J. Xiao, J. Maier, R. F. Kiefl, and W. A. MacFarlane",
        title="Microscopic dynamics of Li<sup>+</sup> in rutile TiO<sub>2</sub> revealed by <sup>8</sup>Li β-detected nuclear magnetic resonance",
        journal="Chem. Mater.",
        volume="29",
        pages="10187",
        year="2017",
        month="11",
        day="07",
        doi="10.1021/acs.chemmater.7b04093",
        arxiv="1709.06674",
        arxiv_cat="cond-mat.mtrl-sci",
        openacess=False,
        kind="article",
        sub_date="2017-09-26",
        pub_date="2017-11-07",
    ),
    bib(
        author="J. Sugiyama, I. Umegaki, T. Uyama, R. M. L. McFadden, S. Shiraki, T. Hitosugi, Z. Salman, H. Saadaoui, G. D. Morris, W. A. MacFarlane, and R. F. Kiefl",
        title="Lithium diffusion in spinel Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub> and LiTi<sub>2</sub>O<sub>4</sub> films detected with <sup>8</sup>Li β-NMR",
        journal="Phys. Rev. B",
        volume="96",
        pages="094402",
        year="2017",
        month="09",
        day="01",
        doi="10.1103/PhysRevB.96.094402",
        openacess=True,
        kind="article",
        sub_date="2017-02-01",
        pub_date="2017-09-01",
    ),
    bib(
        author="A. Chatzichristos, R. M. L. McFadden, V. L. Karner, D. L. Cortie, C. D. P. Levy, W. A. MacFarlane, G. D. Morris, M. R. Pearson, Z. Salman, and R. F. Kiefl",
        title="Determination of the nature of fluctuations using <sup>8</sup>Li and <sup>9</sup>Li β-NMR and spin-lattice relaxation",
        journal="Phys. Rev. B",
        volume="96",
        pages="014307",
        year="2017",
        month="07",
        day="31",
        doi="10.1103/PhysRevB.96.014307",
        arxiv="1703.10156",
        arxiv_cat="cond-mat.mtrl-sci",
        openacess=False,
        kind="article",
        sub_date="2017-03-26",
        pub_date="2017-07-31",
    ),
    bib(
        author="I. McKenzie, D. L. Cortie, M. Harada, R. F. Kiefl, C. D. P. Levy, W. A. MacFarlane, R. M. L. McFadden, G. D. Morris, S.-I. Ogata, M. R. Pearson, and J. Sugiyama",
        title="β-NMR measurements of molecular-scale lithium-ion dynamics in poly(ethylene oxide)-lithium-salt thin films",
        journal="J. Chem. Phys.",
        volume="146",
        pages="244903",
        year="2017",
        month="06",
        day="27",
        doi="10.1063/1.4989866",
        openacess=False,
        kind="article",
        sub_date="2017-02-22",
        pub_date="2017-06-27",
    ),
    bib(
        author="M. H. Dehn, D. J. Arseneau, P. Böni, M. D. Bridges, T. Buck, D. L. Cortie, D. G. Fleming, J. A. Kelly, W. A. MacFarlane, M. J. MacLachlan, R. M. L. McFadden, G. D. Morris, P.-X. Wang, J. Xiao, V. M. Zamarion, and R. F. Kiefl",
        title="Chemisorption of muonium on gold nanoparticles: a sensitive new probe of surface magnetism and reactivity",
        journal="J. Chem. Phys.",
        volume="145",
        pages="181102",
        year="2016",
        month="11",
        day="11",
        doi="10.1063/1.4967460",
        openacess=False,
        kind="article",
        sub_date="2016-08-25",
        pub_date="2016-11-11",
    ),
    bib(
        author="D. L. Cortie, T. Buck, M. H. Dehn, V. L. Karner, R. F. Kiefl, C. D. P. Levy, R. M. L. McFadden, G. D. Morris, I. McKenzie, M. R. Pearson, X. L. Wang, and W. A. MacFarlane",
        title="β-NMR investigation of the depth-dependent magnetic properties of an antiferromagnetic surface",
        journal="Phys. Rev. Lett.",
        volume="116",
        pages="106103",
        year="2016",
        month="03",
        day="10",
        doi="10.1103/PhysRevLett.116.106103",
        openacess=False,
        kind="article",
        sub_date="2015-08-16",
        pub_date="2016-03-10",
    ),
    bib(
        author="D. L. Cortie, T. Buck, M. H. Dehn, R. F. Kiefl, C. D. P. Levy, R. M. L. McFadden, G. D. Morris, M. R. Pearson, Z. Salman, Y. Maeno, and W. A. MacFarlane",
        title="Spin fluctuations in the exotic metallic state of Sr<sub>2</sub>RuO<sub>4</sub> studied with β-NMR",
        journal="Phys. Rev. B",
        volume="91",
        pages="241113(R)",
        year="2015",
        month="06",
        day="23",
        doi="10.1103/PhysRevB.91.241113",
        openacess=False,
        kind="article",
        sub_date="2015-02-14",
        pub_date="2015-06-23",
    ),
    bib(
        author="P. J. Cormier, R. M. Clarke, R. M. L. McFadden, and K. Ghandi",
        title="Selective free radical reactions using supercritical carbon dioxide",
        journal="J. Am. Chem. Soc.",
        volume="136",
        pages="2200",
        year="2014",
        month="01",
        day="29",
        doi="10.1021/ja408438s",
        openacess=False,
        kind="article",
        sub_date="2013-08-17",
        pub_date="2014-01-29",
    ),
    bib(
        author="K. Ghandi, R. M. L. McFadden, P. J. Cormier, P. Satija and M. Smith",
        title="Radical kinetics in sub- and supercritical carbon dioxide: thermodynamic rate tuning",
        journal="Phys. Chem. Chem. Phys.",
        volume="14",
        pages="8502",
        year="2012",
        month="05",
        day="02",
        doi="10.1039/C2CP41170A",
        openacess=False,
        kind="article",
        sub_date="2012-04-12",
        pub_date="2012-05-02",
    ),
    bib(
        author="P. Satija, R. M. L. McFadden, P. Cormier, and K.Ghandi",
        title="Selectivity of free radical reactions with vinylidene fluoride in supercritical carbon dioxide, probed by muon spin spectroscopy",
        journal="Int. Rev. Chem. Eng.",
        volume="3",
        pages="542",
        year="2011",
        month="09",
        day="01",
        url="https://www.praiseworthyprize.org/latest_issues/IRECHE-latest/IRECHE_vol_3_n_5.html#Selectivity_of_Free_Radical_Reactions_with_Vinylidene_Fluoride_in_Supercritical_Carbon_Dioxide,_Probed_by_Muon_Spin_Spectroscopy",
        openacess=False,
        kind="article",
        sub_date=None,
        pub_date=None,
    ),
    # proceedings
    bib(
        author="A. Chatzichristos, R. M. L. McFadden, V. L. Karner, D. L. Cortie, C. D. P. Levy, W. A. MacFarlane, G. D. Morris, M. R. Pearson, Z. Salman, and R. F. Kiefl",
        title="Comparison of <sup>8</sup>Li and <sup>9</sup>Li spin relaxation in SrTiO<sub>3</sub> and Pt: a means to distinguish magnetic and electric quadrupolar sources of relaxation",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011048",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011048",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-19",
        pub_date="2018-03-01",
    ),
    bib(
        author="R. M. L. McFadden, A. Chatzichristos, M. H. Dehn, D. Fujimoto, H. Funakubo, A. Gottberg, T. Hitosugi, V. L. Karner, R. F. Kiefl, M. Kurokawa, J. Lassen, C. D. P. Levy, R. Li, G. D. Morris, M. R. Pearson, S. Shiraki, M. Stachura, J. Sugiyama, D. M. Szunyogh, and W. A. MacFarlane",
        title="On the use of <sup>31</sup>Mg for β-detected NMR studies of solids",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011047",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011047",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-15",
        pub_date="2018-03-01",
    ),
    bib(
        author="A. C. Y. Fang, M. H. Dehn, R. M. L. McFadden, V. L. Karner, J. E. Sonier, W. A. MacFarlane, G. D. Morris, C. Gomez, K. Akintola, and R. F. Kiefl",
        title="Origin of the multi-peak muon frequency spectrum in the heavy fermion compound UBe<sub>13</sub>",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011029",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011029",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-22",
        pub_date="2018-03-01",
    ),
    bib(
        author="V. L. Karner, R. M. L. Mcfadden, M. H. Dehn, D. Fujimoto, A. Chatzichristos, G. D. Morris, M. R. Pearson, C. D. P. Levy, A. Reisner, L. H. Tjeng, R. F. Kiefl, and W. A. Macfarlane",
        title="Beta-detected NMR of LSAT and YSZ",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011024",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011024",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-21",
        pub_date="2018-03-01",
    ),
    bib(
        author="V. L. Karner, R. M. L. Mcfadden, A. Chatzichristos, G. D. Morris, M. R. Pearson, C. D. P. Levy, Z. Salman, D. L. Cortie, R. F. Kiefl, and W. A. Macfarlane",
        title="Beta detected NMR of LaAlO<sub>3</sub>",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011023",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011023",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-21",
        pub_date="2018-03-01",
    ),
    bib(
        author="V. L. Karner, T. Liu, I. Mckenzie, A. Chatzichristos, D. L. Cortie, G. D. Morris, R. F. Kiefl, R. M. L. Mcfadden, Z. Fakhraai, M. Stachura, and W. A. Macfarlane",
        title="Exploring the dynamics of glasses using beta detected NMR",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011022",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011022",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-21",
        pub_date="2018-03-01",
    ),
    bib(
        author="J. Sugiyama, I. Umegaki, S. Shiraki, T. Hitosugi, R. M. L. McFadden, D. Wang, V. Karner, G. D. Morris, W. A. MacFarlane, and R. F. Kiefl",
        title="Challenge for detecting the interface between electrode and electrolyte with β-NMR",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011021",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011021",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-14",
        pub_date="2018-03-01",
    ),
    bib(
        author="W. A. MacFarlane, K. H. Chow, M. D. Hossain, V. L. Karner, R. F. Kiefl, R. M. L. McFadden, G. D. Morris, H. Saadaoui, and Z. Salman",
        title="The spin relaxation of <sup>8</sup>Li<sup>+</sup> in gold at low magnetic field",
        journal="JPS Conf. Proc.",
        volume="21",
        pages="011020",
        year="2018",
        month="03",
        day="01",
        doi="10.7566/JPSCP.21.011020",
        openacess=True,
        kind="proceeding",
        sub_date="2017-06-23",
        pub_date="2018-03-01",
    ),
    bib(
        author="M. Stachura, R. M. L. McFadden, A. Chatzichristos, M. H. Dehn, A. Gottberg, L. Hemmingsen, A. Jancso, V. L. Karner, R. F. Kiefl, F. H. Larsen, J. Lassen, C. D. P. Levy, R. Li, W. A. MacFarlane, G. D. Morris, S. Pallada, M. R. Pearson, D. Szunyogh, P. W. Thulstrup, and A. Voss",
        title="Towards <sup>31</sup>Mg-β-NMR resonance linewidths adequate for applications in magnesium chemistry",
        journal="Hyperfine Interact.",
        volume="238",
        pages="32",
        year="2017",
        month="02",
        day="14",
        doi="10.1007/s10751-017-1408-8",
        openacess=False,
        kind="proceeding",
        sub_date="2017-02-14",
        pub_date="2017-02-14",
    ),
    bib(
        author="C. D. P. Levy, M. R. Pearson, M. H. Dehn, V. L. Karner, R. F. Kiefl, J. Lassen, R. Li, W. A. MacFarlane, R. M. L. McFadden, G. D. Morris, M. Stachura, A. Teigelhöfer, and A. Voss",
        title="Development of a polarized <sup>31</sup>Mg<sup>+</sup> beam as a spin-1/2 probe for BNMR",
        journal="Hyperfine Interact.",
        volume="237",
        pages="162",
        year="2016",
        month="11",
        day="22",
        doi="10.1007/s10751-016-1372-8",
        openacess=False,
        kind="proceeding",
        sub_date="2016-11-22",
        pub_date="2016-11-22",
    ),
    bib(
        author="W. A. MacFarlane, T. J. Parolin, D. L. Cortie, K. H. Chow, M. D. Hossain, R. F. Kiefl, C. D. P. Levy, R. M. L. McFadden, G. D. Morris, M. R. Pearson, H. Saadaoui, Z. Salman, Q. Song, and D. Wang",
        title="<sup>8</sup>Li<sup>+</sup> β-NMR in the cubic insulator MgO",
        journal="J. Phys.: Conf. Ser.",
        volume="551",
        pages="012033",
        year="2014",
        month="12",
        day="16",
        doi="10.1088/1742-6596/551/1/012033",
        openacess=True,
        kind="proceeding",
        sub_date="2014-10-21",
        pub_date="2014-12-16",
    ),
    bib(
        author="R. M. L. McFadden, D. L. Cortie, D. J. Arseneau, T. J. Buck, C.-C. Chen, M. H. Dehn, S. R. Dunsiger, R. F. Kiefl, C. D. P. Levy, C. Li, G. D. Morris, M. R. Pearson, D. Samuelis, J. Xiao, J. Maier, and W. A. MacFarlane",
        title="β-NMR of <sup>8</sup>Li<sup>+</sup> in rutile TiO<sub>2</sub>",
        journal="J. Phys.: Conf. Ser.",
        volume="551",
        pages="012032",
        year="2014",
        month="12",
        day="16",
        doi="10.1088/1742-6596/551/1/012032",
        openacess=True,
        kind="proceeding",
        sub_date="2014-10-21",
        pub_date="2014-12-16",
    ),
    bib(
        author="D. Cortie, T. Buck, R. M. L. McFadden, J. Xiao, C. D. P. Levy, M. Dehn, M. Pearson, G. D. Morris, S. R. Dunsiger, R. F. Kiefl, F. J. Rueß, A. Fuhrer, and W. A. MacFarlane",
        title="β-NMR study of a buried Mn δ-doped layer in a silicon host",
        journal="J. Phys.: Conf. Ser.",
        volume="551",
        pages="012023",
        year="2014",
        month="12",
        day="16",
        doi="10.1088/1742-6596/551/1/012023",
        openacess=True,
        kind="proceeding",
        sub_date="2014-10-21",
        pub_date="2014-12-16",
    ),
    # preprints
    bib(
        author="A. Chatzichristos, R. M. L. McFadden, M. H. Dehn, S. R. Dunsiger, D. Fujimoto, V. L. Karner, C. D. P. Levy, I. McKenzie, G. D. Morris, M. R. Pearson, M. Stachura, J. Sugiyama, J. O. Ticknor, W. A. MacFarlane, and R. F. Kiefl",
        title="Bi-Arrhenius diffusion and surface trapping of <sup>8</sup>Li<sup>+</sup> in rutile TiO<sub>2</sub>",
        year="2018",
        month="10",
        day="30",
        arxiv="1810.12537",
        arxiv_cat="cond-mat.mtrl-sci",
        kind="preprint",
        sub_date="2018-10-30",
        pub_date="2019-03-01",
    ),
]


# sorting lists inplace
# https://stackoverflow.com/a/403426
# https://stackoverflow.com/a/4233482

# sort articles into reverse chronological order and desceding page number
# (i.e., for conference proceedings that are published on the same day)
publications.sort(key=lambda p: (p.date.isoformat(), p.pages), reverse=True)

kinds = ["article", "proceeding", "preprint"]
# write the sorted/formatted publication lists to files
for k in kinds:
    with open("publications/" + k + "s.html", "w") as fh:
        fh.write('<ol reversed id="publications">\n')
        for p in publications:
            if p.kind == k:
                fh.write("<li>\n")
                fh.write(p.format())
                fh.write("</li>\n")
        fh.write("</ol>\n")

"""
# write a temporary .html file to check the formatting
with open("test.html", "w") as f:
    f.write('<meta charset="utf-8">\n')
    f.write(
        '<link rel="stylesheet" href="https://cdn.rawgit.com/jpswalsh/academicons/master/css/academicons.min.css">\n'
    )
    f.write("<ol reversed>\n")
    for p in publications:
        if p.kind == "article" or p.kind == "proceeding" or p.kind == "preprint":
            # print(p.date.isoformat())
            f.write("<li>\n")
            f.write(p.format())
            f.write("</li>\n")
    f.write("</ol>\n")
"""

#
dates = [p.date for p in publications]
v = [1 for p in publications]
journals = [p.journal for a in publications]

fig, ax = plt.subplots(1, 1)  # constrained_layout=True
# ax.axhline(0, linestyle='-', color='black', zorder=0)
ax.plot(dates, v, "o")

for d, y, j in zip(dates, v, journals):
    ax.annotate(j, (d, y), (d, y), va="bottom", ha="left", rotation=60)

ax.set_ylim(0, 10)
ax.set_xlabel("Date")
# ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
# ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m"))
fig.autofmt_xdate()

fig.tight_layout()

# plt.show()

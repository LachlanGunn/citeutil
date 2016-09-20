citeutil
========

*Citeutil* is a program to generate formatted citations from document
references.  Currently this means Crossref DOIs, however the intention
is to support ArXiV references as well.

**Citeutil is in the public domain.**
*See LICENCE.md for details.*

Usage
-----

    usage: citeutil [-h] [--format {bibtex,html,text}] doi [doi ...]

    positional arguments:
      doi                   DOIs to look up

    optional arguments:
      -h, --help            show this help message and exit
      --format {bibtex,html,text}
                            output format

Synopsis
--------

**BibTeX format:**

    citeutil 10.1098/rspa.2015.0748

*Output:*

    @article{gunn16,
     title = {Too good to be true: when overwhelming evidence fails to convince},
     author = {Lachlan J.~Gunn and François Chapeau-Blondeau and Mark D.~McDonnell and Bruce R.~Davis and Andrew Allison and Derek Abbott},
     journal = {Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science},
     volume = {472},
     number = {2187},
     pages = {20150748},
     year = {2016},
     doi = {10.1098/rspa.2015.0748}
    }

**HTML format:**

    citeutil --format text 10.1098/rspa.2015.0748

*Output:*

Lachlan J. Gunn, François Chapeau-Blondeau, Mark D. McDonnell, Bruce R. Davis, Andrew Allison, and Derek Abbott, 'Too good to be true: when overwhelming evidence fails to convince', <em>Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science</em>, <strong>472</strong>(2187), 2016, doi:10.1098/rspa.2015.0748

**Text format:**

    citeutil --format text 10.1098/rspa.2015.0748

*Output:*

    Lachlan J. Gunn, François Chapeau-Blondeau, Mark D. McDonnell, Bruce R. Davis, Andrew Allison, and Derek Abbott, 'Too good to be true: when overwhelming evidence fails to convince', Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science, 472(2187), 2016, doi:10.1098/rspa.2015.0748

Features
--------

We make some effort to maintain proper capitalisation in the BibTeX output.
The file *propernames* contains a list of words that should always have an
initial capital.  In addition, we keep the capitalisation of any word
containing more than one capital letter, though the exact details will
likely change.

Author
------

**Lachlan Gunn**

<table>
<tr><td>Email</td><td>lachlan@twopif.net</td></tr>
<tr>
    <td>PGP</td>
    <td><code>F3E3 8891 8560 5B82 933D  6180 D288 91D2 136B 33B0</code></td>
</tr>
<tr>
    <td>Github</td>
    <td><a href="https://github.com/lachlangunn">LachlanGunn</a></td>
</tr>
<tr>
    <td>Keybase</td>
    <td><a href="https://keybase.io/lachlangunn">LachlanGunn</a></td>
</tr>
</table>

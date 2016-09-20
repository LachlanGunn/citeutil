#!/usr/bin/env python

import worktype
import re

class TextFormatter(object):
    def __init__(self):
        pass

    def __format_author(self, author):
        return re.sub('\.(\w)', '. \\1', author['given']) \
            + ' ' + author['family']
        
    def format(self, work):
        if type(work) == worktype.JournalPaper:
            result = ''
            formatted_authors = [self.__format_author(a) for a in work.authors]
            if len(formatted_authors) == 0:
                pass
            elif len(formatted_authors) == 1:
                result += formatted_authors[0]
            elif len(formatted_authors) == 2:
                result += ' and '.join(formatted_authors)
            else:
                result += ', '.join(formatted_authors[0:-1]) \
                        + ', and ' + formatted_authors[-1]
            result += ", '" + work.title + "'"
            result += ", "  + work.journal
            result +=  ", " + work.issue[0]
            if len(work.issue) > 1:
                result += "(%s)" % work.issue[1]

            result += ", %d" % work.date_published['date-parts'][0][0]
            result += ", doi:" + work.doi

            return result
                                    
        else:
            raise RuntimeError('TextFormatter does not support this work type.')

class HTMLFormatter(object):
    def __init__(self):
        pass

    def __format_author(self, author):
        return re.sub('\.(\w)', '.&nbsp;\\1', author['given']) \
            + ' ' + author['family']
        
    def format(self, work):
        if type(work) == worktype.JournalPaper:
            result = ''
            formatted_authors = [self.__format_author(a) for a in work.authors]
            if len(formatted_authors) == 0:
                pass
            elif len(formatted_authors) == 1:
                result += formatted_authors[0]
            elif len(formatted_authors) == 2:
                result += ' and '.join(formatted_authors)
            else:
                result += ', '.join(formatted_authors[0:-1]) \
                        + ', and ' + formatted_authors[-1]
            result += ", '" + work.title + "'"
            result += ", <em>%s</em>" % work.journal
            result +=  ", <strong>%s</strong>" % work.issue[0]
            if len(work.issue) > 1:
                result += "(%s)" % work.issue[1]

            result += ", %d" % work.date_published['date-parts'][0][0]
            result += ", doi:" + work.doi

            return result
                                    
        else:
            raise RuntimeError('HTMLFormatter does not support this work type.')

class BibtexFormatter(object):
    def __init__(self, proper_names):
        self.proper_names = proper_names
	self.used_identifiers = []

    def __format_author(self, author):
        result = re.sub('\\.(\w)', '. \\1', author['given']) \
            + ' ' + author['family']
        return result.replace('. ', '.~')

    def __format_pages(self, pages):
        return pages.replace('-', '--')

    def __format_title(self, title):
        for name in self.proper_names:
            title = title.replace(name, '{%s}' % name)

        return re.sub('([^\\s]*[A-Z]\w*[A-Z][^\\s]*)', '{\\1}', title)

    def __make_identifier(self, work):
	root = '%s%02d' % ( work.authors[0]['family'].replace(' ','').lower(),
                        work.date_published['date-parts'][0][0] % 100 )

	if root not in self.used_identifiers:
	    self.used_identifiers.append(root)
	    return root

	# The list of used identifiers is finite so this must terminate.
	suffix_length = 0
	suffix = ''
	alphabet_size = 26
	while True:
	    suffix_length += 1
	    suffix = ['a']*suffix_length
	    final_suffix = [chr(ord('a')+alphabet_size-1)]*suffix_length
	    while True:

		new_identifier = root + ''.join(suffix)
		if new_identifier not in self.used_identifiers:
		    self.used_identifiers.append(new_identifier)
		    return new_identifier

		if suffix == final_suffix:
		    break

		# Increment the suffix
		for i in range(1,suffix_length+1):
		    new_suffix_num = ord(suffix[-i])-ord('a')+1
		    suffix[-i] = chr((new_suffix_num%alphabet_size)+ord('a'))
		    if new_suffix_num < alphabet_size:
			    break

    def __bibtex_escape(self, text):
        return text.replace("{", "\\{")\
                   .replace("}", "\\}")\
                   .replace("\"","\"")\
		   .replace("&", "\\&")
        
    def format(self, work):
        if type(work) == worktype.JournalPaper:
            result = '@article{%s,\n' \
                     % self.__make_identifier(work)
            formatted_authors = [self.__format_author(a) for a in work.authors]
            result += " title = {%s},\n" % \
                      self.__format_title(self.__bibtex_escape(work.title))

            result += " author = {%s},\n" % \
                      self.__bibtex_escape(' and '.join(formatted_authors))

            result += " journal = {%s},\n" % self.__bibtex_escape(work.journal)
            result +=  " volume = {%s},\n" % self.__bibtex_escape(work.issue[0])
            if len(work.issue) > 1:
                result += " number = {%s},\n" % \
                          self.__bibtex_escape(work.issue[1])

            result += " pages = {%s},\n" % \
                      self.__bibtex_escape(self.__format_pages(work.pages))
            result += " year = {%d},\n" % \
                      work.date_published['date-parts'][0][0]
            result += " doi = {%s}\n}" % self.__bibtex_escape(work.doi)

            return result
        else:
            raise RuntimeError('TextFormatter does not support this work type.')


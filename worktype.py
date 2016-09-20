#!/usr/bin/env python

class Work(object):
    def __init__(self, json_data):
        self.json = json_data

class ConferenceProceeding(Work):
    def __init__(self, json_data):
        super(ConferenceProceeding, self).__init__(json_data)

class JournalPaper(Work):
    def __init__(self, json_data):
        super(JournalPaper, self).__init__(json_data)
        self.doi = json_data['DOI']
        self.title = json_data['title'][0]
        self.authors = json_data['author']
        lengths = [len(s) for s in json_data['container-title']]
        max_value = max(lengths)
        max_idx = lengths.index(max_value)
        self.journal = json_data['container-title'][max_idx]
        if json_data.has_key('published-print'):
            self.date_published = json_data['published-print']
        elif json_data.has_key('issued'):
            self.date_published = json_data['issued']
            
        self.pages = json_data['page']

        if json_data.has_key('issue'):
            self.issue = (json_data['volume'], json_data['issue'])
        else:
            self.issue = (json_data['volume'])

def parse_work(json_data):
    if json_data['type'] == 'proceedings-article':
        return ConferenceProceeding(json_data)
    elif json_data['type'] in ['journal-article', 'published-print']:
        return JournalPaper(json_data)
    else:
        raise RuntimeError('Unknown work type "%s".' % json_data['type'])

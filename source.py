#!/usr/bin/env python

import json
import re
import requests

import worktype

doi_regexp = re.compile("^((?:doi:)|(https?://dx.doi.org/))?(10(?:\.(?:[^./]+))+)/(.*)$", re.I)

def retrieve_from_doi(raw_doi):
    match = doi_regexp.match(raw_doi)
    if match is None:
        raise ArgumentError("Invalid DOI")

    prefix = match.group(3)
    suffix = match.group(4)

    doi = prefix + '/' + suffix
    doi_urlencoded = requests.utils.quote(prefix, '') \
                     + '/' + requests.utils.quote(suffix, '')

    work_url  = 'http://api.crossref.org/works/%s' % doi_urlencoded
    agency_url = work_url + '/agency'

    # First check that we have a Crossref DOI
    response = requests.get(agency_url)
    agency_data = json.loads(response.text)
    if agency_data['status'] != 'ok':
        raise RuntimeError('Error in agency data response.')
    elif agency_data['message-type'] != 'work-agency':
        raise RuntimeError('Received wrong response type.')
    elif agency_data['message']['agency']['id'] != 'crossref':
        raise RuntimeError('Unsupported registration authority.')

    # Next we can load the actual data
    response = requests.get(work_url)
    work_data = json.loads(response.text)
    if work_data['status'] != 'ok':
        raise RuntimeError('Error in agency data response.')
    elif work_data['message-type'] != 'work':
        raise RuntimeError('Received wrong response type.')

    return worktype.parse_work(work_data['message'])

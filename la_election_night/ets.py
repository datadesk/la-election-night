#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Records layors of fixed-width files published the Los Angeles County Registrar-Recorder/County Clerk
"""
import json
from .layouts import ETS
from itertools import groupby


class ETSParser(object):
    """
    Parses data provided in the Los Angeles County Registrar-Recorder/County Clerk's "ETS" file format.
    """
    layout_lookup = ETS

    def __init__(self, raw_data):
        self.raw_data = raw_data.split("\n")
        self.parsed_data = None

    def run(self):
        """
        Make it happen.
        """
        self.parsed_data = self._parse()
        return self.parsed_data

    def write(self, path, indent=4):
        """
        Writes the parsed data to the provided path as JSON.
        """
        if not self.parsed_data:
            raise Exception("Data has not been parsed. Call the object.")
        with open(path, 'w') as fh:
            json.dump(self.parsed_data, fh, indent=indent)

    def _parse(self):
        """
        Parses the provided file.
        """
        # Get a list of dicts for each line
        parsed_lines = []
        for i in self.raw_data:
            parsed_line = self._parse_line(i)
            # If it's not a "blank" line
            if parsed_line['record_type'] != 'BK':
                parsed_lines.append(parsed_line)

        # Group them by race
        grouped = []
        for key, group in groupby(parsed_lines, lambda x: (x['record_number'])):
            grouped.append(list(group))

        # Transform it
        transformed = {}
        for g in grouped:
            record_type = g[0]['record_type']
            redord_number = g[0]['record_number']
            # sigh
            if record_type in ['MC', 'MT']:
                transformed[redord_number] = self._parse_measure_contest(g)
            elif record_type == 'CC':
                transformed[redord_number] = self._parse_candidate_contest(g)

        return list(transformed.values())

    def _parse_int(self, value):
        """
        Parses the string format provided by the county into an integer.
        """
        try:
            return int(value.replace(',', ''))
        except ValueError:
            # If we can't parse it for an int return the OG string
            return value

    def _parse_float(self, value):
        """
        Parses the string format provided by the county into a float.
        """
        try:
            return float(value.replace(',', '')) / 100.0
        except ValueError:
            # If we can't parse it for an int return the OG string
            return value

    def _parse_line(self, value):
        """
        Takes one line from the ETS file, determines which
        type of record it is, and returns a parsed version.
        """
        # These fields are the same for everything
        parsed = {
            'record_number': value[0:3].strip(),
            'record_type': value[3:5].strip(),
            'race_id': value[5:9].strip(),  # this is basically meaningless
        }
        # Grab the custom string layout for the record type
        layout = self.layout_lookup[parsed['record_type']]
        for start, end, key in layout:
            if key:
                parsed[key] = value[start:end].strip()
        return parsed

    def _parse_candidate_contest(self, data):
        # get the title
        title_record = [i for i in data if i['record_type'] == 'CC'][0]
        # And the yes/nos
        results = [i for i in data if i['record_type'] == 'CN']
        # precincts reporting
        reporting = [i for i in data if i['record_type'] == 'PR'][0]
        # pull it all together
        return {
            'record_number': title_record['record_number'],
            'district': title_record['district'],
            'division': title_record['division'],
            'party_code': title_record['party_code'],
            'record_type': 'contest',
            'title': " ".join([title_record['title_1'], title_record['title_2']]).strip(),
            'precincts_total': self._parse_int(reporting['total_precincts']),
            'precincts_reporting': self._parse_int(reporting['precincts_reporting']),
            'precincts_reporting_pct': self._parse_float(reporting['precincts_reporting_pct']),
            'results': [{
                'name': i['name'],
                'votes': self._parse_int(i['votes']),
                'vote_pct': self._parse_float(i['vote_pct']),
                'party': i['party'],
                'party_code': i['party_code'],
            } for i in results]
        }

    def _parse_measure_contest(self, data):
        # get the title
        title_record = [i for i in data if i['record_type'] == 'MC'][0]
        # And the yes/nos
        results = [i for i in data if i['record_type'] == 'MT']
        # precincts reporting
        reporting = [i for i in data if i['record_type'] == 'PR'][0]
        # pull it all together
        return {
            'record_number': title_record['record_number'],
            'record_type': 'measure',
            'title': " ".join([title_record['title_1'], title_record['title_2']]).strip(),
            'precincts_total': self._parse_int(reporting['total_precincts']),
            'precincts_reporting': self._parse_int(reporting['precincts_reporting']),
            'precincts_reporting_pct': self._parse_float(reporting['precincts_reporting_pct']),
            'results': [{
                'name': i['text'].split("-")[-1].strip(),
                'votes': self._parse_int(i['votes']),
                'vote_pct': self._parse_float(i['vote_pct']),
                'party': ''
            } for i in results]
        }

    def _parse_judicial_contest(self, data):
        """
        We haven't gotten to this one yet. Patches welcome.
        """
        raise NotImplementedError


if __name__ == "__main__":
    pass

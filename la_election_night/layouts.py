#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Records layors of fixed-width files published the Los Angeles County Registrar-Recorder/County Clerk
"""


ETS = {
    # Election Title
    'ET': [
        (9, 15, None),
        (15, 68, 'election_text'),
        (68, 95, None),
    ],
    # Time & Date
    'TD': [
        (9, 15, None),
        (15, 20, 'time'),
        (20, 21, None),
        (21, 31, 'date'),
        (31, 95, None),
    ],
    # Election Statistics Record (??????)
    'ST': [
        (9, 15, None),
        (15, 41, 'text_1'),
        (41, 44, None),
        (44, 70, 'text_2'),
        (70, 95, None),
    ],
    # Candidate Contest Record
    'CC': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 41, 'title_1'),
        (41, 44, None),
        (44, 70, 'title_2'),
        (70, 95, None),
    ],
    # Measure Contest Record
    'MC': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, None),
        (15, 41, 'title_1'),
        (41, 44, None),
        (44, 70, 'title_2'),
        (70, 95, None),
    ],
    # Judicial Contest
    'JC': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, None),
        (15, 41, 'title_1'),
        (41, 44, None),
        (44, 70, 'title_2'),
        (70, 95, None),
    ],
    # Party (????????)
    'PT': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 41, 'party_name'),
        (41, 95, None),
    ],
    # Vote For Record (what the actual hell?!?!?!?!?!?!?!)
    'VF': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 37, 'text'),
        (37, 40, 'number'),
        (40, 95, None),
    ],
    # Candidate Name
    'CN': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 18, None),
        (18, 36, 'name'),
        (36, 41, None),
        (41, 44, 'party'),
        (44, 73, None),
        (73, 82, 'votes'),
        (82, 85, None),
        (85, 91, 'vote_pct'),
        (91, 95, None),
    ],
    # Measure Text
    'MT': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 18, None),
        (18, 22, 'measure_id'),  # ?
        (22, 25, None),
        (25, 57, 'text'),
        (57, 73, None),
        (73, 82, 'votes'),
        (82, 85, None),
        (85, 91, 'vote_pct'),
        (91, 95, None),
    ],
    # Judicial Name Record
    'JN': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 18, None),
        (18, 44, 'text'),
        (44, 45, None),
        (45, 63, 'name'),
        (63, 66, None),
        (66, 69, 'voting_rule'),  # ?
        (69, 73, None),
        (73, 82, 'votes'),
        (82, 85, None),
        (85, 91, 'vote_pct'),
        (91, 95, None),
    ],
    # Precincts Reporting Record
    'PR': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 35, 'precinct_total_text'),
        (35, 36, None),
        (36, 41, 'total_precincts'),
        (41, 53, None),
        (53, 73, 'precinct_reporting_text'),
        (73, 77, None),
        (77, 82, 'precincts_reporting'),
        (82, 85, None),
        (85, 91, 'precincts_reporting_pct'),
        (91, 95, None),
    ],
    # District Registration Record (OMG)
    'DR': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 31, 'text'),
        (31, 32, None),
        (32, 41, 'registration_count'),
        (41, 95, None),
    ],
    # Party Statistics
    #  THE SCHEMA ONLY ADDS TO 94?!
    'PS': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 32, None),
        (32, 41, 'registration'),
        (41, 44, None),
        (44, 70, 'name'),
        (70, 72, None),
        (72, 81, 'ballots_cast'),
        (81, 84, None),
        (84, 90, 'turnout_pct'),  # IT ALL ADDS UP UNTIL THE LAST ROW?!
        (90, 95, None),
    ],
    # Absentee Ballots Cast
    'AB': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 58, None),
        (58, 72, 'text'),
        (72, 73, None),
        (73, 82, 'absentee_ballots_cast'),
        (82, 95, None),
    ],
    # Ballots Cast Record
    'BC': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 52, None),
        (52, 72, 'text'),
        (72, 73, None),
        (73, 82, 'ballots_cast'),
        (82, 85, None),
        (85, 91, 'pct_turnout'),
        (91, 94, None),
    ],
    # Blank, for whatever reason
    'BK': [
        (9, 11, 'district'),
        (11, 14, 'division'),
        (14, 15, 'party_code'),
        (15, 95, None),
    ],
    # THE END
    'EF': [
        (9, 15, None),
        (15, 19, 'record_count'),
        (19, 95, None)
    ],
    # Things not in the docs (this is fun)
    'VN': [
        (9, 95, 'text')
    ]
}

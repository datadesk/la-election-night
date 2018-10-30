# la-election-night

Parse the results file published on election night by the Los Angeles County Registrar-Recorder/County Clerk

### Get started

Install the library from PyPI

```bash
$ pipenv install la-county-election-results
```

Import the library. Get the latest data from the live URL. That's it.

```python
>>> import la_election_night
>>> la_election_night.get()
[
    {
        "record_number": "001",
        "record_type": "measure",
        "title": "LA CO FLOOD CONTROL DIST MEASURE W",
        "precincts_total": 4551,
        "precincts_reporting": 4551,
        "precincts_reporting_pct": 1.0,
        "results": [
            {
                "name": "YES",
                "votes": 134294,
                "vote_pct": 0.6668999999999999,
                "party": ""
            },
            {
                "name": "NO",
                "votes": 67064,
                "vote_pct": 0.3331,
                "party": ""
            }
        ]
    },
    ...
```

You can example of how the data is parsed out can be seen [here](test_data/0018nov18-end.json).

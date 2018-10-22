# la-election-night

Parses election results data published online by the Los Angeles County Registrar-Recorder/County Clerk

### Get started

Install the library from PyPI

```bash
$ pipenv install la-county-election-results
```

Import the library. Pass it the path to an "ETS" file downloaded from the county's website. An example can be seen [here](test_data/0018nov18-end.ets).

```python
>>> import la_election_night
>>> ets_path = "/home/me/data/results.ets"
>>> parser = la_election_night.ETSParser(ets_path)
>>> data_dict = parser.run()
>>> print(data_dict)
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


### Still TK

* Scrape the data live from the county site with web request. This will be added once officials post the live links.

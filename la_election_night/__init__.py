import requests
from .ets import ETSParser


def get():
    """
    Get the latest results from the LA County ETS data service.
    """
    url = "http://rrcc.co.la.ca.us/results/0018nov18.ets"
    r = requests.get(url)
    raw_data = r.text
    parser = ETSParser(raw_data)
    return parser.run()


__all__ = (
    "get",
    "ETSParser",
)

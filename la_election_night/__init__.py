import requests
from .ets import ETSParser


def get(ets_url):
    """
    Get the results from the LA County ETS source available at the provided URL.
    """
    r = requests.get(ets_url)
    raw_data = r.text
    parser = ETSParser(raw_data)
    return parser.run()


__all__ = (
    "get",
    "ETSParser",
)

import pytest
from parsers.afisha_parser import AfishaParser

@pytest.fixture
def afisha_parser():
    return AfishaParser()

def test_fetch_events(afisha_parser):
    events = afisha_parser.fetch_events()
    assert isinstance(events, list)
    if events:
        assert "title" in events[0]
        assert "date" in events[0]
        print(events[0].get('title'))
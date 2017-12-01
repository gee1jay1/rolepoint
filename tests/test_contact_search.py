import os
import ujson as json

import pytest

from app.contact_search.utils import contact_search


@pytest.mark.parametrize('search_text, expected_matches_file', [
    ('', 'no_search_text.json'),
    ('b', 'b_search_text.json'),
    ('vincent', 'vincent_search_text.json'),
    ('westerlo', 'westerlo_search_text.json'),
])
def test_get_matching_contacts(search_text, expected_matches_file):
    """Ensure we match the correct contact results based on the
    search text.
    """
    test_matches = contact_search.get_matching_contacts(search_text)
    with open(os.path.join('expected_matches', expected_matches_file), 'r') as f:
        expected_matches = json.load(f)

    assert test_matches == expected_matches


@pytest.mark.parametrize('search_text', [
    ('ahdasdsad'),
    ('banana'),
    ('vinceent'),
    ('westerloo'),
])
def test_get_matching_contacts_no_reults(search_text):
    """Ensure we match no correct contact results based on the
    search text.
    """
    test_matches = contact_search.get_matching_contacts(search_text)

    assert test_matches == []

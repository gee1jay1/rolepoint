import os
import ujson as json


def get_contacts():
    """Read the json file containing all the contacts
    that we care about.
    """
    contacts_file = os.path.join(os.path.dirname(__file__), 'contacts.json')
    with open(contacts_file, 'r') as cf:
        contacts = json.load(cf)
    return contacts


def is_contact_match(search_text, contact):
    """True if search text matches the contact,
    False otherwise.
    """
    for key, value in contact.iteritems():
        # Job history has a list value so iterate.
        if key == 'job_history':
            for job in value:
                if search_text in job.lower():
                    return True
        else:
            if search_text in value.lower():
                return True
    return False


def get_matching_contacts(search_text):
    """Given a search term, return any contacts which
    match it. If there is no search term, return all contacts.
    """
    matches = []
    if search_text in ('', ' ', None):
        return CONTACTS
    for contact in CONTACTS:
        if is_contact_match(search_text, contact):
            matches.append(contact)

    return matches

# Pre load json file into memory for performance.
CONTACTS = get_contacts()

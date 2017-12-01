import ujson as json

from flask import request, render_template, flash, redirect, url_for
from wtforms import Form, StringField

from . import contact_search_bp
from utils import contact_search


class SearchForm(Form):
    """Ensure incoming text is valid. Given empty strings are
    allowed this doesn't do much but could be extended in future.
    """
    search_text = StringField('search_text')


@contact_search_bp.route('/')
def contact_search_form():
    """Present the search field."""
    return render_template('contact_search_form.html')


@contact_search_bp.route('/', methods=['POST'])
def contact_search_form_post():
    """From an incoming search term, return any contacts that match."""
    form = SearchForm(request.form)
    if form.validate():
        search_text = request.form['search_text']
        processed_text = search_text.lower()
        matches = contact_search.get_matching_contacts(processed_text)
        return json.dumps(matches)
    flash("Please enter valid text or empty search term")
    return render_template('contact_search_form.html')

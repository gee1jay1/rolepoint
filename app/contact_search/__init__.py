from flask import Blueprint

contact_search_bp = Blueprint('contact_search', __name__)

# To avoid circular dependencies.
from . import views

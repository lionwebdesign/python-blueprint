from flask import Blueprint

en_bp = Blueprint('en_bp', __name__)

@en_bp.route('/')
def index():
    return "english template"
from flask import Blueprint

es_bp = Blueprint('es_bp', __name__)

@es_bp.route('/')
def index():
    return "template en español"
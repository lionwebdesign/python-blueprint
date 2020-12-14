from flask import Blueprint

pt_bp = Blueprint('pt_bp', __name__)

@pt_bp.route('/')
def index():
    return "template em portugues"
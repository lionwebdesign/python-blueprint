from flask import Blueprint, render_template
from articulos.articulos_bp import articulos_bp

pt_bp = Blueprint('pt_bp', __name__)

@pt_bp.route('/')
def index():
    return render_template('/home.html')

app.register_blueprint(articulos_bp, url_prefix='/artigos')
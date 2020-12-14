from flask import Blueprint, render_template

articulos_bp = Blueprint('articulos_bp', __name__,
    template_folder='templates')

@app.route('/a-primeira-busqueda')
def aPrimeiraProcura():
    return render_template('./templates/la_primera_busqueda.html')
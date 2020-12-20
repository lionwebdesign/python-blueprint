from flask import Flask, Blueprint, render_template

pt_bp = Blueprint('pt_bp', __name__, template_folder='templates')

app = Flask(__name__)

@pt_bp.route('/')
def home():
    return render_template('pt_br/home.html')
    # return 'En serio no funciona?'

# @app.route('/productos')
# def productos():
#     return render_template('componentes/productos.html')

# @app.route('/outros-artigos')
# def outrosArtigos():
#     return render_template('componentes/outros-artigos.html')

# @app.route('/artigos/a-primeira-busqueda')
# def aPrimeiraProcura():
#     return render_template('artigos/a-primeira-busqueda.html')

if __name__ == '__main__':
    app.run(debug=True)
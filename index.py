from flask import Flask

from pt_br.pt_bp import pt_bp
# from es_mx.es_bp import es_bp
# from en_us.en_bp import en_bp

app = Flask(__name__)

app.register_blueprint(pt_bp, url_prefix='/pt-br')
# app.register_blueprint(es_bp, url_prefix='/es-mx')
# app.register_blueprint(en_bp, url_prefix='/en-us')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

from portugues.portugues_bp import portugues_bp

app = Flask(__name__)
app.register_blueprint(portugues_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug = True)
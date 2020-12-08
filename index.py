from flask import Flask
from blueprint import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)

@blueprint.route('/')
def index():
    return "This is an example app"

if __name__ == '__main__':
    app.run(debug=True)
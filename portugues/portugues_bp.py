from flask import Flask, Blueprint, render_template

portugues_bp = Blueprint("portugues_bp", 
                            __name__, 
                            template_folder= "templates",
                            static_folder="static",
                            static_url_path="/portugues/static")

@portugues_bp.route("/")
def portugues():
    return render_template('portugues/home.html')

@portugues_bp.route("/produtos")
def productos():
    return render_template('portugues/productos.html')

@portugues_bp.route("/artigos")
def catalogo_articulos():
    return render_template('portugues/catalogo-articulos.html')
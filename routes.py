from flask import render_template,url_for
from . import app


@app.route('/accueil')
def accueil():
    return render_template('accueil.html', title='Bienvenue dans notre boutique')


@app.route('/tous_produits')
def montrer_produits(): return '<h2>Nos produits</h2>'

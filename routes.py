from flask import render_template, url_for, request, redirect
from . import app, models
from .models import Vue_agents_maisons


@app.route("/accueil")
def accueil():
    liste_categories = models.Vue_agents_maisons.query.distinct('type_maison')
    print(liste_categories)  # Add this line
    return render_template('accueil.html', title='Bienvenue dans notre boutique', liste_cat=liste_categories)


@app.route('/tous_produits')
def produits():
    liste_produits = models.Vue_agents_maisons.query.all()
    return render_template('tous_produits.html', title='Nos produits', liste_prod=liste_produits)


@app.route('/produits_categorie')
def produits_categorie():
    type_maison = request.args.get('type_maison')
    produits = models.Vue_agents_maisons.query.filter_by(type_maison=type_maison).all()
    return render_template('produits_categorie.html', produits=produits)


@app.route("/about")
def about():
    return render_template('about.html', title='À propos')

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search')
        results = models.Vue_agents_maisons.query.filter(
            (models.Vue_agents_maisons.titre_maison.contains(search_term)) |
            (models.Vue_agents_maisons.ville.contains(search_term))
        ).all()
        return render_template('search_results.html', title='Résultats de recherche', results=results)
    return render_template('search.html', title='Recherche')

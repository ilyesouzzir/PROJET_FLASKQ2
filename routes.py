from flask import render_template, url_for, request, redirect
from . import app, models
from .forms import AjoutProduitForm
from .models import Vue_agents_maisons
from .models import Maison
@app.route("/accueil")
def accueil():
    liste_categories = models.Vue_agents_maisons.query.distinct('type_maison')
    print(liste_categories)  # Add this line
    return render_template('accueil.html', title='Bienvenue dans notre boutique', liste_cat=liste_categories)



@app.route('/ajouter_produit', methods=['GET', 'POST'])
def ajouter_produit():
    form = AjoutProduitForm()
    if form.validate_on_submit():
        # Créez une nouvelle instance de Maison avec les données du formulaire
        nouvelle_maison = Maison(
            titre_maison=form.titre_maison.data,
            type_maison=form.type_maison.data,
            surface=form.surface.data,
            annee_construction=form.annee_construction.data,
            ville=form.ville.data,
            prix=form.prix.data,
            image_maison=form.image_maison.data,
            id_agent=form.id_agent.data  # Changez cette ligne
        )
        # Ajoutez la nouvelle maison à la session
        models.db.session.add(nouvelle_maison)
        # Sauvegardez les changements dans la base de données
        models.db.session.commit()
        # Redirigez l'utilisateur vers la page d'accueil
        return redirect(url_for('accueil'))
    return render_template('ajouter_produit.html', form=form)
@app.route('/tous_produits')
def produits():
    liste_produits = models.Vue_agents_maisons.query.all()
    return render_template('tous_produits.html', title='Nos produits', liste_prod=liste_produits)

@app.route('/produits_categorie')
def produits_categorie():
    type_maison = request.args.get('type_maison')
    produits = models.Vue_agents_maisons.query.filter_by(type_maison=type_maison).all()
    return render_template('produits_categorie.html', produits=produits)
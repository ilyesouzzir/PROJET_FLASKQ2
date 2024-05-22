from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AjoutProduitForm(FlaskForm):
    titre_maison = StringField('Titre', validators=[DataRequired()])
    type_maison = StringField('Type', validators=[DataRequired()])
    surface = IntegerField('Surface', validators=[DataRequired()])
    annee_construction = IntegerField('Année de construction', validators=[DataRequired()])
    ville = StringField('Ville', validators=[DataRequired()])
    prix = IntegerField('Prix', validators=[DataRequired()])
    image_maison = StringField('Image URL')
    maison_agent_id = IntegerField('Agent ID', validators=[DataRequired()])
    submit = SubmitField('Ajouter')
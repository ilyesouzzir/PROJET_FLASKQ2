from . import app, db
from flask_sqlalchemy import SQLAlchemy


class Vue_agents_maisons(db.Model):
    id_maison = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, primary_key=True)
    nom_agent = db.Column(db.String(25), nullable=False)
    prenom_agent = db.Column(db.String(25), nullable=False)
    telephone_agent = db.Column(db.String(20), nullable=False)
    image_agent = db.Column(db.String(200), nullable=True)
    description_agent = db.Column(db.String(200), nullable=True)
    titre_maison = db.Column(db.String(50), nullable=False)
    type_maison = db.Column(db.String(50), nullable=False)
    surface = db.Column(db.Integer, nullable=False)
    annee_construction = db.Column(db.Integer, nullable=False)
    ville = db.Column(db.String(50), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    image_maison = db.Column(db.String(200), nullable=True)
    maison_agent_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f'{self.agent_id} : {self.nom_agent} : {self.prenom_agent} : {self.telephone_agent} : '
                f'{self.image_agent} : {self.description_agent} : {self.id_maison} : {self.titre_maison} : '
                f'{self.type_maison} : {self.surface} : {self.annee_construction} : {self.ville} : '
                f'{self.prix} : {self.image_maison} : {self.maison_agent_id}')

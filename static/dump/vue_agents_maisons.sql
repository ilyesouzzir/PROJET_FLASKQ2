CREATE VIEW vue_agents_maisons AS
SELECT 
    agent_immobilier.id_agent AS agent_id, 
    agent_immobilier.nom AS nom_agent, 
    agent_immobilier.prenom AS prenom_agent, 
    agent_immobilier.n_tel AS telephone_agent, 
    agent_immobilier.image_agent, 
    agent_immobilier.description AS description_agent,
    maison.id_maison, 
    maison.titre_maison,
    maison.type_maison,
    maison.surface,
    maison.annee_construction,
    maison.ville, 
    maison.prix,
    maison.image_maison,
    maison.id_agent AS maison_agent_id  -- renommer cette colonne
FROM 
    agent_immobilier
JOIN 
    maison 
ON 
    agent_immobilier.id_agent = maison.id_agent;

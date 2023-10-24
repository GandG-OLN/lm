from odoo import models, fields, _, api
from datetime import datetime

class LettreMission(models.Model):
    
    _name = "lettre.mission"
    date_doc = fields.Date(String='Date du cocument', required=True)
    type_mission = fields.Selection([('mission_odoo', 'Mission Odoo'), ('mission_expertise', 'Mission Expertise'), ('mission_audit', 'Mission Audit'), ('mission_rh', 'Mission RH'), ('mission_taxeandlegal', 'Mission taxe & légal'), ('mission_coatching', 'Mission coatching'), ('mission_conseil', 'Mission conseil')], String='Type de la mission', required=True, default="mission_expertise")
    partner_id = fields.Many2one("res.partner", String='Client')
    titre_mission = fields.Char(String='Titre de la mission', required=True)
    objet_mission = fields.Char(String='Objet de la mission', required=True)
    titre_personne_contact = fields.Text(String='Titre de la personne contact', required=True)
    capital_entreprise = fields.Char(String='Capital de l\'entreprise')
    registre_de_commerce = fields.Char(String='Registre de commerce du client')
    adresse_client = fields.Text(String ='Adresse du client', required=True)
    description_activite = fields.Text(String = 'Description de l\'activité du client')
    obligation_prestataire = fields.Text(String ='Obligation du préstataire')
    prix_prestation = fields.Text(String='Prix de la prestation')
    prix_maintenance = fields.Text(String='Prix de la maintenance')
    condition_paiement = fields.Text(String='Condition de paiement')
    date_renouvellement = fields.Text(String='Date de renouvellement')
    prix_prestation_odoo = fields.Text(String='Prix de la prestation de odoo')
    etude_de_la_mission = fields.Text(String='Etude de la mission')
    paragraphe_sup1 = fields.Text(String='Paragraphe supplémentaire 1')
    paragraphe_sup2 = fields.Text(String='Paragraphe supplémentaire 2')
    reference = fields.Char(string='Référence', required=True, copy=False, readonly=True, 
                            states={'brouillon': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    code_bu = fields.Char(string='Code de la BU', required=True)
    code_mission = fields.Char(string='Code de la mission', required=True)
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    genre = fields.Selection([('monsieur', 'Monsieur'), ('madame', 'Madame')], required=True)
    date_debut = fields.Date(String="Date de début", required=True)
    date_fin = fields.Date(String="Date de fin", required=True)






    state = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('confirmer', 'Confirmer'),
        ('valider', 'Valider')],
        string="Etat", default="brouillon")
    
    def action_for_validation(self):
        self.write({'state': 'confirmer'})

    def action_valide(self):
        self.write({'state': 'valider'})

    def action_remettre_brouillon(self):
        self.write({'state': 'brouillon'})

    @api.model
    def create(self, vals):
        if not vals.get('titre_mission'):
            vals['titre_mission'] = 'Nouvelle mission'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('lettre.mission').replace('$code_bu', vals.get('code_bu')).replace('$code_mission', vals.get('code_mission')) or _('New')
        res = super(LettreMission, self).create(vals)
        return res





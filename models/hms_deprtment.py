from odoo import models, fields

class HMSDeprtment(models.Model):
    _name="hms.deprtmant"

    name = fields.Char()
    capacity = fields.Integer()
    is_oppened = fields.Boolean()
    
    patient_id = fields.Many2one(comodel_name="hms.patient")
    patient_name = fields.Char(related="patient_id.firstName")

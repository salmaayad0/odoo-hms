from odoo import models, fields

class HMSDoctor(models.Model):
    _name="hms.doctor"
    _rec_name="firstName"

    firstName=fields.Char()
    lastName=fields.Char()
    image = fields.Image()
    patient_ids = fields.One2many(comodel_name="hms.deprtmant", inverse_name="patient_id")
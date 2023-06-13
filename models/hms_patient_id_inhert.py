from odoo import models, fields
from odoo.exceptions import ValidationError

class HMSPatientIdInhertance(models.Model):
    _inherit="res.partner"

    related_patient_id = fields.Many2one(comodel_name="hms.patient")
    vat = fields.Char(required=True)
    display_name = fields.Char()
     
    _sql_constraints = [
        ( 'email' ,'UNIQUE(email)' ,'email has to be Unique') ,
    ]
    
    # unlink function
    # def unlink(self):
    #     for rec in self:
    #         if len(rec.related_patient_id) != 0 :
    #             raise ValidationError('You can\'t delete a customer that is related to patient')
    #         return super().unlink()

    
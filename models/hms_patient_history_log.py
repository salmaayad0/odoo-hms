from odoo import models, fields

class HMSPatientHistoryLog(models.Model):
    _name = "hms.historylog"

    description = fields.Text()

    logs_id=fields.Many2one(comodel_name="hms.patient")
    
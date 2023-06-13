from odoo import models, fields, api
import re
from datetime import date
from odoo.exceptions import ValidationError

class HMSPatient(models.Model):
    _name = "hms.patient"
    # _rec_name = "firstName"

    firstName = fields.Char(required=True)
    lastName = fields.Char(required=True)
    birthDate = fields.Date()
    address = fields.Text()
    age = fields.Integer(compute="compute_age")
    history = fields.Html()
    CR_ratio = fields.Float()
    bloodType = fields.Selection([('o','o'),('a','a'),('b','b'),('ab','ab')])
    PCR = fields.Boolean()
    image = fields.Image()
    email = fields.Char()

    department_id = fields.Many2one(comodel_name="hms.deprtmant")
    department_capacity = fields.Integer(related="department_id.capacity")

    doctors_ids = fields.Many2many(comodel_name="hms.doctor")

    history_logs = fields.One2many(comodel_name="hms.historylog", inverse_name="logs_id")

    state = fields.Selection([
        ('Undetermined','Undetermined'),
        ('Serious','Serious'),
        ('Fair','Fair'),
        ('Good','Good')
        ])
    
    _sql_constraints = [
        ( 'email' ,'UNIQUE(email)' ,'email has to be Unique') ,
    ]


    #state button
    def state_approve(self):
        self.firstName = True

    #state change warning mss   
    @api.onchange('state')
    def show_warning_message(self):
        if self.state:
            return {
                'state changed': {
                    'title': ('state changed'),
                    'message': 'patient state is changed %s' % (self.state)
                }
            }
        
    #change on pcr
    @api.onchange('PCR')
    def pcr_checked(self):
        if self.PCR:
            if self.age < 30:
               self.PCR = True 
            return {
                'PCR changed': {
                    'title': ('PCR changed'),
                    'message': 'patient PCR is checked %s' %(self.PCR)
                }
            }
    

    #creat log table on history
    @api.onchange('history')
    def history_changed(self):
        if self.history:
            logs = {
                'description': 'the patient history Changed to %s' %(self.history),
                'logs_id' : self.id
            }

            self.env['hms.historylog'].create(logs)

    # email validation
    @api.constrains("email")
    def email_validation(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                             self.email)
            if match == None:
                raise ValidationError('Not a valid email it must have (@ and .)')
            

    # age computed function
    @api.depends('birthDate')
    def compute_age(self):
        for rec in self:
            if rec.birthDate:
                today = date.today()
                rec.age = today.year - rec.birthDate.year
                - ((today.month, today.day) < (rec.birthDate.month, rec.birthDate.day))
            else:
                rec.age = 0
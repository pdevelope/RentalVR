from odoo import models, fields
class ControlVR(models.Model):
    _inherit = 'controlvr'
    priority = fields.Selection([
                                ('0','Low'),
                                ('1','Normal'),
                                ('2','High')],
                                'Priority',default='1')
    kanban_state = fields.Selection([
                                ('normal', 'In Progress'),
                                ('blocked', 'Blocked'),
                                ('done', 'Ready for next stage')],
                                'Kanban State',default='normal')
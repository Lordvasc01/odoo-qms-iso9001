# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Version(models.Model):

    _name = "qms.version"

    version = fields.Char()

    change_history = fields.Html()

    date_open = fields.Date()

    document_id = fields.Many2one(
        comodel_name='qms.document',
        ondelete='cascade'        
    )

    procedure_id = fields.Many2one(
        comodel_name='qms.procedure',
        ondelete='cascade'
    )

    instructive_id = fields.Many2one(
        comodel_name='qms.instructive',
        ondelete='cascade'
    )

    registry_id = fields.Many2one(
        comodel_name='qms.registry',
        ondelete='cascade'
    )        

    responsible_id = fields.Many2one(
        comodel_name='qms.interested_party',
        required=True
    )        

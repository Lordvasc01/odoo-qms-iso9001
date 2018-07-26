# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Indicator(models.Model):

    _name = "qms.indicator"

    name = fields.Char(
        required=True
    )

    _resource_states_ = [
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled')
    ]

    responsible_id = fields.Many2one(
        comodel_name='qms.interested_party',
        required=True
    )

    review_ids = fields.One2many(
        comodel_name='qms.review',
        inverse_name='indicator_id'
    )

    state = fields.Selection(
        selection=_resource_states_,
        default='enabled'
    )

    process_id = fields.Many2one(
        comodel_name='qms.process',
        required=True
    )

    measurement_ids = fields.One2many(
        comodel_name='qms.indicator.measurement',
        inverse_name='indicator_id',
    )

    description = fields.Html()

    last_measurement_date = fields.Date(compute='_compute_last_measurement_date')

    last_measurement_result = fields.Char(compute='_compute_last_measurement_result')

    last_review_date = fields.Date(compute='_compute_last_review_date')

    @api.multi
    @api.depends('measurement_ids')
    def _compute_last_measurement_date(self):
        for indicator in self:
            domain = [
                ('indicator_id', '=', indicator.id),
                #('modify_concession', '=', True)
            ]
            related_measurement = indicator.env['qms.indicator.measurement'].search(domain)
            last_measurement = related_measurement.sorted(
                key=lambda r: r.measurement_date,
                reverse=True)
            indicator.last_measurement_date = last_measurement[0].measurement_date

    @api.multi
    @api.depends('measurement_ids')
    def _compute_last_measurement_result(self):
        for indicator in self:
            domain = [
                ('indicator_id', '=', indicator.id),
                #('modify_concession', '=', True)
            ]
            related_measurement = indicator.env['qms.indicator.measurement'].search(domain)
            last_measurement = related_measurement.sorted(
                key=lambda r: r.measurement_date,
                reverse=True)
            indicator.last_measurement_result = last_measurement[0].result

    @api.multi
    @api.depends('review_ids')
    def _compute_last_review_date(self):
        for indicator in self:
            domain = [
                ('indicator_id', '=', indicator.id),
                #('modify_concession', '=', True)
            ]
            related_reviews = indicator.env['qms.review'].search(domain)
            last_review = related_reviews.sorted(
                key=lambda r: r.date,
                reverse=True)
            indicator.last_review_date = last_review[0].date

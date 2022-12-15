# -*- coding: utf-8 -*-

from odoo import models, fields


class EventReport(models.TransientModel):
    _name = 'event.report'

    from_date = fields.Date('Date From', required=True)
    to_date = fields.Date('Date To', required=True)
    event_type_id = fields.Many2one('event.property')
    is_catering = fields.Boolean('Include catering')

    def print_report(self):
        data = {
            'form': self.read()[0]
        }
        return self.env.ref('event_management.action_report_event').report_action(self, data=data)

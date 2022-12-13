# -*- coding: utf-8 -*-

from odoo import models, fields


class WarningWizard(models.TransientModel):
    _name = 'warning'

    # message = fields.Text(string="Quantity should be in the range")
    #                       # , readonly=True)

    def action_accept(self):
        res = self.env['stock.picking'].browse(self.env.context.get('active_ids'))
        res.write({'state': 'done'})

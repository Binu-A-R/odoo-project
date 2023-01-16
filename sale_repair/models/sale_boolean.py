# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleRepair(models.Model):
    _inherit = 'sale.order'

    is_repair = fields.Boolean('Repair')

    @api.onchange('partner_id')
    def pending_repair(self):
        if self.partner_id:
            print(self.partner_id)
            x = self.partner_id
            orders_present = self.env['sale.repair'].search([('partner_id', '=', x.id)])
            print(orders_present)
            if orders_present:
                return {'warning': {'title': _('Warning'), 'message': _('This user has some pending repair requests.')}}

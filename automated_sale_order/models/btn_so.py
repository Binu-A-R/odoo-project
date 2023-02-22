# -*- coding: utf-8 -*-
from odoo import models


class AutomatedSaleOrder(models.Model):
    _inherit = 'product.product'

    def action_create_so(self):
        print('-------created sale-------')

        return {
            'name': 'Create SO',
            'type': 'ir.actions.act_window',
            'res_model': 'create_so.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': self.id}
        }

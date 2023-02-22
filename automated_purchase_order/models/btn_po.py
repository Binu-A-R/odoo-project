# -*- coding: utf-8 -*-
from odoo import models


class AutomatedPurchaseOrder(models.Model):
    _inherit = 'product.product'

    def action_create_po(self):
        print('-------created purchase po-------')

        return {
            'name': 'Create PO',
            'type': 'ir.actions.act_window',
            'res_model': 'create_po.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': self.id}
        }

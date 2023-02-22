# -*- coding: utf-8 -*-

from odoo import models, fields


class CreatePOWizard(models.TransientModel):
    _name = 'create_po.wizard'

    product_id = fields.Many2one('product.product', string='Product')
    partner_id = fields.Many2one('res.partner', string='Vendor')
    quantity = fields.Float(string='Quantity')
    price = fields.Float(string='Price', related='product_id.standard_price')

    def action_confirm(self):
        rfq = self.env['purchase.order'].search([('state', '=', 'draft'), ('partner_id', '=', self.partner_id.id)])
        if not rfq:
            rfq = self.env['purchase.order'].create({
                'partner_id': self.partner_id.id,
                'order_line': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_qty': self.quantity,
                    'price_unit': self.price
                })]
            })

        else:
            rfq.write({
                'order_line': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_qty': self.quantity,
                    'price_unit': self.price
                })]
            })

        rfq.button_confirm()

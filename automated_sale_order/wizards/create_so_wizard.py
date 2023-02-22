# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateSOWizard(models.TransientModel):

    _name = 'create_so.wizard'

    product_id = fields.Many2one('product.product', string='Product')
    partner_id = fields.Many2one('res.partner', string='Customer')
    quantity = fields.Float(string='Quantity')
    price = fields.Float(string='Price', related='product_id.lst_price')

    def action_so_confirm(self):
        print("confirm")

        so = self.env['sale.order'].search([('state', '=', 'draft'), ('partner_id', '=', self.partner_id.id)])
        if not so:
            so = self.env['sale.order'].create({
                'partner_id': self.partner_id.id,
                'order_line': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_uom_qty': self.quantity,
                    'price_unit': self.price
                })]
            })
        else:
            so.write({
                'order_line': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_uom_qty': self.quantity,
                    'price_unit': self.price
                })]
            })

        so.action_confirm()

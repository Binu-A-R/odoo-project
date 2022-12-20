# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseApprovalBlock(models.Model):
    _inherit = 'purchase.order'

    purchase_approval_id = fields.Many2one('approval_block.approval', compute='compute_price_subtotal', default=" ")

    @api.depends('order_line.price_subtotal')
    def compute_price_subtotal(self):
        total = sum(self.order_line.mapped('price_subtotal'))
        print('total--->', total)
        print(total)
        search = self.env['approval_block.approval'].search([])
        print('search--->', search)
        record = search.mapped("amount")
        print('record--->', record)
        res = sorted(record, key=lambda x: abs(x - total))[0]
        print('result-->', res)
        result = self.env['approval_block.approval'].search([('amount', '=', float(res))])
        print('final result --->', result)
        self.purchase_approval_id = result

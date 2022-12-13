# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToleranceFieldPurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    purchase_tolerance = fields.Float('Tolerance', related='order_id.partner_id.tolerance', readonly=False)

    @api.model_create_multi
    def _prepare_stock_moves(self, picking):
        res = super(ToleranceFieldPurchaseOrderLine, self)._prepare_stock_moves(picking)
        for rec in res:
            rec['stock_tolerance'] = self.purchase_tolerance
        return res

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToleranceFieldSaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    sale_tolerance = fields.Float('Tolerance', related='order_id.partner_id.tolerance', readonly=False)

    @api.model_create_multi
    def _prepare_procurement_values(self, group_id=False):
        res = super(ToleranceFieldSaleOrderLine, self)._prepare_procurement_values(group_id)
        res.update({'stock_tolerance': self.sale_tolerance})
        return res

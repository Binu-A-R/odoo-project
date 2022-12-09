# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToleranceFieldSaleOrder(models.Model):

    _inherit = "sale.order"
    sale_tolerance_ids = fields.One2many('sale.order.line', 'sale_tolerance_id')
    sale_tolerance = fields.Float('Tolerance', readonly=False)


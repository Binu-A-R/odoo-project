# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToleranceFieldSaleOrderLine(models.Model):

    _inherit = "sale.order.line"
    sale_tolerance_id = fields.Many2one("res.partner")
    sale_tolerance = fields.Float('Tolerance', related='sale_tolerance_id.tolerance', readonly=False,compute='compute')



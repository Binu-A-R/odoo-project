# -*- coding: utf-8 -*-

from odoo import models, fields


class ToleranceFieldSaleOrderLine(models.Model):

    _inherit = "purchase.order.line"

    purchase_tolerance = fields.Char('Tolerance')


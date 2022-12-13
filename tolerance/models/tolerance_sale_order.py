# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToleranceFieldSaleOrder(models.Model):

    _inherit = "sale.order"
    sale_tolerance = fields.Float('Tolerance')


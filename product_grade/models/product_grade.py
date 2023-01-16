# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductOwner(models.Model):

    _inherit = 'product.template'

    product_grade = fields.Selection(selection=[('A', 'A'), ('B', 'B'),('C', 'C'), ('D', 'D'), ('E', 'E')])


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):

        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('product_grade')
        return result

# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductOwner(models.Model):

    _inherit = 'product.template'

    product_owner_id = fields.Many2one('res.partner', string='Product Owner')


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('product_owner_id')
        print('result----->', result)
        print('resultfvf', result['search_params'])
        print('resultfvfsdfwecf', result['search_params']['fields'])
        return result

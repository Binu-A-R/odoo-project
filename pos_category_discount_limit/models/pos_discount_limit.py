# -*- coding: utf-8 -*-

from odoo import fields, models


class ConfigInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_category_id = fields.Many2many('pos.category',
                                       related="pos_config_id.category_discount_ids", readonly=False)
    discount_value = fields.Float(string="Maximum discount limit",related='pos_config_id.discount_value',readonly=False)
    is_pos_discount_limit = fields.Boolean(related='pos_config_id.is_discount_limit_categories', readonly=False)

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result += ['res.config.settings']
        print(('hdbjskfl'), result)
        return result

    def _loader_params_res_config_settings(self):
        print('nfjkjk')
        # print('search_params',search_params)
        return {
            'search_params': {
                'fields': [
                    'pos_category_id',
                    'discount_value',
                ]

            }
        }

    def _get_pos_ui_res_config_settings(self, params):
        return self.env['res.config.settings'].search_read(**params['search_params'])

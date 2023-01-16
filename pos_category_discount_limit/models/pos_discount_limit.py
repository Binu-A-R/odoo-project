# -*- coding: utf-8 -*-

from odoo import fields, models


class ConfigInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_category_id = fields.Many2many('pos.category',
                                       related="pos_config_id.category_discount_ids", readonly=False)
    discount_value = fields.Float(string="Maximum discount limit")


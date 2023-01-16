from odoo import fields, models


class PosDiscountLimit(models.Model):
    _inherit = 'pos.config'

    category_discount_ids = fields.Many2many('pos.category', 'rel_category_discount_limit_ids', 'category_id')
    discount_value = fields.Float(string="Maximum discount limit")
    is_discount_limit_categories = fields.Boolean("Category Discount")

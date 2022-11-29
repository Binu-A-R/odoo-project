from odoo import fields, models


class CateringMenu(models.Model):
    _name = 'catering.menu'
    _rec_name = 'dish_name'

    dish_name = fields.Char('Name')
    category = fields.Selection(selection=[('Welcome Drink', 'Welcome Drink'),
                                ('Break Fast', 'Break Fast'), ('Lunch', 'Lunch'),
                                ('Dinner', 'Dinner'), ('Snacks and Drinks', 'Snacks and Drinks'),
                                ('Beverages', 'Beverages')])
    catering_image = fields.Binary("Image")
    uom_id = fields.Many2one('uom.uom', string='UOM')
    company_id = fields.Many2one('res.company', string="Company")
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id, invisible="1")
    unit_price = fields.Monetary(string="Unit price")
    relation_id = fields.Many2one('catering', string='Menu')
    category_welcome_drink_id = fields.Many2one('catering.menu', domain=[('category', '=', 'Welcome Drink')])
    category_break_fast_id = fields.Many2one('catering.menu', domain=[('category', '=', 'Break Fast')])
    category_lunch_id = fields.Many2one('catering.menu', domain=[('category', '=', 'Lunch')])
    category_dinner_id = fields.Many2one('catering.menu', domain=[('category', '=', 'Dinner')])
    category_snack_drinks_id = fields.Many2one('catering.menu', domain=[('category', '=', 'Snacks and Drinks')])
    category_beverages_id = fields.Many2one('catering.menu', domain=[('category', '=', 'Beverages')])






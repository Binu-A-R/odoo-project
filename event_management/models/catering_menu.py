from odoo import fields, models


class CateringMenu(models.Model):
    _name = 'catering.menu'

    dish_name = fields.Char('Name')
    category = fields.Selection(selection=[('Welcome Drink', 'welcome drink'),
                                ('Break Fast', 'break fast'), ('Lunch', 'lunch'),
                                ('Dinner', 'dinner'), ('Snacks and Drinks', 'snacks and drinks'),
                                ('Beverages', 'beverages')])
    catering_image = fields.Binary("Image")
    # uom_id = fields.Many2one(comodel_name='uom.uom', string='UOM')
    company_id = fields.Many2one('res.company', string="Company")
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    unit_price = fields.Monetary(string="Unit price")

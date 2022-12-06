# -*- coding: utf-8 -*-

from odoo import fields, models


class CateringMenu(models.Model):
    _name = 'catering.menu'
    _rec_name = 'dish_name'

    dish_name = fields.Char('Name', required=True)
    category = fields.Selection(selection=[('Welcome Drink', 'Welcome Drink'),
                                ('Break Fast', 'Break Fast'), ('Lunch', 'Lunch'),
                                ('Dinner', 'Dinner'), ('Snacks and Drinks', 'Snacks and Drinks'),
                                ('Beverages', 'Beverages')], required=True)
    catering_image = fields.Binary("Image")
    uom_id = fields.Many2one('uom.uom', string='UOM')
    unit_price = fields.Monetary(string="Unit price", required=True)

    company_id = fields.Many2one('res.company', string="Company")
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    price_subtotal = fields.Monetary(string="Subtotal")

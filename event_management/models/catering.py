# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class Catering(models.Model):
    _name = "catering"
    _rec_name = 'name_sequence'

    event_id = fields.Many2one('event.booking', string='Event', required=True)
    date = fields.Date('Booking Date', related='event_id.booking_date')
    start_date = fields.Datetime(related='event_id.start_date')
    end_date = fields.Datetime(related='event_id.end_date')
    guest = fields.Integer("Number of guests", default='1')
    name_sequence = fields.Char(string='Order Reference', readonly=True, default=lambda self: _('New'))
    is_welcome_drink = fields.Boolean(string='Welcome Drink')
    is_break_fast = fields.Boolean('Break Fast')
    is_lunch = fields.Boolean('Lunch')
    is_dinner = fields.Boolean('Dinner')
    is_snack_drinks = fields.Boolean('Snacks and Drinks')
    is_beverages = fields.Boolean('Beverages')
    category_welcome_drink_ids = fields.One2many('catering.line', 'welcome_drinks_menu_id', string="Welcome Drinks")
    category_break_fast_ids = fields.One2many('catering.line', 'break_fast_menu_id', string="Break Fast")
    category_lunch_ids = fields.One2many('catering.line', 'lunch_menu_id', string="Lunch")
    category_dinner_ids = fields.One2many('catering.line', 'dinner_menu_id', string="Dinner")
    category_snack_drinks_ids = fields.One2many('catering.line', 'snacks_drink_menu_id', string="Snacks and Drinks")
    category_beverages_ids = fields.One2many('catering.line', 'beverages_menu_id', string="Beverages")


    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('deliver', 'Delivered'),
            ('invoice', 'Invoiced'),
            ('expired', 'Expired'),
        ], default="draft"
    )
    grand_total = fields.Float(string="Grand total", compute='_compute_grand_total', store=True)

    @api.depends('category_welcome_drink_ids.price_subtotal', 'category_break_fast_ids.price_subtotal',
                 'category_lunch_ids.price_subtotal', 'category_dinner_ids.price_subtotal',
                 'category_snack_drinks_ids.price_subtotal', 'category_beverages_ids.price_subtotal')
    def _compute_grand_total(self):
        self.grand_total = sum((self.category_welcome_drink_ids.mapped('price_subtotal')) +
                               (self.category_break_fast_ids.mapped('price_subtotal')) +
                               (self.category_lunch_ids.mapped('price_subtotal')) +
                               (self.category_dinner_ids.mapped('price_subtotal')) +
                               (self.category_snack_drinks_ids.mapped('price_subtotal')) +
                               (self.category_beverages_ids.mapped('price_subtotal')))

    def action_confirm(self):
        self.state = 'confirm'


    def action_deliver(self):
        self.state = 'deliver'

    @api.model
    def validation_cron(self):
        current_date = datetime.now()
        res = 0
        print(current_date)
        for rec in self.search([('state', '!=', 'confirm')]):
            if rec.end_date:
                print(rec.end_date)
                if current_date > rec.end_date:
                    print("expired")
                    res = rec.write({'state': 'expired'})
                else:
                    res = rec.write({'state': 'draft'})
        return res

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code(
                'catering.sequence') or _('New')
            res = super(Catering, self).create(vals)
            return res


class CateringLine(models.Model):
    _name = "catering.line"
    _description = "Catering Line"

    welcome_drinks_menu_id = fields.Many2one('catering')
    break_fast_menu_id = fields.Many2one('catering')
    lunch_menu_id = fields.Many2one('catering')
    dinner_menu_id = fields.Many2one('catering')
    snacks_drink_menu_id = fields.Many2one('catering')
    beverages_menu_id = fields.Many2one('catering')
    menu_id = fields.Many2one('catering.menu', string='Item')
    description = fields.Char(string='Description')
    quantity = fields.Integer(string='Quantity', default='1')
    uom_id = fields.Many2one('uom.uom', related='menu_id.uom_id')
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    unit_price = fields.Monetary(string='Unit Price', related='menu_id.unit_price')
    price_subtotal = fields.Monetary(string='subtotal')

    @api.onchange('unit_price', 'quantity')
    def _onchange_price_subtotal(self):
        self.price_subtotal = self.unit_price * self.quantity

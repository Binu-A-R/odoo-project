from odoo import models, fields, api, _
from datetime import datetime


class Catering(models.Model):
    _name = "catering"
    _rec_name = 'name_sequence'

    event_id = fields.Many2one('event.booking', string='Event', required=True)
    date = fields.Date('event.booking', related='event_id.booking_date')
    start_date = fields.Date('event.booking', related='event_id.start_date')
    end_date = fields.Date('event.booking', related='event_id.end_date')
    guest = fields.Integer("Number of guests", default='1')
    name_sequence = fields.Char(string='Order Reference', required=True, readonly=True, default=lambda self: _('New'))
    welcome_drink = fields.Boolean(string='Welcome Drink')
    break_fast = fields.Boolean('Break Fast')
    lunch = fields.Boolean('Lunch')
    dinner = fields.Boolean('Dinner')
    snack_drinks = fields.Boolean('Snacks and Drinks')
    beverages = fields.Boolean('Beverages')

    category_welcome_drink_ids = fields.One2many('catering.line', 'catering_menu_id', string="Welcome Drinks")
    category_break_fast_ids = fields.One2many('catering.line', 'catering_menu_id', string="Break Fast")
    category_lunch_ids = fields.One2many('catering.line', 'catering_menu_id', string="Lunch")
    category_dinner_ids = fields.One2many('catering.line', 'catering_menu_id', string="Dinner")
    category_snack_drinks_ids = fields.One2many('catering.line', 'catering_menu_id', string="Snacks and Drinks")
    category_beverages_ids = fields.One2many('catering.line', 'catering_menu_id', string="Beverages")

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('deliver', 'Delivered'),
            ('invoice', 'Invoiced'),
            ('expired', 'Expired'),
        ], default="draft"
    )

    def action_confirm(self):
        self.state = 'confirm'

    def action_deliver(self):
        self.state = 'deliver'

    @api.onchange('end_date')
    def _action_expired(self):
        current_date = fields.Date.today()
        # print(current_date)
        for rec in self:
            if rec.end_date:
                if current_date > rec.end_date:
                    self.state = 'expired'
                else:
                    self.state = 'draft'

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

    catering_menu_id = fields.Many2one('catering')
    menu_id = fields.Many2one('catering.menu', string='Item')
    description = fields.Char(string='Description')
    quantity = fields.Integer(string='Quantity', default='1')
    uom = fields.Many2one('uom.uom', string='Unit of Measure', related='menu_id.uom_id')
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    unit_price = fields.Monetary(string='Unit Price', related='menu_id.unit_price')
    price_subtotal = fields.Monetary(string='subtotal')

    @api.onchange('unit_price', 'quantity')
    def _sub_total(self):
        self.price_subtotal = self.unit_price * self.quantity

from odoo import models, fields, api, _


class Catering(models.Model):
    _name = "catering"

    event_id = fields.Many2one('event.booking')
    date = fields.Date('event.booking', related='event_id.booking_date')
    start_date = fields.Date('event.booking', related='event_id.start_date')
    end_date = fields.Date('event.booking', related='event_id.end_date')
    guest = fields.Integer("Number of guests")
    name_sequence = fields.Char(string='Order Reference', required=True, readonly=True, default=lambda self: _('New'))
    welcome_drink = fields.Boolean('Welcome Drink')
    break_fast = fields.Boolean('Break Fast')
    lunch = fields.Boolean('Lunch')
    dinner = fields.Boolean('Dinner')
    snack_drinks = fields.Boolean('Snacks and Drinks')
    beverages = fields.Boolean('Beverages')

    @api.model
    def create(self, vals):
        for rec in vals:

            if vals.get('name_sequence', _('New')) == _('New'):
                vals['name_sequence'] = self.env['ir.sequence'].next_by_code(
                    'catering.sequence') or _('New')
                res = super(Catering, self).create(vals)
            return res

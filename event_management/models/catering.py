from odoo import models, fields, api, _


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

    category_welcome_drink_ids = fields.One2many('catering.menu', 'relation_id')
    category_break_fast_ids = fields.One2many('catering.menu', 'relation_id')
    category_lunch_ids = fields.One2many('catering.menu', 'relation_id')
    category_dinner_ids = fields.One2many('catering.menu', 'relation_id')
    category_snack_drinks_ids = fields.One2many('catering.menu', 'relation_id')
    category_beverages_ids = fields.One2many('catering.menu', 'relation_id')

    # description = fields.Char()
    quantity = fields.Float("Quantity")
    uom_id = fields.Many2one('catering.menu', related='category_welcome_drink_ids.uom_id')

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code(
                'catering.sequence') or _('New')
            res = super(Catering, self).create(vals)
        return res

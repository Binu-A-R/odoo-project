from odoo import models, fields


class Catering(models.Model):
    _name = "catering"

    event_id = fields.Many2one('event.booking')
    date = fields.Date('event.booking', related='event_id.booking_date')
    start_date = fields.Date('event.booking', related='event_id.start_date')
    end_date = fields.Date('event.booking', related='event_id.end_date')
    guest = fields.Integer("Number of guests")




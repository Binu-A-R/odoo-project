from odoo import fields, models


class EventBooking(models.Model):
    _name = "event.booking"
    _description = "Event Booking"
    _inherit = 'mail.thread', 'mail.activity.mixin'
    event_name = fields.Char("Event Name")
    name = fields.Char("customer", required=True)
    name = fields.Many2one('res.partner')
    event_type = fields.Many2one('event.property')
    booking_date = fields.Date("Booking Date")
    start_date = fields.Datetime("Start Date")
    end_date = fields.Datetime("End Date")


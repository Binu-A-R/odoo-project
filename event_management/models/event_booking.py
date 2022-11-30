
from odoo import fields, models, api
from datetime import datetime


class EventBooking(models.Model):
    _name = "event.booking"
    _description = "Event Booking"
    _inherit = 'mail.thread', 'mail.activity.mixin'
    event_name = fields.Char(" ", readonly=True, compute="name_get")
    partner_id = fields.Many2one('res.partner', required=True)
    event_type_id = fields.Many2one('event.property', required=True)
    booking_date = fields.Date("Booking Date")
    start_date = fields.Datetime("Start Date", required=True)
    end_date = fields.Datetime("End Date", required=True)
    duration_id = fields.Char(string='Duration', compute='_duration_id')

    @api.onchange('start_date', 'end_date')
    def _duration_id(self):
        if self.start_date and self.end_date:
            start_date = datetime.strptime(str(self.start_date), '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(str(self.end_date), '%Y-%m-%d %H:%M:%S')
            duration = end_date - start_date
            self.duration_id = str(duration.days)

    def name_get(self):
        sequence = []
        for rec in self:
            rec.event_name = str(
                '%s: %s /%s: %s' % (rec.event_type_id.name, rec.partner_id.name, rec.start_date, rec.end_date))
            sequence.append(
                (rec.id, '%s : %s / %s : %s' % (rec.event_type_id.name, rec.partner_id.name, rec.start_date,
                                                rec.end_date)))
        return sequence

    def action_catering_service(self):
        return {
            'name': 'catering',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'catering',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': ({'default_event_id': self.id})
        }

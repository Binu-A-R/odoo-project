# -*- coding: utf-8 -*-

from odoo import models, fields


class EventReport(models.TransientModel):
    _name = 'event.report'

    from_date = fields.Date('Date From')
    to_date = fields.Date('Date To')
    event_type_id = fields.Many2one('event.property')
    is_catering = fields.Boolean('Include catering')

    def print_report(self):

        query = """SELECT ep.name AS event_type, eb.booking_date AS booking_date ,
             rp.name as customer, eb.state as status, c.grand_total, eb.event_name FROM event_property AS ep inner
          join event_booking AS eb on eb.event_type_id
           = ep.id inner join res_partner AS rp on
         eb.partner_id = rp.id inner join catering AS c on c.id = eb.id"""

        if self.event_type_id:
            query += """ where ep.id = %d""" % self.event_type_id
            print('event_type-->', query)
            print('event_type_id-->', self.event_type_id)
        if self.from_date:
            query += """ and eb.start_date > '%s'""" % self.from_date
            print('event_type-->', query)
            print('start_date-->', self.from_date)
        if self.to_date:
            query += """ and eb.end_date < '%s'""" % self.to_date
            print('event_type-->', query)
            print('to_date-->', self.to_date)
         # if self.state:

        self.env.cr.execute(query)
        event = self.env.cr.dictfetchall()

        print('query_data--->', event)

        data = {
            'form': self.read()[0],
            'event': event
        }
        print('data ---->', data)
        return self.env.ref('event_management.action_report_event').report_action(self, data=data)

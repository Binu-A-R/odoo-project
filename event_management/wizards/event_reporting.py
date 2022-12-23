# -*- coding: utf-8 -*-

from odoo import models, fields

# state = {
#     'draft': 'Draft',
#     'catering done': 'Catering Done',
#     'confirm': 'Confirmed',
#     'invoice': 'Invoiced'
# }


class EventReport(models.TransientModel):
    _name = 'event.report'

    from_date = fields.Date('Date From')
    to_date = fields.Date('Date To')
    event_type_id = fields.Many2one('event.property')
    is_catering = fields.Boolean('Include catering')

    def print_report(self):
        query = """SELECT ep.name AS event_type, eb.booking_date AS booking_date ,
                        rp.name as customer, eb.state, c.grand_total, eb.event_name ,
                        cm.dish_name,cm.category,cm.unit_price,cl.description,cl.quantity,cl.price_subtotal
                   FROM event_property AS ep 
                   INNER JOIN event_booking AS eb ON eb.event_type_id = ep.id 
                   INNER JOIN res_partner AS rp ON eb.partner_id = rp.id 
                   INNER JOIN catering AS c ON c.id = eb.id
                   INNER JOIN catering_line AS cl ON c.id = cl.welcome_drinks_menu_id OR cl.break_fast_menu_id = c.id 
                        OR cl.dinner_menu_id = c.id OR cl.lunch_menu_id = c.id OR cl.snacks_drink_menu_id = c.id 
                        OR cl.beverages_menu_id = c.id
                   INNER JOIN catering_menu AS cm ON cm.id = cl.menu_id
                   """

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

        self.env.cr.execute(query)
        event = self.env.cr.dictfetchall()
        val = []
        value = ' '

        total = 0
        for rec in event:
            if rec['state'] == 'draft':
                value = "Draft"
            elif rec['state'] == 'catering done':
                value = "Catering Done"
            elif rec['state'] == 'confirm':
                value = "Confirmed"
            elif rec['state'] == 'invoice':
                value = "Invoiced"

            print('value---->', value)
            if {'event_name': rec['event_name'], 'event_type': rec['event_type'], 'customer': rec['customer'],
                    'booking_date': rec['booking_date'], 'state': value, 'grand_total': rec['grand_total']} \
                    in val:
                pass
            else:
                val.append({'event_name': rec['event_name'],
                            'event_type': rec['event_type'],
                            'customer': rec['customer'],
                            'booking_date': rec['booking_date'],
                            'state': value,
                            'grand_total': rec['grand_total']
                            })
                total += rec['grand_total']
                print('grand_total------>', total)

        print('query_data--->', event)
        data = {
            'form': self.read()[0],
            'event': event,
            'total': total,
            'val': val,
        }
        print('data ---->', data)
        return self.env.ref('event_management.action_report_event').report_action(self, data=data)

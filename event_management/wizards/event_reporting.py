# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import ValidationError
from odoo.tools import date_utils
import io
import json
from datetime import date

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class EventReport(models.TransientModel):
    _name = 'event.report'

    from_date = fields.Date('Date From')
    to_date = fields.Date('Date To')
    event_type_id = fields.Many2one('event.property')
    is_catering = fields.Boolean('Include catering')

    def print_report(self):
        query = """SELECT ep.name AS event_type, eb.booking_date AS booking_date ,
                        rp.name as customer, eb.state, c.grand_total, eb.event_name ,
                        cm.dish_name,cm.category,cm.unit_price,cl.description,cl.quantity,cl.price_sub_total
                   FROM event_property AS ep 
                   INNER JOIN event_booking AS eb ON eb.event_type_id = ep.id 
                   INNER JOIN res_partner AS rp ON eb.partner_id = rp.id 
                   INNER JOIN catering AS c ON c.event_id = eb.id
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

        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError("**** From date greater than To date.****")

        self.env.cr.execute(query)
        event = self.env.cr.dictfetchall()
        val = []
        value = ' '

        total = 0
        for rec in event:
            if rec['state'] == 'draft':
                value = "Draft"
            elif rec['state'] == 'catering_done':
                value = "Catering Done"
            elif rec['state'] == 'confirm':
                value = "Confirmed"
            elif rec['state'] == 'invoice':
                value = "Invoiced"
            elif rec['state'] == 'paid':
                value = "Paid"

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
        print('data')
        print('data ---->', data)
        return self.env.ref('event_management.action_report_event').report_action(self, data=data)

    def xlsx_report(self):
        print('print excel')
        query = """SELECT ep.name AS event_type, eb.booking_date AS booking_date ,
                        rp.name as customer, eb.state, c.grand_total, eb.event_name ,
                        cm.dish_name,cm.category,cm.unit_price,cl.description,cl.quantity,cl.price_sub_total
                   FROM event_property AS ep 
                   INNER JOIN event_booking AS eb ON eb.event_type_id = ep.id 
                   INNER JOIN res_partner AS rp ON eb.partner_id = rp.id 
                   INNER JOIN catering AS c ON c.event_id = eb.id
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

        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError("**** From date greater than To date.****")

        if self.to_date:
            query += """ and eb.end_date < '%s'""" % self.to_date
            print('event_type-->', query)
            print('to_date-->', self.to_date)

        self.env.cr.execute(query)
        event = self.env.cr.dictfetchall()

        print('query_data--->', event)
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'event_type_id': self.event_type_id.name,
            'is_catering': self.is_catering,
            'event': event
        }
        print('data ---->', data)
        return {'type': 'ir.actions.report',
                'data': {'model': 'event.report', 'output_format': 'xlsx',
                         'options': json.dumps(data, default=date_utils.json_default),
                         'report_name': 'XLSX report', },
                'report_type': 'xlsx'}

    def get_xlsx_report(self, data, response):

        print('get excel--->')
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'font_size': '12px'})
        head = workbook.add_format({'align': 'center', 'border': True, 'bold': True, 'font_size': '20px',
                                    'font_color': 'red'})
        txt = workbook.add_format({'font_size': '10px'})
        align = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('B2:R3', 'Event Management Report', head)
        current_date = str(date.today())
        total_style = workbook.add_format({'font_size': '12px', 'align': 'center', 'border': True,
                                           'bold': True, 'font_color': 'black'})
        head_style = workbook.add_format({'font_size': '10px', 'align': 'center', 'bold': True, 'font_color': 'black'})
        head_total = workbook.add_format({'align': 'center', 'border': True, 'bold': True, 'font_size': '12px',
                                          'font_color': 'red'})

        if data['from_date'] and data['to_date']:
            sheet.write('B6', 'From:', cell_format)
            sheet.merge_range('C6:D6', data['from_date'], cell_format)
            sheet.write('B8', 'To:', cell_format)
            sheet.merge_range('C8:D8', data['to_date'], cell_format)

        elif data['from_date']:
            sheet.write('B6', 'From:', cell_format)
            sheet.merge_range('D6:E6', data['from_date'], cell_format)
            sheet.merge_range('B8:C8', 'Printed Date:', cell_format)
            sheet.merge_range('D8:E8', current_date, cell_format)

        elif data['to_date']:
            sheet.write('B6', 'To:', cell_format)
            sheet.merge_range('D6:E6', data['to_date'], cell_format)
            sheet.merge_range('B8:C8', 'Printed Date:', cell_format)
            sheet.merge_range('D8:E8', current_date, cell_format)

        else:
            sheet.write('B7', 'Date:', cell_format)
            sheet.merge_range('C7:D7', current_date, txt)

        if data['event_type_id']:
            sheet.write('B10', 'Event:', cell_format)
            sheet.merge_range('C10:D10', data['event_type_id'], txt)

        print(data['from_date'])
        print(data['to_date'])
        print(data['event_type_id'])
        print(data['event'])
        bold = workbook.add_format({'align': 'center', 'bold': True, 'font_color': 'blue'})
        sheet.write('B12', 'Sl.NO', bold)

        if data['event_type_id']:
            sheet.merge_range('C12:I12', 'EVENT NAME', bold)
            sheet.merge_range('J12:K12', 'CUSTOMER', bold)
            sheet.merge_range('L12:M12', 'BOOKING DATE', bold)
            sheet.merge_range('N12:O12', 'STATUS', bold)
            sheet.merge_range('P12:R12', 'TOTAL AMOUNT', bold)

        else:
            sheet.merge_range('C12:K12', 'EVENT NAME', bold)
            sheet.merge_range('L12:O12', 'EVENT TYPE', bold)
            sheet.merge_range('P12:R12', 'TOTAL AMOUNT', bold)

        index = 1
        col = 0
        row = 12
        total = 0
        val = []
        value = ' '
        for rec in data['event']:

            if {'event_name': rec['event_name'], 'event_type': rec['event_type'], 'customer': rec['customer'],
                'booking_date': rec['booking_date'], 'state': rec['state'], 'grand_total': rec['grand_total']} \
                    in val:
                pass
            else:
                val.append({'event_name': rec['event_name'],
                            'event_type': rec['event_type'],
                            'customer': rec['customer'],
                            'booking_date': rec['booking_date'],
                            'state': rec['state'],
                            'grand_total': rec['grand_total']
                            })
        for record in val:
            print('loop--->:', record)
            if record['state'] == 'draft':
                value = "Draft"
            elif record['state'] == 'catering_done':
                value = "Catering Done"
            elif record['state'] == 'confirm':
                value = "Confirmed"
            elif record['state'] == 'invoice':
                value = "Invoiced"
            elif record['state'] == 'paid':
                value = "Paid"

            total += record['grand_total']
            print('grand_total------>', total)
            sheet.write(row, col + 1, index, align)

            if data['event_type_id']:
                sheet.merge_range(row, col + 2, row, col + 8, record['event_name'], txt)
                sheet.merge_range(row, col + 9, row, col + 10, record['customer'], txt)
                sheet.merge_range(row, col + 11, row, col + 12, record['booking_date'], txt)
                sheet.merge_range(row, col + 13, row, col + 14, value, txt)
                sheet.merge_range(row, col + 15, row, col + 17, record['grand_total'], align)
            else:
                sheet.merge_range(row, col + 2, row, col + 10, record['event_name'], txt)
                sheet.merge_range(row, col + 11, row, col + 14, record['event_type'], txt)
                sheet.merge_range(row, col + 15, row, col + 17, record['grand_total'], head_style)

            index += 1
            row += 1
            if data['is_catering']:
                sheet.merge_range(row, col + 2, row, col + 4, 'Item', head_style)
                sheet.merge_range(row, col + 5, row, col + 7, 'Category', head_style)
                sheet.merge_range(row, col + 8, row, col + 10, 'Description', head_style)
                sheet.merge_range(row, col + 11, row, col + 12, 'Quantity', head_style)
                sheet.merge_range(row, col + 13, row, col + 14, 'Unit Price', head_style)
                sheet.merge_range(row, col + 15, row, col + 17, 'Subtotal', head_style)
                row += 1

                for line in data['event']:
                    print('line--->', line)
                    if line['event_name'] == record['event_name']:
                        print('result', line['event_name'] == record['event_name'])

                        sheet.merge_range(row, col + 2, row, col + 4, line['dish_name'], txt)
                        sheet.merge_range(row, col + 5, row, col + 7, line['category'], txt)
                        sheet.merge_range(row, col + 8, row, col + 10, line['description'], txt)
                        sheet.merge_range(row, col + 11, row, col + 12, line['quantity'], align)
                        sheet.merge_range(row, col + 13, row, col + 14, line['unit_price'], align)
                        sheet.merge_range(row, col + 15, row, col + 17, line['price_sub_total'], align)
                        row += 1
                row += 2
        sheet.write(row + 1, col + 14, 'TOTAL', total_style)
        sheet.merge_range(row + 1, col + 15, row + 1, col + 17, total, head_total)

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()

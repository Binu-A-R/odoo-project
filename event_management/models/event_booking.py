# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime


class EventBooking(models.Model):
    _name = "event.booking"
    _description = "Event Booking"
    _inherit = 'mail.thread', 'mail.activity.mixin'
    event_name = fields.Char(" ", readonly=True, store=True, compute="name_get")
    partner_id = fields.Many2one('res.partner', required=True)
    event_type_id = fields.Many2one('event.property', required=True)
    booking_date = fields.Date("Booking Date")
    start_date = fields.Datetime("Start Date", required=True)
    end_date = fields.Datetime("End Date", required=True)
    duration = fields.Char(string='Duration', compute='onchange_duration_id')

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('catering_done', 'Catering Done'),
            ('confirm', 'Confirmed'),
            ('invoice', 'Invoiced'),
            ('paid', 'Paid')

        ], default="draft"
    )
    invoice_id = fields.Many2one('account.move')

    def action_confirm(self):
        self.state = 'confirm'
        self.env['catering'].search([('state', '=', 'draft')]).action_confirm()

    @api.onchange('start_date', 'end_date')
    def onchange_duration_id(self):
        if self.start_date and self.end_date:
            start_date = datetime.strptime(str(self.start_date), '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(str(self.end_date), '%Y-%m-%d %H:%M:%S')
            duration = end_date - start_date
            self.duration = str(duration.days)

    @api.depends('event_type_id.name', 'event_type_id', 'partner_id.name', 'partner_id', 'start_date', 'end_date')
    def name_get(self):
        sequence = []

        for rec in self:
            # print('rec-->',rec)
            if rec.event_type_id.name and rec.partner_id.name and rec.start_date and rec.end_date:
                rec.event_name = str(
                    '%s: %s /%s: %s' % (rec.event_type_id.name, rec.partner_id.name, rec.start_date, rec.end_date))
                sequence.append(
                    (rec.id, '%s : %s / %s : %s' % (rec.event_type_id.name, rec.partner_id.name, rec.start_date,
                                                    rec.end_date)))

        return sequence

    def action_catering_service(self):
        self.state = "catering_done"
        return {
            'name': 'catering',
            'view_mode': 'form',
            'res_model': 'catering',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {'default_event_id': self.id}
        }

    def action_invoice(self):
        self.write({'state': 'invoice'})

        vals = []
        rec = self.env['catering'].search([('event_id', '=', self.id)])
        for line in rec.category_welcome_drink_ids:
            vals.append((0, 0,
                         {
                             'name': line.menu_id.dish_name,
                             'quantity': line.quantity,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.price_subtotal
                         }))
        for line in rec.category_break_fast_ids:
            vals.append((0, 0,
                         {
                             'name': line.menu_id.dish_name,
                             'quantity': line.quantity,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.price_subtotal
                         }))
        for line in rec.category_lunch_ids:
            vals.append((0, 0,
                         {
                             'name': line.menu_id.dish_name,
                             'quantity': line.quantity,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.price_subtotal
                         }))
        for line in rec.category_dinner_ids:
            vals.append((0, 0,
                         {
                             'name': line.menu_id.dish_name,
                             'quantity': line.quantity,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.price_subtotal
                         }))

        for line in rec.category_snack_drinks_ids:
            vals.append((0, 0,
                         {
                             'name': line.menu_id.dish_name,
                             'quantity': line.quantity,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.price_subtotal
                         }))

        for line in rec.category_beverages_ids:
            vals.append((0, 0,
                         {
                             'name': line.menu_id.dish_name,
                             'quantity': line.quantity,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.price_subtotal
                         }))

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'invoice_line_ids': vals,
        })

        self.invoice_id = invoice.id
        return {
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def action_view_invoice(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'invoice',
            'view_mode': 'tree',
            'view_id': self.env.ref('account.view_move_form').id,
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'target': 'current',

        }
        # return result

    def action_view_catering(self):
        # event = self.env['catering'].search([('event_id', '=', self.id)])
        # event_id = event
        return {
            'type': 'ir.actions.act_window',
            'name': 'catering',
            'view_mode': 'tree,form',
            'res_model': 'catering',
            # 'res_id': event.id,
            'target': 'current',
            'context': {'default_event_id': self.id},
            'domain': [('event_id', '=', self.id)]

        }


class EventBookingInvoice(models.Model):
    _inherit = 'account.move'

    def action_register_payment(self):
        res = super(EventBookingInvoice, self).action_register_payment()
        if res:
            self.payment_state = 'paid'
            state = self.env['event.booking'].search([('invoice_id', '=', self.id)])
            print('id =>', self.id)
            print('state =>', state)
            state.write({'state': 'paid'})

# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.tools import date_utils
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    is_discount_limit = fields.Boolean("Discount of the month", config_parameter='sale_order.discount_limit')
    total_amount_limit = fields.Float(string="Default Limit", config_parameter='sale_order.total_amount_limit')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        sale_orders = self.search([])
        discount = 0
        total_discount = 0
        for record in self.order_line:
            discount += record.discount

        for rec in sale_orders:
            order_date = rec.date_order.date()
            starting_month = date_utils.start_of(order_date, "month")
            ending_month = date_utils.end_of(order_date, "month")
            if starting_month <= order_date <= ending_month:
                for discount_per_line in rec.order_line:
                    calculate_discount = ((discount_per_line.product_uom_qty * discount_per_line.price_unit) -
                                          discount_per_line.price_subtotal)
                    total_discount += calculate_discount
                    print('total_discount:', total_discount)
        discount_limit = float(self.env['ir.config_parameter'].sudo().get_param('sale_order.total_amount_limit'))
        print('discount_limit', discount_limit)
        if total_discount > discount_limit and discount > 0 and bool(self.env['ir.config_parameter'].sudo().get_param('sale_order.discount_limit')) == True:
            print('True')
            raise ValidationError("Total discount of the month is exceed the limit.")
        res = super(SaleOrder, self).action_confirm()
        return res

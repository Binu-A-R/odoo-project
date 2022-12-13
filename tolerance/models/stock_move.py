# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToleranceStockMove(models.Model):
    _inherit = "stock.move"

    stock_tolerance = fields.Float("Tolerance")


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, values, group_id):
        res = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id,
                                                            name, origin, values, group_id)
        res['stock_tolerance'] = group_id.get('stock_tolerance', False)
        return res

    @api.model
    def _prepare_purchase_order_line(self, product_id, product_qty, product_uom, values, po, supplier):
        res = super(StockRule)._prepare_purchase_order_line(product_id, product_qty, product_uom, values, po, supplier)

        res['stock_tolerance'] = values.get('stock_tolerance', False)
        return res


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        print("heloo")
        for record in self.move_ids:
            print("heloo1")

            if record.sale_line_id:
                tolerance = record.sale_line_id.sale_tolerance
            if record.purchase_line_id:
                tolerance = record.purchase_line_id.purchase_tolerance
            minimum_tolerance = record.product_uom_qty - tolerance
            maximum_tolerance = record.product_uom_qty + tolerance
            if (not minimum_tolerance <= record.quantity_done <= maximum_tolerance) or\
                    (not minimum_tolerance >= record.quantity_done >= maximum_tolerance):
                return {
                    'name': 'Warning',
                    'type': 'ir.actions.act_window',
                    'res_model': 'warning',
                    'view_mode': 'form',
                    'target': 'new'

                }

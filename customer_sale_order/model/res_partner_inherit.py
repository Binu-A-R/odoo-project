from odoo import fields, models


class Customer(models.Model):
    _inherit = 'res.partner'


    sale_orders_id = fields.One2many('sale.order','partner_id')

    no_of_sold = fields.Integer(compute="_no_of_sold")

    def sold_product(self):
        self.ensure_one()

        return {
            'name': "_",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'product.product',
            'domain': [('id', '=', self.sale_order_ids.order_line.mapped('product_id.id'))]        }

    def _no_of_sold(self):
        record = self.env["sale.order"].search([('partner_id', '=', self.id)])
        self.no_of_sold = 0
        for rec in record:
            self.no_of_sold=self.no_of_sold+1
            print(rec)


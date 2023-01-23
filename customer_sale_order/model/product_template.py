from odoo import fields, models,api,_


class Number_of_product_sold(models.Model):
    _inherit = 'product.template'

    num_sold = fields.Float(compute="_no_sold")





    def _no_sold(self):
        record = self.env["sale.order"].search([('state', '!=', 'draft')])
        self.num_sold = 0
        # print(record)
        for rec in record:
            for line in rec.order_line:
                # print(line.product_id.product_tmpl_id)
                if line.product_id.product_tmpl_id.id == self.id:
                    self.num_sold = self.num_sold + line.product_uom_qty




    @api.onchange('list_price')
    def _list_price(self):
        print(self.ids)

        data = self.env["sale.order.line"].search([('order_id.state','!=','sale'),('product_id.product_tmpl_id','in',self.ids)])
        print(data.product_id.product_tmpl_id)
        for rec in data:
            rec.price_unit = self.list_price







from odoo import models, fields, api


class EventManagement(models.Model):
    _name = "event.service"
    _description = "event.service"

    name = fields.Char("Name",  required=True)
    user_id = fields.Many2one('res.users', string='Responsible Person')
    order_ids = fields.One2many("event.service.tab", "relation_id", string="order line")
    # company_id = fields.Many2one('res.company', string="Company")
    # currency_id = fields.Many2one('res.currency', string="Currency",
    #                               related='company_id.currency_id',
    #                               default=lambda self: self.env.user.company_id.currency_id.id, invisible="1")
    #
    # price_total = fields.Monetary(string='Total', compute='_compute_total_amount')
    #
    # @api.onchange('order_ids.price_subtotal')
    # def _compute_total_amount(self):
    #     for rec in self:
    #         rec.price_total = sum(rec.order_ids.mapped('price_subtotal'))

    class ServiceTab(models.Model):
        _name = "event.service.tab"
        _description = "Service line"

        relation_id = fields.Many2one('event.service')
        description = fields.Char(string="Description")
        quantity = fields.Integer(string="Quantity")
        unit_price = fields.Float(string="Unit Price")
        company_id = fields.Many2one('res.company', string="Company")
        currency_id = fields.Many2one('res.currency', string="Currency",
                                      related='company_id.currency_id',
                                      default=lambda self: self.env.user.company_id.currency_id.id, invisible="1")
        price_subtotal = fields.Monetary(string="Subtotal")

        @api.onchange('unit_price', 'quantity')
        def _compute_sub_total(self):
            for rec in self:
                rec.price_subtotal = rec.unit_price * rec.quantity


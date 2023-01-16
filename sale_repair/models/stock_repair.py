# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class SaleRepair(models.Model):
    _name = 'sale.repair'
    _rec_name = 'name_sequence'
    _inherit = 'mail.thread', 'mail.activity.mixin'

    name_sequence = fields.Char(string='Order Reference', readonly=True, default=lambda self: _('New'))
    sale_id = fields.Many2one('sale.order', string=' Sale Order', domain="[('state', '=', 'sale')]")
    # sale_line_id = fields.Many2one('sale.order.line')

    product_id = fields.Many2one('product.product', readonly=False)
    partner_id = fields.Many2one(related='sale_id.partner_id')

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('done', 'Done'),
        ], default="draft"
    )

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code(
                'repair.sequence') or _('New')
            res = super(SaleRepair, self).create(vals)
            return res

    @api.onchange('sale_id')
    def _onchange_invoice_id(self):
        products = self.sale_id.order_line.product_id
        return {'domain': {'product_id': [('id', 'in', products.ids)]}}

    def action_confirm(self):
        self.state = 'confirm'
        self.sale_id.is_repair = True


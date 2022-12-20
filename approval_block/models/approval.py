# -*- coding: utf-8 -*-

from odoo import models, fields


class ApprovalBlock(models.Model):
    _name = "approval_block.approval"
    _rec_name = 'name'

    name = fields.Char("Name")
    amount = fields.Float("Amount")
    # company_id = fields.Many2one('res.company', string="Company")
    # currency_id = fields.Many2one('res.currency', string="Currency",
    #                               related='company_id.currency_id',
    #                               default=lambda self: self.env.user.company_id.currency_id.id, invisible="1")
    #
    # user_id = fields.Many2one("res.users", string="Manager")

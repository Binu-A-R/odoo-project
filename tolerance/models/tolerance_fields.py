# -*- coding: utf-8 -*-

from odoo import models, fields


class ToleranceField(models.Model):

    _inherit = "res.partner"

    tolerance = fields.Float("Tolerance (%)")

from odoo import models, fields


class EventManagement(models.Model):
    _name = "event.service"
    _description = "event.service"

    name = fields.Char("Name")
    # responsible = fields.Many2one('res.user')

from odoo import models, fields


class EventManagement(models.Model):
    _name = "event.property"
    _description = "event.property"
    name = fields.Char('Event Type:')
    code = fields.Char('Code:')
    image = fields.Binary('Image:')

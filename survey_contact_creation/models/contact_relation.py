# -*- coding: utf-8 -*-

from odoo import models, fields


class ContactCreationSurvey(models.Model):

    _inherit = 'survey.survey'

    ques_ids = fields.One2many('contact.creation', 'connect_id', string='Questions')


class Contact(models.Model):
    _name = "contact.creation"

    question_id = fields.Many2one('survey.question')
    partner_id = fields.Many2one('ir.model.fields', domain="[('model', '=', 'res.partner')]")
    connect_id = fields.Many2one('survey.survey')


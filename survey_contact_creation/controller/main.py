# -*- coding: utf-8 -*-
from odoo.addons.survey.controllers.main import Survey
from odoo import http
from odoo.http import request

class ContactCreationPage(Survey):
    @http.route('/survey/submit/<string:survey_token>/<string:answer_token>', type='json', auth='public', website=True)
    def survey_submit(self, survey_token, answer_token, **post):
        print('iroekfkw')
        # print('gvfhbj ')
        search = super(ContactCreationPage, self).survey_submit(survey_token, answer_token, **post)
        search_question = request.env['survey.question'].browse(int(post['question_id'])).survey_id.ques_ids
        print('search_question--->', search_question)
        search_question_answer = request.env['survey.user_input'].search([('access_token','=',answer_token)])
        print('search_ans--->', search_question_answer)

        field_name = []

        for rec in search_question:
            print('rec--->', rec)
            field_name.append(rec.partner_id.name)
            print('field-->', field_name)
        field_ans = search_question_answer.user_input_line_ids.mapped('value_char_box')
        print('field_ans',field_ans)
        dic = dict(zip(field_name,field_ans))
        contact_list = request.env['res.partner'].create(dic)
        print('contact_details',contact_list)
        return search





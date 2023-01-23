# -*- coding: utf-8 -*-
from odoo.addons.survey.controllers.main import Survey
from odoo import http
from odoo.http import request


class ContactCreationPage(Survey):
    @http.route('/survey/submit/<string:survey_token>/<string:answer_token>', type='json', auth='public', website=True)
    def survey_submit(self, survey_token, answer_token, **post):
        print('iroekfkw')
        print('gvfhbj ')
        access_data = self._get_access_data(survey_token, answer_token, ensure_token=True)

        survey_sudo, answer_sudo = access_data['survey_sudo'], access_data['answer_sudo']
        # if answer_sudo.survey_time_limit_reached or survey_sudo.questions_layout == 'one_page':

        print('answer' , answer_sudo)
        print('survey_sudo' , survey_sudo)
        # y = survey_sudo._get_next_page_or_question(
        #     answer_sudo,
        #     answer_sudo.last_displayed_page_id.id if answer_sudo.last_displayed_page_id else 0)
        # print("bbbbbbbbb", answer_sudo)
        # print("mmmmmmmmmm", answer_sudo.last_displayed_page_id.id)
        # print("jjjjjjjjjjjjj", answer_sudo.last_displayed_page_id)
        # print("yyyyyyyyy", y)
        # print("*******", survey_sudo._is_last_page_or_question(answer_sudo, y))

        search = super(ContactCreationPage, self).survey_submit(survey_token, answer_token, **post)
        # next_page = survey_sudo._get_next_page_or_question(answer_sudo, page_or_question_id)

        search_question = request.env['survey.question'].browse(int(post['question_id'])).survey_id.ques_ids
        print('search_question--->', search_question)
        search_question_answer = request.env['survey.user_input'].search([('access_token', '=', answer_token)])
        print('search_ans--->', search_question_answer)

        field_name = []

        for rec in search_question:
            print('rec--->', rec)
            field_name.append(rec.partner_id.name)
            print('field_name-->', field_name)
        field_ans = search_question_answer.user_input_line_ids.mapped('value_char_box')
        partner = request.env['res.partner'].search([])
        print(partner)
        # id = request.env['res.partner'].search(['name'])

        print('field_ans', field_ans)
        dic = dict(zip(field_name, field_ans))
        print('dic', dic)
        contact_list = request.env['res.partner'].create(dic)

        # len =1
        # test=[]

        # for res in search_question:
        #     test.append(res.question_id.id)
        #     print('test-->', test)
        #     print(len(test))
        #
        #     if test[res] == len(test):
        #         print('write')
        #
        #         contact_list = request.env['res.partner'].write(dic)
        #         print('contact_details', contact_list)
        #
        #     else:
        #         print('created')
        #         contact_list = request.env['res.partner'].create(dic)
        #         print('contact_details', contact_list)
        #

        print('contact_details', contact_list)
        return search


    # access_data = self._get_access_data(survey_token, answer_token, ensure_token=True)
    # if access_data['validity_code'] is not True:
    #     return {'error': access_data['validity_code']}
    # survey_sudo, answer_sudo = access_data['survey_sudo'], access_data['answer_sudo']
    #
    # if answer_sudo.state == 'done':
    #     return {'error': 'unauthorized'}
    #
    # questions, page_or_question_id = survey_sudo._get_survey_questions(answer=answer_sudo,
    #                                                                    page_id=post.get('page_id'),
    #                                                                    question_id=post.get('question_id'))
    #
    # if not answer_sudo.test_entry and not survey_sudo._has_attempts_left(answer_sudo.partner_id, answer_sudo.email, answer_sudo.invite_token):
    #     # prevent cheating with users creating multiple 'user_input' before their last attempt
    #     return {'error': 'unauthorized'}
    #
    # if answer_sudo.survey_time_limit_reached or answer_sudo.question_time_limit_reached:
    #     if answer_sudo.question_time_limit_reached:
    #         time_limit = survey_sudo.session_question_start_time + relativedelta(
    #             seconds=survey_sudo.session_question_id.time_limit
    #         )
    #         time_limit += timedelta(seconds=3)
    #     else:
    #         time_limit = answer_sudo.start_datetime + timedelta(minutes=survey_sudo.time_limit)
    #         time_limit += timedelta(seconds=10)
    #     if fields.Datetime.now() > time_limit:
    #         # prevent cheating with users blocking the JS timer and taking all their time to answer
    #         return {'error': 'unauthorized'}
    #
    # errors = {}
    # # Prepare answers / comment by question, validate and save answers
    # for question in questions:
    #     inactive_questions = request.env['survey.question'] if answer_sudo.is_session_answer else answer_sudo._get_inactive_conditional_questions()
    #     if question in inactive_questions:  # if question is inactive, skip validation and save
    #         continue
    #     answer, comment = self._extract_comment_from_answers(question, post.get(str(question.id)))
    #     errors.update(question.validate_question(answer, comment))
    #     if not errors.get(question.id):
    #         answer_sudo.save_lines(question, answer, comment)
    #
    # if errors and not (answer_sudo.survey_time_limit_reached or answer_sudo.question_time_limit_reached):
    #     return {'error': 'validation', 'fields': errors}
    #
    # if not answer_sudo.is_session_answer:
    #     answer_sudo._clear_inactive_conditional_answers()
    #
    # if answer_sudo.survey_time_limit_reached or survey_sudo.questions_layout == 'one_page':
    #     answer_sudo._mark_done()
    # elif 'previous_page_id' in post:
    #     # when going back, save the last displayed to reload the survey where the user left it.
    #     answer_sudo.write({'last_displayed_page_id': post['previous_page_id']})
    #     # Go back to specific page using the breadcrumb. Lines are saved and survey continues
    #     return self._prepare_question_html(survey_sudo, answer_sudo, **post)
    # else:
    #     if not answer_sudo.is_session_answer:
    #         next_page = survey_sudo._get_next_page_or_question(answer_sudo, page_or_question_id)
    #         if not next_page:
    #
    #             search_question = request.env['survey.question'].browse(int(post['question_id'])).survey_id.ques_ids
    #             print('search_question--->', search_question)
    #             search_question_answer = request.env['survey.user_input'].search(
    #                 [('access_token', '=', answer_token)])
    #             print('search_ans--->', search_question_answer)
    #
    #             field_name = []
    #
    #             for rec in search_question:
    #                 print('rec--->', rec)
    #                 field_name.append(rec.partner_id.name)
    #                 print('field-->', field_name)
    #             field_ans = search_question_answer.user_input_line_ids.mapped('value_char_box')
    #             print('field_ans', field_ans)
    #             dic = dict(zip(field_name, field_ans))
    #
    #             contact_list = request.env['res.partner'].create(dic)
    #
    #             print('contact_details', contact_list)
    #             answer_sudo._mark_done()
    #
    #     answer_sudo.write({'last_displayed_page_id': page_or_question_id})
    #
    # return self._prepare_question_html(survey_sudo, answer_sudo)
    #
    #

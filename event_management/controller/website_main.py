# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request


class WebsitePage(http.Controller):
    @http.route('/event_booking', type='http', auth='public', website=True)
    def event_page(self, **kw):
        customer = request.env['res.partner'].sudo().search([])
        event_type = request.env['event.property'].sudo().search([])
        return http.request.render('event_management.website_page', {'customer': customer, 'event_type': event_type})

    @http.route(['/event_booking/form/submit'], type='http', auth="public", website=True)
    def event_form_submit(self, **post):

        print(post)
        print('event-type---->', post.get('event_type'))
        booking = request.env['event.booking'].sudo().create({
            'event_type_id': int(post.get('event')),
            'partner_id': int(post.get('partner')),
            'booking_date': post.get('booking_date'),
            'start_date': post.get('start_date'),
            'end_date': post.get('end_date'),

        })

        welcome_drink = request.env['catering.menu'].sudo().search([('category', '=', 'Welcome Drink')])
        break_fast = request.env['catering.menu'].sudo().search([('category', '=', 'Break Fast')])
        lunch = request.env['catering.menu'].sudo().search([('category', '=', 'Lunch')])
        dinner = request.env['catering.menu'].sudo().search([('category', '=', 'Dinner')])
        snack_drinks = request.env['catering.menu'].sudo().search([('category', '=', 'Snacks and Drinks')])
        beverages = request.env['catering.menu'].sudo().search([('category', '=', 'Beverages')])
        event_type = request.env['event.booking'].sudo().search([])

        vals = {
            'event_type': event_type,
            'booking': booking,
            'welcome_drink': welcome_drink,
            'break_fast': break_fast,
            'lunch': lunch,
            'dinner': dinner,
            'snack_drinks': snack_drinks,
            'beverages': beverages

        }

        return request.render("event_management.tmp_event_form_success", vals)

    @http.route(['/event_booking/form/submit/catering'], type='http', auth="public", website=True)
    def catering_form_submit(self, **post):
        print(post)

        catering = request.env['catering'].sudo().create({
            'event_id': post.get('event'),
            'guest': post.get('guest')
        })
        print('catering---->', catering)

        if post.get('cate1'):
            catering.update({'is_welcome_drink': True,
                             'category_welcome_drink_ids': [(0, 0, {'menu_id': post.get('welcome_drink')}
                                                             )]
                             })
        val = {
            'catering': catering,
        }
        print('val', val)
        return request.render("event_management.tmp_catering_form_success", val)

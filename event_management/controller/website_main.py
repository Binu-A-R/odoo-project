# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsitePage(http.Controller):
    @http.route('/event_booking', type='http', auth='public', website=True)
    def event_page(self, **kw):
        customer = request.env['res.partner'].sudo().search([])
        event_type = request.env['event.property'].sudo().search([])
        return http.request.render('event_management.website_page', {'customer': customer, 'event_type': event_type})

    @http.route(['/event_booking/form/submit'], type='http', auth="public", website=True)
    # next controller with url for submitting data from the form#
    def event_form_submit(self, **post):
        booking = request.env['event.booking'].sudo().create({
            'event_type_id': int(post.get('event_type')),
            'partner_id': int(post.get('partner')),
            'booking_date': post.get('booking_date'),
            'start_date': post.get('start_date'),
            'end_date': post.get('end_date'),

        })
        vals = {
            'booking': booking,
        }
        return request.render("event_management.tmp_event_form_success", vals)

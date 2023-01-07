# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Event(http.Controller):
    @http.route(['/latest_events'], type="json", auth="public")
    def events(self):
        # latest = request.env['event.booking'].sudo().search([], order='start_date desc')
        latest = request.env['event.booking'].sudo().search_read([], ['partner_id', 'event_type_id', 'start_date',
                                                                      'end_date', 'booking_date'],
                                                                 order='start_date desc')
        # val = {
        #     'latest': latest
        # }
        # print("vals-->>", val)

        return latest

        # response = http.Response(template='event_management_snippet.latest_event_dynamic_snippet', qcontext=val)
        # return response.render()

    @http.route('/booking/<model("event.booking"):latest>', type="http", auth="user", website=True)
    def booking_details(self, latest):
        print('booking Details-->', latest)
        values = {
            'latest': latest,
        }
        return request.render('event_management_snippet.booking_details', values)



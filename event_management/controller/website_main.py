# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsitePage(http.Controller):
    @http.route('/event_booking', type='http', auth='public', website=True)
    def test_page(self, **kw):
        return http.request.render('event_management.website_page_test', {})